# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FolderCreateParams"]


class FolderCreateParams(TypedDict, total=False):
    name: Required[str]
    """Folder name shown in the sidebar."""

    color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"]
    """Folder icon color. Defaults to neutral."""
