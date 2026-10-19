# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubWorkflowRunFailedFilters"]


class GithubWorkflowRunFailedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the workflow run is in one of the repositories"""

    workflow_names: Optional[List[str]] = FieldInfo(alias="workflowNames", default=None)
    """Only trigger for specific workflow names"""

    branches: Optional[List[str]] = None
    """Only trigger for specific branches"""
