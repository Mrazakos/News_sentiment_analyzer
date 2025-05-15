import unittest
from unittest.mock import patch, MagicMock
from app.fetcher import NewsFetcher
from app.sentiment import SentimentAnalyzer

class TestNewsFetcher(unittest.TestCase):
    """
    Unit tests for the NewsFetcher class.
    """
    @patch("app.fetcher.requests.get") 
    def test_fetch_articles_success(self, mock_get):
        """
        Test the successful fetching of articles from the News API.
        """
        # Mock SentimentAnalyzer
        mock_analyzer = SentimentAnalyzer()
        mock_analyzer.analyze = MagicMock()  # prevent it from doing real work

        # Instance of NewsFetcher with mock analyzer
        fetcher = NewsFetcher(mock_analyzer)
        fetcher.api_key = "fake_api_key"

        # Mock API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "articles": [
                {
                    "title": "Test Article",
                    "description": "Test Description",
                    "content": "Test Content",
                    "publishedAt": "2025-05-10T12:00:00Z",
                    "url": "http://example.com/test-article"
                }
            ]
        }
        mock_get.return_value = mock_response

        articles = fetcher.fetch_articles("test", "day")

        self.assertTrue(mock_get.called, "requests.get was not called!")
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, "Test Article")
        self.assertEqual(articles[0].link, "http://example.com/test-article")
        
        
    @patch("app.fetcher.requests.get")
    def test_fetch_articles_no_results(self, mock_get):
        """
        Test the case where no articles are found.
        """
        mock_analyzer = SentimentAnalyzer()
        fetcher = NewsFetcher(mock_analyzer)

        # Mock API response with no articles
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"articles": []}
        mock_get.return_value = mock_response

        articles = fetcher.fetch_articles("nonexistentkeyword", "day")
        self.assertEqual(len(articles), 0)  # No articles should be returned

    @patch("app.fetcher.requests.get")
    def test_fetch_articles_api_error(self, mock_get):
        """
        Test the case where the API returns an error.
        """
        mock_analyzer = SentimentAnalyzer()
        fetcher = NewsFetcher(mock_analyzer)

        # Mock API response with an error
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"message": "Internal Server Error"}
        mock_get.return_value = mock_response

        articles = fetcher.fetch_articles("test", "day")
        self.assertEqual(len(articles), 0)  # No articles should be returned

if __name__ == "__main__":
    unittest.main()