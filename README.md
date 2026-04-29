# Spell Checking for Python

A lightweight **Python spell-checking library** — because spelling is hard. Built on top of proven NLP techniques to detect and correct misspellings in text.

## ✨ Features

- 🔍 Detect misspelled words in any string
- ✅ Suggest correct spellings
- ⚡ Fast and lightweight
- 🐍 Easy to integrate into any Python project
- 📦 Minimal dependencies

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## ⚙️ Requirements

- Python >= 3.6

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/hamdyelbatal122/Spell-Checking-for-Python.git
   cd Spell-Checking-for-Python
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the spell checker**
   ```bash
   python spell_check.py
   ```

## 🧪 Usage Example

```python
from spell_checker import check

result = check("Ths is a speling mstake")
print(result)
# Output: "This is a spelling mistake"
```

## 📁 Project Structure

```
Spell-Checking-for-Python/
├── spell_check.py
├── requirements.txt
└── README.md
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
