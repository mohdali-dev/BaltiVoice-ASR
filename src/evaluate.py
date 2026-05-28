"""
BaltiVoice ASR — Evaluation Script
Measures WER of the fine-tuned model on the validation set.

Usage:
    python src/evaluate.py --token hf_xxx
"""

import argparse
import evaluate
from datasets import load_dataset, Audio
from transformers import pipeline
from tqdm import tqdm


def main(args):
    print("Loading model...")
    asr = pipeline(
        "automatic-speech-recognition",
        model="mohdali1/whisper-small-balti",
        generate_kwargs={"language": "urdu", "task": "transcribe"},
        token=args.token,
    )

    print("Loading validation dataset...")
    dataset = load_dataset(
        "mohdali1/baltivoice-asr",
        split="validation",
        token=args.token
    )
    dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))

    metric = evaluate.load("wer")

    predictions = []
    references  = []

    for sample in tqdm(dataset, desc="Evaluating"):
        result = asr(sample["audio"]["array"])
        predictions.append(result["text"])
        references.append(sample["sentence"])

    wer = 100 * metric.compute(predictions=predictions, references=references)
    print(f"\n📊 Final WER: {wer:.2f}%")

    # Show some examples
    print("\nSample predictions:")
    for i in range(min(5, len(predictions))):
        print(f"  Reference  : {references[i]}")
        print(f"  Prediction : {predictions[i]}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None)
    args = parser.parse_args()
    main(args)
