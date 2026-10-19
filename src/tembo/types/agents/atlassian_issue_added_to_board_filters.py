# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AtlassianIssueAddedToBoardFilters"]


class AtlassianIssueAddedToBoardFilters(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    boards: Optional[List[str]] = None
    """Only trigger if the issue is on one of the specified boards"""

    statuses: Optional[List[str]] = None
    """Only trigger if the issue was moved to one of the specified statuses (board columns)"""

    assigned_to: Optional[List[str]] = FieldInfo(alias="assignedTo", default=None)
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""

    include_new_issues: Optional[bool] = FieldInfo(alias="includeNewIssues", default=None)
    """Also trigger for newly created issues (not just status changes)"""
