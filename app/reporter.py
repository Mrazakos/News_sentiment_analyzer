
import plotly.graph_objects as go
import pandas as pd


class ReportGenerator:
    def __init__(self, sentiment_analyzer):
      self.sentiment_analyzer = sentiment_analyzer  # Assuming sentiment_analyzer is already set up

    def generate_sentiment_over_time_chart(self, articles: list):
        """
        Generate a sentiment over time chart for a list of articles.
        :param articles: List of article objects with 'date', 'title', and 'description'
        :return: Plotly Figure (interactive chart)
        """
        sentiment_data = self.sentiment_analyzer.get_sentiment_over_time(articles)
        
        # Convert data into DataFrame
        df = pd.DataFrame(sentiment_data)
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate moving average (optional)
        df['moving_avg'] = df['sentiment'].rolling(window=3).mean()

        # Create the Plotly chart
        fig = go.Figure()

        # Add sentiment data line
        fig.add_trace(go.Scatter(x=df['date'], y=df['sentiment'], mode='lines+markers', name='Sentiment'))

        # Add moving average line (optional)
        fig.add_trace(go.Scatter(x=df['date'], y=df['moving_avg'], mode='lines', name='Moving Average', line=dict(dash='dash')))

        # Customize layout
        fig.update_layout(
            title="Sentiment Over Time",
            xaxis_title="Date",
            yaxis_title="Sentiment Score",
            template="plotly_dark",  # You can change the theme
        )

        # Return the figure to be displayed or saved
        return fig