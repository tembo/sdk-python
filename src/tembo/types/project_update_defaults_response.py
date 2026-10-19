# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectUpdateDefaultsResponse"]


class ProjectUpdateDefaultsResponse(BaseModel):
    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """Project to make the organization default, or null to clear the default."""

    sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"] = FieldInfo(
        alias="sandboxSize"
    )
    """Default workspace VM size for the organization."""
