# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Filter messages belonging to this session."""

    thread_id: Annotated[str, PropertyInfo(alias="threadId")]
    """Filter messages belonging to this thread."""
