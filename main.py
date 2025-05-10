from app.fetcher import NewsFetcher
from app.sentiment import SentimentAnalyzer
from app.article import Article
from app.reporter import ReportGenerator
import datetime
import fire

def main(keyword: str, time_frame: str, articles_count: int = 100): 
    """
    Run the News Sentiment Analyzer.

    :param keyword: The topic to search for.
    :param time_frame: The time frame for the search ('day', 'week', or 'month').
    :param articles_count: The number of articles to fetch (default and max is 100).
    """

    analyzer = SentimentAnalyzer()
    fetcher = NewsFetcher(analyzer)
    reporter = ReportGenerator(analyzer)

    articles = fetcher.fetch_articles(keyword, time_frame, articles_count)
    
    # Generate sentiment summary
    reporter.generate_sentiment_summary(articles)

    # Generate and display the sentiment chart
    fig = reporter.generate_sentiment_over_time_chart(articles)
    fig.show()

if __name__ == "__main__":
    fire.Fire(main)
