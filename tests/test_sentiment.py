"""
# News Sentiment Analyzer
# This script fetches news articles based on a keyword, analyzes their sentiment,
# and generates a report with visualizations."""
import unittest
from app.sentiment import SentimentAnalyzer
from app.article import Article

class TestSentimentAnalyzer(unittest.TestCase):
    """
    Unit tests for the SentimentAnalyzer class.
    """
    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_analyze(self):
        """
        Test the analyze method of SentimentAnalyzer.
        """
        article = Article(
            title="Positive news",
            description="This is great!",
            content="Everything is awesome.",
            published_at="2025-05-10"
        )
        self.analyzer.analyze(article)
        self.assertGreater(article.sentiment, 0)  # Positive sentiment expected
    
    def test_analyze_negative(self):
        """
        Test the analyze method of SentimentAnalyzer for negative sentiment.
        """
        article = Article(
            title="Negative news",
            description="This is bad!",
            content="Everything is terrible.",
            published_at="2025-05-10"
        )
        self.analyzer.analyze(article)
        self.assertLess(article.sentiment, 0)  # Negative sentiment expected

if __name__ == "__main__":
    unittest.main()