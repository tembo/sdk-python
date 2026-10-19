# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpConnectionListResponse", "Item"]


class Item(BaseModel):
    connected_at: Optional[datetime] = FieldInfo(alias="connectedAt", default=None)

    id: str

    name: str

    server_url: Optional[str] = FieldInfo(alias="serverUrl", default=None)

    type: Literal["remote", "stdio"]

    visibility: Literal["shared", "personal"]
    """shared makes the connection available to the organization; personal restricts it to its owner."""


class McpConnectionListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
