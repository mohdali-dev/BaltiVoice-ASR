"""
BaltiVoice ASR — Whisper Fine-tuning Script
Fine-tunes openai/whisper-small on the BaltiVoice dataset.

Usage:
    python src/train.py --token hf_xxx --output_dir ./whisper-balti
"""

import argparse
import torch
from dataclasses import dataclass
from typing import Any, Dict, List, Union

import evaluate
from datasets import load_dataset, Audio
from transformers import (
    WhisperFeatureExtractor,
    WhisperTokenizer,
    WhisperProcessor,
    WhisperForConditionalGeneration,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
)


# ── Data Collator ────────────────────────────────────────────
@dataclass
class DataCollatorSpeechSeq2SeqWithPadding:
    processor: Any

    def __call__(self, features: List[Dict[str, Union[List[int], torch.Tensor]]]):
        input_features = [{"input_features": f["input_features"]} for f in features]
        batch = self.processor.feature_extractor.pad(input_features, return_tensors="pt")

        label_features = [{"input_ids": f["labels"]} for f in features]
        labels_batch   = self.processor.tokenizer.pad(label_features, return_tensors="pt")
        labels = labels_batch["input_ids"].masked_fill(
            labels_batch.attention_mask.ne(1), -100
        )
        if (labels[:, 0] == self.processor.tokenizer.bos_token_id).all().cpu().item():
            labels = labels[:, 1:]

        batch["labels"] = labels
        return batch


def main(args):
    # ── Load processor ───────────────────────────────────────
    feature_extractor = WhisperFeatureExtractor.from_pretrained(args.model_name)
    tokenizer  = WhisperTokenizer.from_pretrained(args.model_name, language="urdu", task="transcribe")
    processor  = WhisperProcessor.from_pretrained(args.model_name, language="urdu", task="transcribe")

    # ── Load dataset ─────────────────────────────────────────
    dataset = load_dataset("mohdali1/baltivoice-asr", token=args.token)
    dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))

    # ── Preprocess ───────────────────────────────────────────
    def prepare_dataset(batch):
        audio = batch["audio"]
        batch["input_features"] = feature_extractor(
            audio["array"], sampling_rate=audio["sampling_rate"]
        ).input_features[0]
        batch["labels"] = tokenizer(batch["sentence"]).input_ids
        return batch

    dataset = dataset.map(
        prepare_dataset,
        remove_columns=dataset.column_names["train"],
        num_proc=1
    )

    # ── Model ────────────────────────────────────────────────
    model = WhisperForConditionalGeneration.from_pretrained(args.model_name)
    model.generation_config.language = "urdu"
    model.generation_config.task     = "transcribe"
    model.generation_config.forced_decoder_ids = None

    # ── Metric ───────────────────────────────────────────────
    metric = evaluate.load("wer")

    def compute_metrics(pred):
        pred_ids  = pred.predictions
        label_ids = pred.label_ids
        label_ids[label_ids == -100] = tokenizer.pad_token_id
        pred_str  = tokenizer.batch_decode(pred_ids,  skip_special_tokens=True)
        label_str = tokenizer.batch_decode(label_ids, skip_special_tokens=True)
        return {"wer": 100 * metric.compute(predictions=pred_str, references=label_str)}

    # ── Training args ─────────────────────────────────────────
    training_args = Seq2SeqTrainingArguments(
        output_dir                  = args.output_dir,
        per_device_train_batch_size = 8,
        gradient_accumulation_steps = 2,
        learning_rate               = args.learning_rate,
        warmup_steps                = 100,
        max_steps                   = args.max_steps,
        gradient_checkpointing      = True,
        fp16                        = True,
        eval_strategy               = "steps",
        per_device_eval_batch_size  = 8,
        predict_with_generate       = True,
        generation_max_length       = 225,
        save_steps                  = 250,
        eval_steps                  = 250,
        logging_steps               = 25,
        load_best_model_at_end      = True,
        metric_for_best_model       = "wer",
        greater_is_better           = False,
        push_to_hub                 = False,
    )

    data_collator = DataCollatorSpeechSeq2SeqWithPadding(processor=processor)

    trainer = Seq2SeqTrainer(
        args             = training_args,
        model            = model,
        train_dataset    = dataset["train"],
        eval_dataset     = dataset["validation"],
        data_collator    = data_collator,
        compute_metrics  = compute_metrics,
        processing_class = processor.feature_extractor,
    )

    trainer.train()

    # ── Push to Hub ──────────────────────────────────────────
    if args.token and args.push_to_hub:
        model.push_to_hub("mohdali1/whisper-small-balti", token=args.token)
        processor.push_to_hub("mohdali1/whisper-small-balti", token=args.token)
        print("✅ Model pushed to HuggingFace Hub")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name",    default="openai/whisper-small")
    parser.add_argument("--output_dir",    default="./whisper-balti")
    parser.add_argument("--max_steps",     type=int,   default=1000)
    parser.add_argument("--learning_rate", type=float, default=1e-5)
    parser.add_argument("--token",         default=None)
    parser.add_argument("--push_to_hub",   action="store_true")
    args = parser.parse_args()
    main(args)
