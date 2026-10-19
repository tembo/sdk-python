# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, Literal, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BuildCreateParams"]


class BuildCreateParams(TypedDict, total=False):
    sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]]
    """VM sizes to build. Omit to use the project sizes. Cannot be combined with snapshotId."""

    snapshot_id: Annotated[str, PropertyInfo(alias="snapshotId")]
    """Rebuild one existing snapshot instead of building project sizes. Cannot be combined with sizes."""
