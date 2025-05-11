from  textblob import TextBlob

class SentimentAnalyzer:
  def analyze(self, article: str) -> float:
    text = article.title + " " + (article.description or "") + " " + (article.content or "")
    polarity = TextBlob(text).sentiment.polarity
    article.sentiment = polarity
    return polarity
  
