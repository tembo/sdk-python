# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubIssueClosedFilters"]


class GithubIssueClosedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the issue is in one of the repositories"""

    opened_by: Optional[List[str]] = FieldInfo(alias="openedBy", default=None)
    """Only trigger if the issue was opened by one of the specified users"""

    tembo_issues: Optional[bool] = FieldInfo(alias="temboIssues", default=None)
    """Enable agent for Tembo-created issues (disabled by default)"""
