# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectUpdateDefaultsParams"]


class ProjectUpdateDefaultsParams(TypedDict, total=False):
    project_id: Required[Annotated[Optional[str], PropertyInfo(alias="projectId")]]
    """Project to make the organization default, or null to clear the default."""

    sandbox_size: Required[
        Annotated[
            Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"],
            PropertyInfo(alias="sandboxSize"),
        ]
    ]
    """Default workspace VM size for the organization."""
