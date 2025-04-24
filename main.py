from app.fetcher import NewsFetcher
from app.sentiment import SentimentAnalyzer
from app.article import Article
from app.reporter import ReportGenerator

def main():
    keyword = input("Enter a topic to search: ")
    fetcher = NewsFetcher()
    analyzer = SentimentAnalyzer()
    reporter = ReportGenerator(analyzer)

    raw_articles = fetcher.fetch_articles(keyword, 100, "2025-04-15")
    articles = []

    for item in raw_articles:
        article = Article(
            title=item.get("title", ""),
            description=item.get("description", ""),
            content=item.get("content", ""),
            published_at=item.get("publishedAt", "")
        )
        analyzer.analyze(article)
        articles.append(article)

    fig = reporter.generate_sentiment_over_time_chart(articles)
    fig.show()

if __name__ == "__main__":
    main()
