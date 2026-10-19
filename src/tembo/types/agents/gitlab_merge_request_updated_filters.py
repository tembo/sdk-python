# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GitlabMergeRequestUpdatedFilters"]


class GitlabMergeRequestUpdatedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the merge request is in one of the repositories"""

    pushed_by: Optional[List[str]] = FieldInfo(alias="pushedBy", default=None)
    """Only trigger if the commits were pushed by one of the specified users"""

    draft_mrs: Optional[bool] = FieldInfo(alias="draftMrs", default=None)
    """Include draft merge requests. Drafts are excluded when omitted or false."""

    tembo_mrs: Optional[bool] = FieldInfo(alias="temboMrs", default=None)
    """Enable agent for Tembo-created merge requests (disabled by default)"""
