# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketplaceListResponse", "Item"]


class Item(BaseModel):
    source: str

    skill_id: str = FieldInfo(alias="skillId")

    name: str

    installs: int


class MarketplaceListResponse(BaseModel):
    items: List[Item]

    next_cursor: None = FieldInfo(alias="nextCursor", default=None)
    """Always null; marketplace results have no continuation page."""
