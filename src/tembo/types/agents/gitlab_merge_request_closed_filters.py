# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GitlabMergeRequestClosedFilters"]


class GitlabMergeRequestClosedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the merge request is in one of the repositories"""

    closed_by: Optional[List[str]] = FieldInfo(alias="closedBy", default=None)
    """Only trigger if the merge request was closed by one of the specified users"""

    tembo_mrs: Optional[bool] = FieldInfo(alias="temboMrs", default=None)
    """Enable agent for Tembo-created merge requests (disabled by default)"""
