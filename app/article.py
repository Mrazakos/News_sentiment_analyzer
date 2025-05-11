from dataclasses import dataclass
from typing import Optional

@dataclass
class Article:
    title: str
    description: str
    content: str
    published_at: str
    sentiment: Optional[float] = None
    link: Optional[str] = None

    @property
    def sentiment_emoji(self) -> str:
        """
        Determine the emoji based on the sentiment score.
        :return: Emoji representing the sentiment
        """
        if self.sentiment is None:
            return "⚪"  # No sentiment available
        elif self.sentiment > 0.1:
            return "🟢"  # Positive
        elif self.sentiment < -0.1:
            return "🔴"  # Negative
        else:
            return "🟡"  # Neutral
