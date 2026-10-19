# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InsightUpdateParams"]


class InsightUpdateParams(TypedDict, total=False):
    enabled: Required[bool]
    """Enable or disable pull request contribution insight collection. Enabling starts the initial refresh when needed."""
