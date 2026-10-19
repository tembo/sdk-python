# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SourceListResponse", "Item", "ItemIntegration", "ItemRepository"]


class ItemRepository(BaseModel):
    id: str

    name: str

    owner: Optional[str] = None

    base_branch: Optional[str] = FieldInfo(alias="baseBranch", default=None)

    provider: str


class ItemIntegration(BaseModel):
    type: str


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    external_url: Optional[str] = FieldInfo(alias="externalUrl", default=None)

    id: str

    last_scanned_at: Optional[datetime] = FieldInfo(alias="lastScannedAt", default=None)

    last_seen_at: Optional[datetime] = FieldInfo(alias="lastSeenAt", default=None)

    name: str

    type: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    integration: Optional[ItemIntegration] = None

    repositories: List[ItemRepository]


class SourceListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
