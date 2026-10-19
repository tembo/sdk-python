# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MemberListResponse", "Item"]


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    role: Literal["org:admin", "org:member"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    email_address: str = FieldInfo(alias="emailAddress")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    status: Literal["active", "pending"]


class MemberListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
