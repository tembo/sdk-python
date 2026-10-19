# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionStopParams"]


class SessionStopParams(TypedDict, total=False):
    cancel_queued: Annotated[bool, PropertyInfo(alias="cancelQueued")]
    """Also cancel pending queued messages instead of continuing with the next queued message. Does not archive the session."""
