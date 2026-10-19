# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContentRevisionListResponse", "Item"]


class Item(BaseModel):
    version: int

    author_id: Optional[str] = FieldInfo(alias="authorId", default=None)

    author_name: Optional[str] = FieldInfo(alias="authorName", default=None)

    source: str

    restored_from_version: Optional[int] = FieldInfo(alias="restoredFromVersion", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")


class ContentRevisionListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
