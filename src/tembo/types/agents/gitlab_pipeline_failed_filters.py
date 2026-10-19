# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["GitlabPipelineFailedFilters"]


class GitlabPipelineFailedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pipeline is in one of the repositories"""

    branches: Optional[List[str]] = None
    """Only trigger for specific branches"""
