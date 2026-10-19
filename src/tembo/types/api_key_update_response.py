# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["APIKeyUpdateResponse"]


class APIKeyUpdateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    id: str

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)

    name: Optional[str] = None

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")

    token_preview: str = FieldInfo(alias="tokenPreview")
