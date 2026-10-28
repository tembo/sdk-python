# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["BillingListUsageParams"]


class BillingListUsageParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    type: Literal["all", "sessions", "warm-pool"]
    """Usage types to include. Defaults to sessions for backwards compatibility."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Filter billing usage to this session."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Include sessions created or warm pool runtime at or after this ISO 8601 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Include sessions created or warm pool runtime before this ISO 8601 timestamp."""

    created_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="createdBy")]
    """Filter by creator IDs, supplied as a comma-separated list."""

    models: SequenceNotStr[str]
    """Filter by model names, supplied as a comma-separated list."""
