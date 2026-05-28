<div align="center">

# 🎙️ BaltiVoice ASR

### First AI-powered Automatic Speech Recognition System for Balti Language

[![Dataset](https://img.shields.io/badge/🤗%20Dataset-baltivoice--asr-blue)](https://huggingface.co/datasets/mohdali1/baltivoice-asr)
[![Model](https://img.shields.io/badge/🤗%20Model-whisper--small--balti-green)](https://huggingface.co/mohdali1/whisper-small-balti)
[![Demo](https://img.shields.io/badge/🤗%20Demo-baltivoice--demo-orange)](https://huggingface.co/spaces/mohdali1/baltivoice-demo)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)

[**Live Demo**](https://huggingface.co/spaces/mohdali1/baltivoice-demo) · [**Dataset**](https://huggingface.co/datasets/mohdali1/baltivoice-asr) · [**Model**](https://huggingface.co/mohdali1/whisper-small-balti)

</div>

---

## 📖 About

**Balti (بلتی)** is a critically low-resource Tibetic language spoken by ~300,000 people in Gilgit-Baltistan, Pakistan. Despite its cultural significance, Balti has virtually no publicly available NLP or ASR resources.

This project presents:
- 📦 **The first publicly available Balti speech dataset** — 16.8 hours of validated audio
- 🤖 **A fine-tuned Whisper ASR model** achieving **30% WER** on unseen Balti speech
- 🎙️ **A live web demo** for real-time Balti speech transcription

---

## 🏆 Results

| Model | WER ↓ | Dataset | Steps |
|---|---|---|---|
| Whisper-small (zero-shot) | ~95%+ | BaltiVoice | — |
| **Whisper-small (fine-tuned)** | **30.07%** | **BaltiVoice** | **1000** |

Training curve:

| Step | Training Loss | Validation Loss | WER |
|---|---|---|---|
| 250 | 0.7905 | 0.4037 | 40.19% |
| 500 | 0.5968 | 0.3208 | 33.37% |
| 750 | 0.4542 | 0.2963 | 31.37% |
| **1000** | **0.4652** | **0.2830** | **30.07%** |

---

## 📦 Dataset

**[mohdali1/baltivoice-asr](https://huggingface.co/datasets/mohdali1/baltivoice-asr)**

| Property | Value |
|---|---|
| Language | Balti (bft) |
| Script | Nastaliq (Arabic-based) |
| Total clips | 10,060 |
| Total duration | ~16.8 hours |
| Avg clip length | ~6 seconds |
| Format | 16kHz mono WAV |
| Train split | 9,051 samples |
| Validation split | 1,006 samples |

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/mohdali1/BaltiVoice-ASR.git
cd BaltiVoice-ASR
pip install -r requirements.txt
```

### Transcribe Audio

```python
from transformers import pipeline

asr = pipeline(
    "automatic-speech-recognition",
    model="mohdali1/whisper-small-balti",
    generate_kwargs={"language": "urdu", "task": "transcribe"}
)

result = asr("your_audio.wav")
print(result["text"])
# Output: بوا لہ سلام بے اِنپا سلام سہ مہ بیاس
```

### Use the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("mohdali1/baltivoice-asr")
print(dataset)
# DatasetDict({
#     train: Dataset({features: ['audio', 'sentence'], num_rows: 9051})
#     validation: Dataset({features: ['audio', 'sentence'], num_rows: 1006})
# })
```

---

## 🏗️ Project Structure

```
BaltiVoice-ASR/
├── src/
│   ├── data_audit.py          # Dataset loading and analysis
│   ├── preprocess.py          # Audio preprocessing pipeline
│   ├── train.py               # Whisper fine-tuning script
│   └── evaluate.py            # WER evaluation script
├── notebooks/
│   └── BaltiVoice.ipynb       # Full training notebook (Colab-ready)
├── scripts/
│   └── run_training.sh        # One-command training script
├── app.py                     # Gradio demo (HuggingFace Spaces)
├── requirements.txt
└── README.md
```

---

## 🔧 Training

### Requirements
- Google Colab (free T4 GPU) or any CUDA-enabled GPU
- HuggingFace account with write token
- ~2 hours training time

### Run Training

```python
# Full training script — see notebooks/BaltiVoice.ipynb
python src/train.py \
    --model_name openai/whisper-small \
    --dataset mohdali1/baltivoice-asr \
    --output_dir ./whisper-balti \
    --max_steps 1000 \
    --learning_rate 1e-5
```

### Key Training Config

```python
Seq2SeqTrainingArguments(
    per_device_train_batch_size = 8,
    gradient_accumulation_steps = 2,
    learning_rate               = 1e-5,
    warmup_steps                = 100,
    max_steps                   = 1000,
    gradient_checkpointing      = True,
    fp16                        = True,
)
```

---

## 🌐 Live Demo

Try the live demo at **[huggingface.co/spaces/mohdali1/baltivoice-demo](https://huggingface.co/spaces/mohdali1/baltivoice-demo)**

- 🎤 Record directly from your microphone
- 📁 Upload a WAV/MP3 file
- 📝 Get transcription in native Balti script instantly

---

## 🗺️ Roadmap

- [x] Dataset collection and validation
- [x] Whisper-small fine-tuning (WER: 30%)
- [x] Live Gradio demo deployment
- [ ] Extended training to 2000 steps (target WER: ~24%)
- [ ] Text normalisation for improved accuracy
- [ ] Whisper-medium fine-tuning
- [ ] arXiv paper submission
- [ ] Mozilla Common Voice Balti contribution

---

## 📚 Citation

If you use this dataset or model in your research, please cite:

```bibtex
@misc{baltivoice2025,
  author    = {Mohammad Ali},
  title     = {BaltiVoice: First ASR Dataset and Model for Balti Language},
  year      = {2025},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/datasets/mohdali1/baltivoice-asr}
}
```

---

## 🤝 Contributing

Contributions welcome! If you speak Balti and want to help improve the dataset or model accuracy, please open an issue or pull request.

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ❤️ for Balti language preservation**

[HuggingFace](https://huggingface.co/mohdali1) · [Dataset](https://huggingface.co/datasets/mohdali1/baltivoice-asr) · [Model](https://huggingface.co/mohdali1/whisper-small-balti) · [Demo](https://huggingface.co/spaces/mohdali1/baltivoice-demo)

</div>
