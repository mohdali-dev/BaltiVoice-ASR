---
language:
- bft
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
task_ids:
- speech-recognition
pretty_name: BaltiVoice ASR Dataset
size_categories:
- 10K<n<100K
tags:
- balti
- low-resource
- speech
- asr
- gilgit-baltistan
- pakistan
- tibetic
---

# BaltiVoice ASR Dataset

## Dataset Description

BaltiVoice is one of the first publicly available Automatic Speech 
Recognition (ASR) datasets for the Balti language (ISO 639-3: bft), 
a critically low-resource Tibetic language spoken primarily in the 
Gilgit-Baltistan region of Pakistan and parts of India (Ladakh).

This dataset was collected, validated, and processed as part of a 
portfolio research project aimed at building the first open-source 
Balti ASR system using OpenAI Whisper fine-tuning.

---

## Language

| Property        | Detail |
|----------------|--------|
| Language        | Balti (بلتی) |
| ISO Code        | bft |
| Language Family | Sino-Tibetan → Tibeto-Burman → Tibetic |
| Script          | Nastaliq (Arabic-based) |
| Region          | Gilgit-Baltistan, Pakistan; Ladakh, India |
| Speakers        | ~300,000–500,000 (estimated) |
| Resource Level  | Critically low-resource |

Balti is considered endangered by many linguists. It has very limited 
digital presence, almost no NLP tooling, and until now, no publicly 
available ASR dataset.

---

## Dataset Statistics

| Split      | Samples | Estimated Hours |
|------------|---------|-----------------|
| Train      | 9,051   | ~15.1 hours     |
| Validation | 1,006   | ~1.7 hours      |
| **Total**  | **10,060** | **~16.8 hours** |

### Audio Properties
| Property         | Value |
|-----------------|-------|
| Format           | WAV (16kHz, mono) |
| Avg Duration     | ~6.0 seconds |
| Min Duration     | ~1.0 seconds |
| Max Duration     | ~15.0 seconds |
| Sample Rate      | 16,000 Hz |

### Text Properties
| Property         | Value |
|-----------------|-------|
| Avg Words/Sentence | 10.12 |
| Avg Characters    | 48.80 |
| Script            | Nastaliq (RTL) |

---

## Dataset Structure

Each sample contains:
- `audio`: 16kHz mono WAV audio array
- `sentence`: Balti transcription in Nastaliq script

```python
{
  "audio": {
    "array": [...],          # numpy array
    "sampling_rate": 16000
  },
  "sentence": "بوا لہ سلام بے اِنپا سلام سہ مہ بیاس"
}
```

---

## Source & Collection

- Base data sourced from **Mozilla Common Voice** Balti (bft) 
  contribution project
- Audio clips were validated for quality and transcription accuracy
- Processed and structured for HuggingFace-compatible ASR training
- Train/validation split applied with `random_state=42` (90/10)

---

## Usage

### Load the dataset

```python
from datasets import load_dataset, Audio

dataset = load_dataset("mohdali1/baltivoice-asr")
dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))

print(dataset)
# DatasetDict({
#     train: Dataset({features: ['audio', 'sentence'], num_rows: 9051})
#     validation: Dataset({features: ['audio', 'sentence'], num_rows: 1006})
# })
```

### Preview a sample

```python
sample = dataset["train"][0]
print("Transcription:", sample["sentence"])
print("Audio shape:", sample["audio"]["array"].shape)
print("Sample rate:", sample["audio"]["sampling_rate"])
```

---

## Model Trained on This Dataset

A fine-tuned Whisper model trained on BaltiVoice is available at:

👉 [mohdali1/whisper-small-balti](https://huggingface.co/mohdali1/whisper-small-balti)

```python
from transformers import pipeline

asr = pipeline(
    "automatic-speech-recognition",
    model="mohdali1/whisper-small-balti"
)
result = asr("your_balti_audio.wav")
print(result["text"])
```

---

## Social Impact

Balti is an endangered language with very limited computational 
resources. This dataset contributes toward:

- Preserving Balti language digitally
- Enabling voice technology for Balti speakers
- Supporting NLP research for low-resource Tibetic languages
- Providing a foundation for future Balti TTS, NER, and MT systems

---

## Limitations

- Audio collected from volunteer contributors — some variation in 
  recording quality
- Vocabulary may be limited to common conversational domains
- Model fine-tuned using Urdu tokenizer as a proxy (closest supported 
  Nastaliq script in Whisper)
- WER metrics are relative to Whisper's Urdu tokenization, not a 
  native Balti tokenizer

---

## License

[Creative Commons Attribution 4.0 (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/)

---

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{baltivoice2025,
  author    = {Mohammad Ali},
  title     = {BaltiVoice: A Low-Resource ASR Dataset for the Balti Language},
  year      = {2025},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/datasets/mohdali1/baltivoice-asr}
}
```

---

## Author

**Mohammad Ali**  
BSc Software Engineering, IUB  
[HuggingFace](https://huggingface.co/mohdali1) · [GitHub](https://github.com/mohdali1)
