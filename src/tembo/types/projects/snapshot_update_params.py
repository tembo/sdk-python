# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SnapshotUpdateParams"]


class SnapshotUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    name: Optional[str]
    """Rename the snapshot, or null to clear its name."""

    pinned: bool
    """Pin the snapshot with true to retain it, or unpin with false. This is separate from user sidebar resource pins."""
