"""
# News Sentiment Analyzer
# This script fetches news articles based on a keyword, analyzes their sentiment,
# and generates a report with visualizations.
"""
import unittest
from app.article import Article

class TestArticle(unittest.TestCase):
    """
    Unit tests for the Article class.
    """
    def test_article_initialization(self):
        """
        Test the initialization of the Article class.
        """
        article = Article(
            title="Test Title",
            description="Test Description",
            content="Test Content",
            published_at="2025-05-10",
            sentiment=0.5
        )
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.sentiment, 0.5)

if __name__ == "__main__":
    unittest.main()