# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProviderDiscoverSnykOrganizationsResponse", "Item"]


class Item(BaseModel):
    id: str

    name: Optional[str] = None

    slug: Optional[str] = None


class ProviderDiscoverSnykOrganizationsResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
