# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SecretListResponse", "Item"]


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    key: str

    updated_at: datetime = FieldInfo(alias="updatedAt")


class SecretListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
