# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LinearIssueUpdatedFilters"]


class LinearIssueUpdatedFilters(BaseModel):
    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of the specified teams"""

    states: Optional[List[str]] = None
    """Only trigger if the issue state type matches one of the specified types"""

    assigned_to: Optional[List[str]] = FieldInfo(alias="assignedTo", default=None)
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""

    tembo_issues: Optional[bool] = FieldInfo(alias="temboIssues", default=None)
    """Enable agent for Tembo-updated issues (disabled by default)"""
