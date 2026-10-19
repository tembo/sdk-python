# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationRetrieveResponse"]


class IntegrationRetrieveResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    display_name: str = FieldInfo(alias="displayName")

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    id: str

    last_synced_at: Optional[datetime] = FieldInfo(alias="lastSyncedAt", default=None)

    repository_count: int = FieldInfo(alias="repositoryCount")

    source_count: int = FieldInfo(alias="sourceCount")

    type: str

    updated_at: datetime = FieldInfo(alias="updatedAt")
