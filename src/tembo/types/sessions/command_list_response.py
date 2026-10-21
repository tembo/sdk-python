# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CommandListResponse", "Item"]


class Item(BaseModel):
    name: str

    command: str

    description: Optional[str] = None

    argument_hint: Optional[str] = FieldInfo(alias="argumentHint", default=None)

    source: Literal["builtin", "project", "mcp", "skill", "unknown"]


class CommandListResponse(BaseModel):
    items: List[Item]

    next_cursor: None = FieldInfo(alias="nextCursor", default=None)

    cached: bool
