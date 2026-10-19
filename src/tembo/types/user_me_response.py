# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserMeResponse"]


class UserMeResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    email: Optional[str] = None

    email_verified: bool = FieldInfo(alias="emailVerified")

    id: str

    image: Optional[str] = None

    name: Optional[str] = None

    updated_at: datetime = FieldInfo(alias="updatedAt")
