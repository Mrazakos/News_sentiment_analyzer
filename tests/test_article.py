import unittest
from app.article import Article

class TestArticle(unittest.TestCase):
    def test_article_initialization(self):
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