# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InputListResponse", "Item", "ItemQuestion", "ItemQuestionOption"]


class ItemQuestionOption(BaseModel):
    label: str

    description: str


class ItemQuestion(BaseModel):
    id: str

    header: str

    question: str

    is_other: bool = FieldInfo(alias="isOther")

    is_secret: bool = FieldInfo(alias="isSecret")

    options: List[ItemQuestionOption]


class Item(BaseModel):
    id: str

    tool_call_id: str = FieldInfo(alias="toolCallId")

    status: Literal["pending", "answered"]

    questions: List[ItemQuestion]


class InputListResponse(BaseModel):
    items: List[Item]

    next_cursor: None = FieldInfo(alias="nextCursor", default=None)
