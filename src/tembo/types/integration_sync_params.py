# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IntegrationSyncParams"]


class IntegrationSyncParams(TypedDict, total=False):
    mode: Literal["immediate", "queued"]
    """queued schedules a background integration sync; immediate performs the sync in this request."""
