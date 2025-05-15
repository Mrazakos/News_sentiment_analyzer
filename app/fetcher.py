"""
# News Sentiment Analyzer
# This script fetches news articles based on a keyword, analyzes their sentiment,
# and generates a report with visualizations.
# """
import os
import time
import datetime
import requests
from dotenv import load_dotenv

from app.article import Article
from app.sentiment import SentimentAnalyzer

load_dotenv()

class NewsFetcher:
    """
    Class to fetch news articles from the News API based on a keyword and time frame.
    It uses the News API to retrieve articles and analyze their sentiment.
    """
    def __init__(self, analyzer: SentimentAnalyzer):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"
        self.analyzer = analyzer

    def fetch_articles(self, keyword:str, time_frame:str, max_articles: int=100):
        """
        Fetch articles from the News API based on a keyword and time frame.
        :param keyword: The topic to search for.
        :param time_frame: The time frame for the search ('day', 'week', or 'month').
        :param max_articles: The maximum number of articles to fetch.
        :return: A list of Article objects.
        """
        all_articles = []
        page = 1
        page_size = 100  # Maximum number of articles per page

        # Calculate the from_date based on the time frame
        today = datetime.datetime.now()
        if time_frame == "day":
            from_date = today - datetime.timedelta(days=1)
        elif time_frame == "week":
            from_date = today - datetime.timedelta(weeks=1)
        elif time_frame == "month":
            from_date = today - datetime.timedelta(days=30)
        else:
            print("Invalid time frame. Please enter 'day', 'week', or 'month'.")
            return []

        from_date = from_date.strftime("%Y-%m-%dT%H:%M:%S")
        while len(all_articles) < max_articles and page * page_size <= max_articles:
            if max_articles - len(all_articles) < page_size:
                page_size = max_articles - len(all_articles)
            params = {
                "q": keyword,
                "language": "en",
                "sortBy": "relevancy",
                "pageSize": page_size,
                "page": page,
                "from": from_date,
                "apiKey": self.api_key,
            }

            response = requests.get(self.base_url, params=params, timeout=10)
            data = response.json()

            if response.status_code != 200:
                print("Error:", response.status_code, data.get("message", "Unknown error"))
                break

            articles = data.get("articles", [])
            if not articles:
                break  # No more results

            all_articles.extend(articles)

            page += 1
            time.sleep(1)

        if not all_articles:
            print(f"No articles found for keyword '{keyword}' in the given time frame '{time_frame}'.")
            return []

        articles = []
        for item in all_articles:
            if "publishedAt" in item:
                item["publishedAt"] = datetime.datetime.strptime(item["publishedAt"],
                        "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
            article = Article(
                title=item.get("title", ""),
                description=item.get("description", ""),
                content=item.get("content", ""),
                published_at=item.get("publishedAt", ""),
                link=item.get("url", "")
            )
            self.analyzer.analyze(article)
            articles.append(article)
        return articles
