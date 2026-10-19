# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AtlassianIssueUpdatedFilters"]


class AtlassianIssueUpdatedFilters(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    issue_types: Optional[List[str]] = FieldInfo(alias="issueTypes", default=None)
    """Only trigger for the specified issue types, such as Story, Bug, or Sub-task."""

    assigned_to: Optional[List[str]] = FieldInfo(alias="assignedTo", default=None)
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""
