# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrganizationUpdateResponse"]


class OrganizationUpdateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    name: str

    slug: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    member_count: int = FieldInfo(alias="memberCount")
