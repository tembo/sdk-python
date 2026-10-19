# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionForkParams"]


class SessionForkParams(TypedDict, total=False):
    prompt: str
    """Optional first task for the independent fork. Existing messages are not replayed."""

    title: str
    """Display title for the forked session."""

    queue_right_away: Annotated[bool, PropertyInfo(alias="queueRightAway")]
    """Start the supplied prompt immediately. Without a prompt, the fork waits for a new message."""
