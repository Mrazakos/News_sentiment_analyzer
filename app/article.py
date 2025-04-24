from dataclasses import dataclass
from typing import Optional

@dataclass
class Article:
    title: str
    description: str
    content: str
    published_at: str
    sentiment: Optional[float] = None
