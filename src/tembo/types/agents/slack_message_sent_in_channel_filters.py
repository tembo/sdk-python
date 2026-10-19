# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SlackMessageSentInChannelFilters"]


class SlackMessageSentInChannelFilters(BaseModel):
    channels: Optional[List[str]] = None
    """Only trigger if the message is sent in one of the channels"""

    users: Optional[List[str]] = None
    """Only trigger if the message was sent by one of these user names"""

    message_contains: Optional[List[str]] = FieldInfo(alias="messageContains", default=None)
    """Only trigger if the message contains one of these substrings"""

    message_not_contains: Optional[List[str]] = FieldInfo(alias="messageNotContains", default=None)
    """Skip messages containing any of these case-sensitive substrings (for example, On-call handover:)"""
