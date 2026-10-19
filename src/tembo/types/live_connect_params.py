# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LiveConnectParams"]


class LiveConnectParams(TypedDict, total=False):
    ticket: Required[str]
    """Short-lived connection ticket returned by liveConnectionTicket. Used to authenticate the native WebSocket connection."""
