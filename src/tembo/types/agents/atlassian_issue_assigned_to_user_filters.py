# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AtlassianIssueAssignedToUserFilters"]


class AtlassianIssueAssignedToUserFilters(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    assigned_to: Optional[List[str]] = FieldInfo(alias="assignedTo", default=None)
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""

    include_new_issues: Optional[bool] = FieldInfo(alias="includeNewIssues", default=None)
    """Also trigger for newly created issues that are already assigned"""
