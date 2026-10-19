# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubPullRequestSynchronizeFilters"]


class GithubPullRequestSynchronizeFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    pushed_by: Optional[List[str]] = FieldInfo(alias="pushedBy", default=None)
    """Only trigger if the commits were pushed by one of the specified users"""

    draft_prs: Optional[bool] = FieldInfo(alias="draftPrs", default=None)
    """Trigger even if the pull request is a draft"""

    tembo_prs: Optional[bool] = FieldInfo(alias="temboPrs", default=None)
    """Enable agent for Tembo-created pull requests (enabled by default)"""
