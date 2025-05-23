# 🔍 Google Search Sentiment Analyzer

This Python tool lets you search Google, analyze the sentiment of the results using a Hugging Face transformer model, and filter results based on high-confidence scores. It’s ideal for gauging public sentiment on any topic using real-time web content.

---

## 1. 🚀 Features

- 🌐 Fetches Google search results using the Custom Search API  
- 🤖 Analyzes sentiment using `distilbert-base-uncased-finetuned-sst-2-english`  
- 📈 Filters for high-confidence results (score > 0.9)  
- 📝 Saves results to a local `sentiment_results.txt` file  

---

## 2. 🛠️ Setup Instructions

### 2.1 Clone the Repository

```bash
git clone https://github.com/yourusername/google-search-sentiment-analyzer.git
cd google-search-sentiment-analyzer
```

### 2.2 Install Dependencies

Make sure Python 3.7+ is installed, then run:

```bash
pip install -r requirements.txt
```

### 2.3 Add API Credentials

Open `sentiment_search.py` and replace the placeholders with your own:

```python
api_key = "YOUR_GOOGLE_API_KEY"
cx = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
```

To get these:
- 📘 [Google Custom Search setup guide](https://developers.google.com/custom-search/v1/introduction)

---

## 3. ▶️ Usage

```bash
python sentiment_search.py
```

Enter your search query when prompted. The script will:

- Fetch Google results  
- Analyze each snippet and title for sentiment  
- Filter and display results with confidence > 0.9  
- Save them in `sentiment_results.txt`  

---

## 4. 🧪 Example Output

```
Text: Tesla AI day stuns investors - Learn what happened
Sentiment: POSITIVE (Score: 0.97)
Source: https://example.com/article123
--------------------------------------------------------------------------------
```

---

## 5. 📦 Requirements

- Python 3.7+  
- `transformers`  
- `requests`  

Install them with:

```bash
pip install transformers requests
```

---

## 6. 📁 Project Structure

```
google-search-sentiment-analyzer/
├── sentiment_search.py       # Main script
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── .gitignore                # Python cache and env exclusions
```

---

## 7. 🛡️ License

MIT License — free to use, modify, and distribute.

---

## 8. ✨ Acknowledgments

- 🤗 [Hugging Face Transformers](https://huggingface.co/transformers/)
- 🔍 [Google Custom Search API](https://developers.google.com/custom-search)

---

> Built with Python, curiosity, and AI 🔧🧠
