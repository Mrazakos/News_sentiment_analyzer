import unittest
from unittest.mock import patch, MagicMock
from app.fetcher import NewsFetcher
from app.sentiment import SentimentAnalyzer

class TestNewsFetcher(unittest.TestCase):
    @patch("app.fetcher.requests.get")
    def test_fetch_articles(self, mock_get):
        mock_analyzer = SentimentAnalyzer()
        fetcher = NewsFetcher(mock_analyzer)

        # Mock API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "articles": [
                {"title": "Test Article", "description": "Test", "content": "Test Content", "publishedAt": "2025-05-10T12:00:00Z"}
            ]
        }
        mock_get.return_value = mock_response

        articles = fetcher.fetch_articles("test", "day", 1)
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, "Test Article")

if __name__ == "__main__":
    unittest.main()