# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubPullRequestMergedFilters"]


class GithubPullRequestMergedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    merged_by: Optional[List[str]] = FieldInfo(alias="mergedBy", default=None)
    """Only trigger if the pull request was merged by one of the specified users"""

    tembo_prs: Optional[bool] = FieldInfo(alias="temboPrs", default=None)
    """Enable agent for Tembo-created pull requests (enabled by default)"""
