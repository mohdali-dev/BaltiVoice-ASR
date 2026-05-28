
<div align="center">

# 🤝 Contributing to BaltiVoice ASR

**Thank you for your interest in contributing to the first open-source ASR project for the Balti language!** 🎙️

Whether you are a **Balti speaker**, a **Machine Learning Engineer**, or a **Linguist**, your contribution helps preserve and digitize this critically low-resource language.

[![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Contributor%20Covenant-blue?style=flat-square)](CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

---

## 📋 Table of Contents

1. [🌟 How Can I Contribute?](#-how-can-i-contribute)
2. [🐛 Reporting Bugs & Issues](#-reporting-bugs--issues)
3. [💡 Suggesting Enhancements](#-suggesting-enhancements)
4. [ Development Setup](#-development-setup)
5. [📝 Code Style Guidelines](#-code-style-guidelines)
6. [🗣️ For Native Balti Speakers](#-for-native-balti-speakers)
7. [🚀 Pull Request Process](#-pull-request-process)
8. [ Code of Conduct](#-code-of-conduct)

---

## 🌟 How Can I Contribute?

We welcome contributions in several areas:

| Role | Tasks | Skills Needed |
|------|-------|---------------|
| **🗣️ Linguist / Speaker** | Validate transcriptions, record new audio clips, flag cultural errors | Native/Fluent Balti |
| **🤖 ML Engineer** | Improve model architecture, optimize training, add data augmentation | Python, PyTorch, HuggingFace |
| **🛠️ Developer** | Build web demos, fix bugs, improve documentation, write tests | JavaScript, Python, Git |
| **📚 Researcher** | Analyze error cases, write papers, compare with other low-resource models | NLP, Linguistics, Academic Writing |

---

## 🐛 Reporting Bugs & Issues

Found a bug? Please help us fix it!

### Before You Report
1. Check the **[Issues Tab](https://github.com/mohdali-dev/baltivoice-asr/issues)** to see if it’s already reported.
2. Try to reproduce the bug with the latest version of the code.

### How to Submit a Bug Report
Click **[New Issue](https://github.com/mohdali-dev/baltivoice-asr/issues/new)** and include:
- **Description**: What happened vs. what you expected.
- **Steps to Reproduce**: Exact commands or code snippets.
- **Environment**: OS, Python version, GPU/CPU info.
- **Audio Sample** (if applicable): A small `.wav` file that triggers the error.
- **Error Logs**: Copy-paste the full traceback.

> 💡 *Tip: Use the "Bug Report" template if available.*

---

##  Suggesting Enhancements

Have an idea to make BaltiVoice better?

### Examples of Enhancements
- Adding support for Romanized Balti script.
- Implementing speaker adaptation techniques.
- Creating a mobile-friendly demo interface.
- Adding unit tests for the preprocessing pipeline.

### How to Submit
1. Open a **[New Issue](https://github.com/mohdali-dev/baltivoice-asr/issues/new)** labeled `enhancement`.
2. Clearly describe the feature and why it’s useful.
3. If possible, sketch out how you’d implement it.

---

## 🔧 Development Setup

Ready to code? Here’s how to get started locally.

### 1. Fork & Clone
```bash
# Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/baltivoice-asr.git
cd baltivoice-asr
```

### 2. Install Dependencies
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
pip install -e .  # If setup.py exists
```

### 3. Run Tests
```bash
# Run existing tests (if any)
pytest tests/

# Or run a quick inference check
python src/inference_check.py --audio samples/test_balti.wav
```

### 4. Make Your Changes
- Create a new branch: `git checkout -b feat/your-feature-name`
- Write clean, documented code.
- Add tests if applicable.

---

## 📝 Code Style Guidelines

We follow standard Python best practices to keep the codebase maintainable.

### Python Style
- Follow **[PEP 8](https://peps.python.org/pep-0008/)** guidelines.
- Use **[Black](https://black.readthedocs.io/)** for formatting:
  ```bash
  black src/ tests/ app.py
  ```
- Use **[Flake8](https://flake8.pycqa.org/)** for linting:
  ```bash
  flake8 src/ tests/ app.py
  ```
- Use type hints where possible (`def func(x: int) -> str:`).
- Write docstrings for all functions/classes (Google style preferred).

### Commit Messages
Use clear, imperative commit messages:
- ✅ `feat: add romanized balti support`
- ✅ `fix: correct audio sampling rate in preprocess.py`
- ❌ `fixed stuff`
- ❌ `update`

### Branch Naming
- `feat/feature-name` (new features)
- `fix/bug-description` (bug fixes)
- `docs/update-readme` (documentation)
- `refactor/clean-code` (code improvements)

---

## 🗣️ For Native Balti Speakers

Your voice matters! Here’s how you can help without coding:

### 1. Validate Transcriptions
- Listen to audio clips in the **[Dataset](https://huggingface.co/datasets/mohdali1/baltivoice-asr)**.
- Check if the text matches the speech accurately.
- Flag issues like:
  - Wrong words
  - Missing punctuation
  - Dialect variations not captured

### 2. Record New Data
- We need more diverse speakers (different ages, genders, regions).
- Record 5–10 second clips in quiet environments.
- Submit via Google Form *(link coming soon)* or email `alisdkse@gmail.com`.

### 3. Cultural Context
- Help us understand idioms, loanwords, or code-switching (Balti + Urdu/English).
- Review model outputs for cultural sensitivity.

---

## 🚀 Pull Request Process

1. **Fork** the repository.
2. **Create** a feature branch (`git checkout -b feat/my-feature`).
3. **Commit** your changes (`git commit -m 'feat: add my feature'`).
4. **Push** to your fork (`git push origin feat/my-feature`).
5. **Open** a Pull Request against the `main` branch.

### PR Checklist
- [ ] My code follows the style guidelines.
- [ ] I have added tests that prove my fix/feature works.
- [ ] All existing tests pass.
- [ ] I have updated the documentation (README/docs).
- [ ] I have linked the relevant issue (e.g., `Closes #123`).

### Review Process
- Maintainers will review your PR within **3–5 days**.
- Be open to feedback and requested changes.
- Once approved, your PR will be merged! 

---

## 📜 Code of Conduct

We are committed to providing a friendly, safe, and welcoming environment for all contributors.

Please read our **[Code of Conduct](CODE_OF_CONDUCT.md)** before participating.

In short:
- Be respectful.
- No harassment or discrimination.
- Welcome newcomers.
- Focus on constructive criticism.

---

##  Thank You!

Every contribution, no matter how small, helps bring Balti into the digital age.

**Questions?**
- Open an issue.
- Email: `alisdkse@gmail.com`
- LinkedIn: https://linkedin.com/in/mohdali1

<div align="center">

*Built with ❤️ by the BaltiVoice Community*

[![GitHub Stars](https://img.shields.io/github/stars/mohdali-dev/baltivoice-asr?style=social)](https://github.com/mohdali-dev/baltivoice-asr)
[![GitHub Forks](https://img.shields.io/github/forks/mohdali-dev/baltivoice-asr?style=social)](https://github.com/mohdali-dev/baltivoice-asr)

</div>
```
