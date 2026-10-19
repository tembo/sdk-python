# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RunListResponse", "Item"]


class Item(BaseModel):
    id: str

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)

    status: str

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    duration_ms: int = FieldInfo(alias="durationMs")
    """Measured duration of the agent run in milliseconds."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)


class RunListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
