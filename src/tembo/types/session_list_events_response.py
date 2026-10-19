# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .session_event_data import SessionEventData

__all__ = ["SessionListEventsResponse", "Item"]


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    event_type: str = FieldInfo(alias="eventType")

    id: int

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)

    provider: Literal["anthropic", "openai", "openai_responses", "openai_completions", "tembo"]

    session_id: str = FieldInfo(alias="sessionId")

    event_data: SessionEventData = FieldInfo(alias="eventData")


class SessionListEventsResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
