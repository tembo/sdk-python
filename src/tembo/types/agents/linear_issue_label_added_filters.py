# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LinearIssueLabelAddedFilters"]


class LinearIssueLabelAddedFilters(BaseModel):
    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of the specified teams"""

    assigned_to: Optional[List[str]] = FieldInfo(alias="assignedTo", default=None)
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if one of the specified labels was added to the issue"""
