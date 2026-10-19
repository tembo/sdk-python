# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LinearIssueStatusChangedFilters"]


class LinearIssueStatusChangedFilters(BaseModel):
    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of the specified teams"""

    statuses: Optional[List[str]] = None
    """Only trigger if the issue was moved to one of the specified statuses"""

    previous_statuses: Optional[List[str]] = FieldInfo(alias="previousStatuses", default=None)
    """Only trigger when the issue changes from one of the specified previous statuses."""

    assigned_to: Optional[List[str]] = FieldInfo(alias="assignedTo", default=None)
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""
