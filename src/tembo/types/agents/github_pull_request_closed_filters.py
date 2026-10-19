# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubPullRequestClosedFilters"]


class GithubPullRequestClosedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    opened_by: Optional[List[str]] = FieldInfo(alias="openedBy", default=None)
    """Only trigger if the pull request was opened by one of the specified users"""

    tembo_prs: Optional[bool] = FieldInfo(alias="temboPrs", default=None)
    """Enable agent for Tembo-created pull requests (enabled by default)"""
