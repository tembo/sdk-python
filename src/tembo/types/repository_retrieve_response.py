# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RepositoryRetrieveResponse", "Provider"]


class Provider(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    integration_id: str = FieldInfo(alias="integrationId")

    type: str


class RepositoryRetrieveResponse(BaseModel):
    base_branch: Optional[str] = FieldInfo(alias="baseBranch", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    id: str

    name: str

    owner: Optional[str] = None

    provider: Provider

    target_branch: Optional[str] = FieldInfo(alias="targetBranch", default=None)

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str
