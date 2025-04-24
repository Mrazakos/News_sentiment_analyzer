import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NewsFetcher:
  def __init__(self):
    self.api_key = os.getenv("NEWS_API_KEY")
    self.base_url = "https://newsapi.org/v2/everything"

  def fetch_articles(self, keyword, page_size=10, from_date="2025-04-24"):
    params = {
        "q": keyword,
        "language": "en",
        "sortBy": "popularity",
        "pageSize": page_size,
        "from": from_date,
        "apiKey": self.api_key,

    }
    response = requests.get(self.base_url, params=params)
    data = response.json()
    return data.get("articles", [])
