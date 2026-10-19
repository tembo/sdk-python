# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubCreateFilters"]


class GithubCreateFilters(BaseModel):
    repositories: Optional[List[str]] = None

    ref_type: Optional[List[Literal["branch", "tag"]]] = FieldInfo(alias="refType", default=None)
    """Only trigger for the specified Git reference type: branch or tag."""

    branch_names: Optional[List[str]] = FieldInfo(alias="branchNames", default=None)

    tag_names: Optional[List[str]] = FieldInfo(alias="tagNames", default=None)
