"""
# News Sentiment Analyzer
# This script fetches news articles based on a keyword, analyzes their sentiment,
# and generates a report with visualizations."""
from  textblob import TextBlob

from app.article import Article

class SentimentAnalyzer:
    """
    A class to analyze the sentiment of news articles using TextBlob.
    """
    def analyze(self, article: Article) -> float:
        """
        Analyze the sentiment of a news article.
        :param article: The article object containing title, description, and content.
        """
        text = article.title + " " + (article.description or "") + " " + (article.content or "")
        polarity = TextBlob(text).sentiment.polarity
        article.sentiment = polarity
        return polarity
