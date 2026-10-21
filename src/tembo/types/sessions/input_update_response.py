# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InputUpdateResponse", "Question", "QuestionOption"]


class QuestionOption(BaseModel):
    label: str

    description: str


class Question(BaseModel):
    id: str

    header: str

    question: str

    is_other: bool = FieldInfo(alias="isOther")

    is_secret: bool = FieldInfo(alias="isSecret")

    options: List[QuestionOption]


class InputUpdateResponse(BaseModel):
    id: str

    tool_call_id: str = FieldInfo(alias="toolCallId")

    status: Literal["pending", "answered"]

    questions: List[Question]
