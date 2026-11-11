# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectRetrieveDefaultsResponse"]


class ProjectRetrieveDefaultsResponse(BaseModel):
    sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"] = FieldInfo(
        alias="sandboxSize"
    )
    """Default workspace VM size for the organization."""

    max_sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]] = FieldInfo(
        alias="maxSandboxSize", default=None
    )
    """Largest VM size the organization plan allows, or null when unlimited."""
