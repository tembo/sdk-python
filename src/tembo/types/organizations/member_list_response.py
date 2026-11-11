# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MemberListResponse", "Item", "Item2", "Item2Role", "Item3", "Item3Role"]


class Item3Role(BaseModel):
    id: str

    name: str


class Item3(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: None = FieldInfo(alias="userId", default=None)

    email_address: str = FieldInfo(alias="emailAddress")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    role: Optional[Item3Role] = None

    status: Literal["pending"]


class Item2Role(BaseModel):
    id: str

    name: str


class Item2(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")

    email_address: str = FieldInfo(alias="emailAddress")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    role: Item2Role

    status: Literal["active"]


Item: TypeAlias = Union[Item2, Item3]


class MemberListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
