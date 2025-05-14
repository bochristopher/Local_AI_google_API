import requests
from transformers import pipeline

# Step 1: Google Custom Search API
def fetch_google_search_results(api_key, cx, query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    results = response.json()
    return [{"title": item["title"], "snippet": item.get("snippet", ""), "link": item.get("link", "")} for item in results.get("items", [])]

# Step 2: Local AI Model for Sentiment Analysis
def analyze_sentiment(search_results):
    """
    Analyze the sentiment of search results using a pre-trained Hugging Face model.

    :param search_results: List of dictionaries containing 'title', 'snippet', and 'link'
    :return: List of dictionaries with 'text', 'sentiment', 'score', and 'link'
    """
    # Load a pre-trained sentiment analysis model
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    results = []
    for item in search_results:
        text = item["title"] + " - " + item.get("snippet", "")
        analysis = sentiment_analyzer(text)
        results.append({
            "text": text,
            "sentiment": analysis[0]["label"],
            "score": analysis[0]["score"],
            "link": item.get("link", "No link available")  # Include the link
        })
    return results

# Main Function
if __name__ == "__main__":
    # Google API credentials
    api_key = "AIzaSyDdHk-39CJzp3L0bFoJmW2VBSOUfaZy-4M"  # Replace with your Google API key
    cx = "c77b81e227c5d4cae"  # Replace with your Custom Search Engine ID

    # Search query
    query = input("Enter your search query: ")
    print(f"Fetching Google search results for query: '{query}'...\n")

    # Fetch search results
    search_results = fetch_google_search_results(api_key, cx, query)

    # Analyze sentiment using the local AI model
    print("Analyzing sentiment of search results...\n")
    sentiment_results = analyze_sentiment(search_results)

    # Filter results with a score greater than 0.9
    filtered_results = [result for result in sentiment_results if result['score'] > 0.9]

    # Print results
    for result in filtered_results:
        print(f"Text: {result['text']}")
        print(f"Sentiment: {result['sentiment']} (Score: {result['score']:.2f})")
        print(f"Source: {result['link']}")
        print("-" * 80)

    # Save results to a file
    with open("sentiment_results.txt", "w") as file:
        for result in filtered_results:
            file.write(f"Text: {result['text']}\n")
            file.write(f"Sentiment: {result['sentiment']} (Score: {result['score']:.2f})\n")
            file.write(f"Source: {result['link']}\n")
            file.write("-" * 80 + "\n")

