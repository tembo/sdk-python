# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketplaceRetrieveResponse", "File"]


class File(BaseModel):
    content: str
    """Complete text content of the skill file."""

    filename: str
    """Relative file path within the skill, such as SKILL.md."""


class MarketplaceRetrieveResponse(BaseModel):
    source: str

    skill_id: str = FieldInfo(alias="skillId")

    files: List[File]

    hash: str
