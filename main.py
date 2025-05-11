from app.fetcher import NewsFetcher
from app.sentiment import SentimentAnalyzer
from app.article import Article
from app.reporter import ReportGenerator
import datetime
import fire

def main(keyword: str, time_frame: str, articles_count: int = 100, export_to_csv: bool = False): 
    """
    Run the News Sentiment Analyzer for a single keyword.

    :param keyword: The topic to search for.
    :param time_frame: The time frame for the search ('day', 'week', or 'month').
    :param articles_count: The number of articles to fetch.
    :param export_to_csv: Whether to export the results to a CSV file (default is False).
    """

    analyzer = SentimentAnalyzer()
    fetcher = NewsFetcher(analyzer)
    reporter = ReportGenerator(analyzer)

    print(f"\nAnalyzing sentiment for keyword: {keyword}")
    articles = fetcher.fetch_articles(keyword, time_frame, articles_count)
    if not articles:
        return
    
    # Generate sentiment summary
    reporter.generate_sentiment_summary(articles)

    # Generate and display the sentiment chart
    fig = reporter.generate_sentiment_over_time_chart(articles)
    fig.show()

    # Export to CSV if requested
    if export_to_csv:
        reporter.export_sentiment_analysis(articles, keyword)


if __name__ == "__main__":
    fire.Fire(main)
