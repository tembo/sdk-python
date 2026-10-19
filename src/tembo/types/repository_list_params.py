# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["RepositoryListParams"]


class RepositoryListParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    enabled: Literal["all", "true", "false"]
    """Select enabled repositories, disabled repositories, or all. The public API defaults to enabled repositories."""

    ids: SequenceNotStr[str]
    """Filter by repository IDs, supplied as a comma-separated list."""

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]
    """Filter repositories belonging to this integration."""

    order: Literal["asc", "desc"]
    """Sort direction: ascending or descending."""

    search: str
    """Search repository names and owners."""

    sort: Literal["createdAt", "integration", "name", "pullRequests", "updatedAt"]
    """Sort by creation time, integration, name, pull request count, or update time."""
