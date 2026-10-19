# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AtlassianIssueLabelAddedFilters"]


class AtlassianIssueLabelAddedFilters(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of these Jira teams. Enter exact team names or team IDs (from the team profile URL)."""

    labels: Optional[List[str]] = None
    """Only trigger if one of the specified labels was added"""
