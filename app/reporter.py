"""
reporter.py
This module contains the ReportGenerator class,
which is responsible for generating reports and visualizations
for sentiment analysis.

It includes methods to create sentiment over time charts,
generate sentiment summaries, and export the analysis
to CSV files."""
import csv
import datetime
import plotly.graph_objects as go
import pandas as pd


class ReportGenerator:
    """
    Class to generate reports and visualizations for sentiment analysis.
    """
    def __init__(self, sentiment_analyzer):
        self.sentiment_analyzer = sentiment_analyzer

    def generate_sentiment_over_time_chart(self, articles: list):
        """
        Generate a sentiment over time chart for a list of articles.
        :param articles: List of article objects with 'date', 'title', and 'description'
        :return: Plotly Figure (interactive chart)
        """
        # Prepare data for the chart
        sentiment_data = []
        for article in articles:
            sentiment_data.append({
                'date': article.published_at,
                'sentiment': article.sentiment,
                'title': article.title,
                'link': article.link
            })

        # Convert data into DataFrame
        df = pd.DataFrame(sentiment_data)
        df['date'] = pd.to_datetime(df['date'])
        df.sort_values(by='date', inplace=True)

        # Calculate moving average
        df['moving_avg'] = df['sentiment'].rolling(window=15, min_periods=1).mean()

        # Create the Plotly chart
        fig = go.Figure()

        # Add sentiment data points
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['sentiment'],
            mode='markers+lines',
            name='Sentiment',
            text=df['title'],
            customdata=df['link'],
            hovertemplate="<b>%{text}</b><br>Sentiment: %{y}<br>Date: %{x}<br><extra></extra>"
        ))

        # Add moving average line
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['moving_avg'],
            mode='lines',
            name='Moving Average',
            line=dict(dash='dash')
        ))

        # Customize layout
        fig.update_layout(
            title="Sentiment Over Time",
            xaxis_title="Date",
            yaxis_title="Sentiment Score",
            template="plotly_dark",
        )
        return fig

    def generate_sentiment_summary(self, articles: list):
        """
        Generate and display a sentiment summary for the articles.
        :param articles: List of Article objects
        """
        # Sort articles by sentiment
        articles.sort(key=lambda x: x.sentiment)

        # Extract subsets
        most_positive = articles[-3:]  # Last 3 articles (highest sentiment)
        least_positive = articles[:3]  # First 3 articles (lowest sentiment)
        most_neutral = sorted(articles, key=lambda x: abs(x.sentiment))[:3]  # Closest to 0

        # Display the results
        print("\nMost Positive Articles:")
        for article in most_positive:
            print(f"Title: {article.title}, Sentiment: {round(article.sentiment, 2)}, Emoji: {article.sentiment_emoji}, Link: {article.link}")

        print("\nLeast Positive Articles:")
        for article in least_positive:
            print(f"Title: {article.title}, Sentiment: {round(article.sentiment, 2)}, Emoji: {article.sentiment_emoji}, Link: {article.link}")

        print("\nMost Neutral Articles:")
        for article in most_neutral:
            print(f"Title: {article.title}, Sentiment: {round(article.sentiment, 2)}, Emoji: {article.sentiment_emoji}, Link: {article.link}")

    def export_sentiment_analysis(self, articles: list, keyword: str):
        """
        Export the sentiment analysis and all articles to a CSV file.
        :param articles: List of Article objects
        :param keyword: The keyword used for analysis (used in the filename)
        """
        # Generate a timestamped filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sentiment_{keyword.replace(' ', '_')}_{timestamp}.csv"

        # Sort articles by sentiment
        articles.sort(key=lambda x: x.sentiment)

        # Write to CSV
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow(["Title", "Sentiment", "Link", "Sentiment Emoji"])
            for article in articles:
                writer.writerow([
                    article.title,
                    round(article.sentiment, 2),
                    article.link,
                    article.sentiment_emoji  # Use the property
                ])

        print(f"Sentiment summary and all articles exported to {filename}")
        