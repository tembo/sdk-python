# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SkillListResponse", "Item"]


class Item(BaseModel):
    description: str

    id: str

    name: str

    keywords: List[str]

    source: Literal["organization", "repository"]


class SkillListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
