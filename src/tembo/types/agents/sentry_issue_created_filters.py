# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SentryIssueCreatedFilters"]


class SentryIssueCreatedFilters(BaseModel):
    priorities: Optional[List[Literal["high", "medium", "low"]]] = None
    """Only trigger if the issue has one of the specified priorities"""

    project_slugs: Optional[List[str]] = FieldInfo(alias="projectSlugs", default=None)
    """Only trigger if the issue is in one of the specified projects"""
