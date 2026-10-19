# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InsightListRepositoriesResponse", "Item"]


class Item(BaseModel):
    code_repository_id: str = FieldInfo(alias="codeRepositoryId")

    name: str

    url: str

    provider: str

    prs_created: int = FieldInfo(alias="prsCreated")

    prs_merged: int = FieldInfo(alias="prsMerged")

    tembo_contribution: float = FieldInfo(alias="temboContribution")


class InsightListRepositoriesResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
