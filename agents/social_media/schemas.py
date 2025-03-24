"""
    This module contains the schemas for the social media agents.
"""

from enum import Enum
from pydantic import BaseModel


class StatusEnum(str, Enum):
    """
        This class represents the status of the tweet.
    """
    PENDING = "Pending"
    COMPLETED = "Completed"


class TimeEnum(str, Enum):
    """
        This class represents the time of the tweet.
    """
    MORNING = "Morning"
    AFTERNOON = "Afternoon"
    EVENING = "Evening"


class TweetFields(BaseModel):
    """
        This class represents the schema for the tweet fields.
    """
    Time: TimeEnum
    Status: StatusEnum


class TweetSheet(BaseModel):
    """
        This class represents the schema for the tweet sheet.
    """
    id: str
    createdTime: str
    fields: TweetFields
