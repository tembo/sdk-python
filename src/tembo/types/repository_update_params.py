# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RepositoryUpdateParams"]


class RepositoryUpdateParams(TypedDict, total=False):
    enabled: bool
    """Enable or disable this repository for Tembo. Disabled by default on creation."""

    base_branch: Annotated[Optional[str], PropertyInfo(alias="baseBranch")]
    """Default Git branch to start sessions from. Null clears the override."""

    target_branch: Annotated[Optional[str], PropertyInfo(alias="targetBranch")]
    """Default target branch for agent-created pull requests. Null clears the override."""
