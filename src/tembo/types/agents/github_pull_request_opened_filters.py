# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubPullRequestOpenedFilters"]


class GithubPullRequestOpenedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    labels: Optional[List[str]] = None
    """Only trigger if the pull request has at least one of the specified labels"""

    opened_by: Optional[List[str]] = FieldInfo(alias="openedBy", default=None)
    """Only trigger if the pull request was opened by one of the specified users"""

    branches: Optional[List[str]] = None
    """Only trigger if the pull request targets one of these branches"""

    draft_prs: Optional[bool] = FieldInfo(alias="draftPrs", default=None)
    """Trigger also for draft pull requests (disabled by default)"""

    tembo_prs: Optional[bool] = FieldInfo(alias="temboPrs", default=None)
    """Enable agent for Tembo-created pull requests (enabled by default)"""
