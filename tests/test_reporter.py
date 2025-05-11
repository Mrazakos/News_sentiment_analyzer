import unittest
from app.reporter import ReportGenerator
from unittest.mock import MagicMock

class MockArticle:
    def __init__(self, title, sentiment, link):
        self.title = title
        self.sentiment = sentiment
        self.link = link

    @property
    def sentiment_emoji(self):
        if self.sentiment > 0.1:
            return "🟢"
        elif self.sentiment < -0.1:
            return "🔴"
        else:
            return "🟡"
class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.mock_analyzer = MagicMock()
        self.reporter = ReportGenerator(self.mock_analyzer)

        self.articles = [
            MockArticle("Positive Article", 0.9, "2025-05-01"),
            MockArticle("Neutral Article", 0.0, "2025-05-02"),
            MockArticle("Negative Article", -0.9, "2025-05-03"),
        ]

    def test_generate_sentiment_summary(self):
        self.reporter.generate_sentiment_summary(self.articles)
        # Add assertions for printed output if needed

if __name__ == "__main__":
    unittest.main()