# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionListEventsParams"]


class SessionListEventsParams(TypedDict, total=False):
    cursor: Union[str, int]
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    message_id: Annotated[Union[str, Literal["null"]], PropertyInfo(alias="messageId")]
    """Filter by message ID, or "null" for session-level events."""

    after: Union[str, int]
    """Only return events recorded after this event ID."""
