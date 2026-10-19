# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel

__all__ = ["EnvironmentVariableCreateResponse", "Item"]


class Item(BaseModel):
    key: str


class EnvironmentVariableCreateResponse(BaseModel):
    items: List[Item]
