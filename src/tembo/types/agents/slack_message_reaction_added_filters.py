# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SlackMessageReactionAddedFilters"]


class SlackMessageReactionAddedFilters(BaseModel):
    emojis: Optional[List[str]] = None
    """Only trigger if one of these emoji reactions is added"""

    channels: Optional[List[str]] = None
    """Only trigger if the reaction is added in one of these channels"""

    users: Optional[List[str]] = None
    """Only trigger if the reaction is added by one of these user names"""
