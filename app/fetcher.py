import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

class NewsFetcher:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_articles(self, keyword, from_date="2025-04-24", max_articles=100):
        all_articles = []
        page = 1
        page_size = 100  # Maximum number of articles per page

        while len(all_articles) < max_articles:
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

            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code != 200:
                print("Error:", response.status_code, data.get("message", "Unknown error"))
                break

            articles = data.get("articles", [])
            if not articles:
                break  # No more results

            all_articles.extend(articles)

            page += 1
            time.sleep(1)  # Be nice to the API

        return all_articles
