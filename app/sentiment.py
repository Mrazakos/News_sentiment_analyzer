from  textblob import TextBlob

class SentimentAnalyzer:
  def analyze(self, article: str) -> float:
    text = article.title + " " + (article.description or "") + " " + (article.content or "")
    polarity = TextBlob(text).sentiment.polarity
    article.sentiment = polarity
    return polarity
  
  def get_sentiment_over_time(self, articles: list) -> list:
        """
        Get sentiment scores over time for a list of articles.
        :param articles: List of article objects with 'date', 'title', and 'description'
        :return: List of sentiment scores and dates
        """
        sentiment_data = []
      
        for article in articles:
            polarity = self.analyze(article)
            sentiment_data.append({
                'date': article.published_at, 
                'sentiment': polarity,
                'title': article.title,
            })
        
        return sentiment_data
