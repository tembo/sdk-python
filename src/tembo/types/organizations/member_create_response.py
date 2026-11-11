# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MemberCreateResponse", "MemberCreateResponseRole", "MemberCreateResponse2", "MemberCreateResponse2Role"]


class MemberCreateResponse2Role(BaseModel):
    id: str

    name: str


class MemberCreateResponse2(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: None = FieldInfo(alias="userId", default=None)

    email_address: str = FieldInfo(alias="emailAddress")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    role: Optional[MemberCreateResponse2Role] = None

    status: Literal["pending"]


class MemberCreateResponseRole(BaseModel):
    id: str

    name: str


class MemberCreateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")

    email_address: str = FieldInfo(alias="emailAddress")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    role: MemberCreateResponseRole

    status: Literal["active"]


MemberCreateResponse: TypeAlias = Union[MemberCreateResponse, MemberCreateResponse2]
