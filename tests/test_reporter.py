"""
# News Sentiment Analyzer
# This script fetches news articles based on a keyword, analyzes their sentiment,
# and generates a report with visualizations."""
import unittest
from unittest.mock import MagicMock
from app.reporter import ReportGenerator
import io
import sys


class MockArticle:
    """
    Mock class to simulate the behavior of the Article class.
    """
    def __init__(self, title, sentiment, link):
        self.title = title
        self.sentiment = sentiment
        self.link = link

    @property
    def sentiment_emoji(self):
        """
        Determine the emoji based on the sentiment score.
        :return: Emoji representing the sentiment
        """
        if self.sentiment > 0.1:
            return "🟢"
        elif self.sentiment < -0.1:
            return "🔴"
        else:
            return "🟡"
class TestReportGenerator(unittest.TestCase):
    """
    Unit tests for the ReportGenerator class.
    """
    def setUp(self):
        self.mock_analyzer = MagicMock()
        self.reporter = ReportGenerator(self.mock_analyzer)

        self.articles = [
            MockArticle("Positive Article", 0.9, "2025-05-01"),
            MockArticle("Neutral Article", 0.0, "2025-05-02"),
            MockArticle("Negative Article", -0.9, "2025-05-03"),
        ]


    def test_generate_sentiment_summary_prints_expected_output(self):
        """
        Test that generate_sentiment_summary prints the expected output.
        """
        # Capture stdout
        captured_output = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            self.reporter.generate_sentiment_summary(self.articles)
        finally:
            sys.stdout = sys_stdout

        output = captured_output.getvalue()
            # Check for expected substrings in the output
        self.assertIn("Most Positive Articles:", output)
        self.assertIn("Least Positive Articles:", output)
        self.assertIn("Most Neutral Articles:", output)
        self.assertIn("Positive Article", output)
        self.assertIn("Neutral Article", output)
        self.assertIn("Negative Article", output)


if __name__ == "__main__":
    unittest.main()