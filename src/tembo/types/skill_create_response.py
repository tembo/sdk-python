# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SkillCreateResponse", "File"]


class File(BaseModel):
    content: str

    encoding: Literal["utf8", "base64"]

    filename: str

    id: str


class SkillCreateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    description: str

    id: str

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    files: List[File]
