"""
# News Sentiment Analyzer
# This script fetches news articles based on a keyword, analyzes their sentiment,
# and generates a report with visualizations.
"""
import fire
from app.fetcher import NewsFetcher
from app.sentiment import SentimentAnalyzer
from app.reporter import ReportGenerator

def run(keyword: str, time_frame: str, articles_count: int = 100, export_to_csv: bool = False): 
    """
    Run the News Sentiment Analyzer for a single keyword.
    """
    analyzer = SentimentAnalyzer()
    fetcher = NewsFetcher(analyzer)
    reporter = ReportGenerator(analyzer)

    print(f"\nAnalyzing sentiment for keyword: {keyword}")
    articles = fetcher.fetch_articles(keyword, time_frame, articles_count)
    if not articles:
        return

    reporter.generate_sentiment_summary(articles)
    fig = reporter.generate_sentiment_over_time_chart(articles)
    fig.show()

    if export_to_csv:
        reporter.export_sentiment_analysis(articles, keyword)

# 🔧 New entry point function
def main():
    """
    Main entry point for the script.
    """
    fire.Fire(run)

if __name__ == "__main__":
    main()
