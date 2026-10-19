# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubTemboPullRequestOpenedFilters"]


class GithubTemboPullRequestOpenedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    draft_prs: Optional[bool] = FieldInfo(alias="draftPrs", default=None)
    """Also trigger for draft pull requests"""
