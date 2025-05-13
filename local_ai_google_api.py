import requests
from transformers import pipeline

# Step 1: Google Custom Search API
def fetch_google_search_results(api_key, cx, query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    results = response.json()
    return results.get("items", [])

# Step 2: Local AI Model for Sentiment Analysis
def analyze_sentiment(texts):
    # Load a pre-trained sentiment analysis model
    sentiment_analyzer = pipeline("sentiment-analysis")
    results = []
    for text in texts:
        analysis = sentiment_analyzer(text)
        results.append({"text": text, "sentiment": analysis[0]["label"], "score": analysis[0]["score"]})
    return results

# Main Function
if __name__ == "__main__":
    # Google API credentials
    api_key = "AIzaSyDdHk-39CJzp3L0bFoJmW2VBSOUfaZy-4M"  # Replace with your Google API key
    cx = "c77b81e227c5d4cae"  # Replace with your Custom Search Engine ID

    # Search query
    query = "Artificial Intelligence in healthcare"
    print(f"Fetching Google search results for query: '{query}'...\n")

    # Fetch search results
    search_results = fetch_google_search_results(api_key, cx, query)

    # Extract titles and snippets for sentiment analysis
    texts_to_analyze = [item["title"] + " - " + item.get("snippet", "") for item in search_results]

    # Analyze sentiment using the local AI model
    print("Analyzing sentiment of search results...\n")
    sentiment_results = analyze_sentiment(texts_to_analyze)

    # Print results
    for result in sentiment_results:
        print(f"Text: {result['text']}")
        print(f"Sentiment: {result['sentiment']} (Score: {result['score']:.2f})")
        print("-" * 80)