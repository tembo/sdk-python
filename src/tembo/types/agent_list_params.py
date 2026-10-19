# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    ids: str
    """Filter by agent IDs, supplied as a comma-separated list."""

    search: str
    """Search agent names."""

    archived: bool
    """true lists archived agents; false or omitted lists unarchived agents. Use this to find agents to restore."""

    sort: Literal["latestRun", "runCount"]
    """Sort agents by latest run or run count."""

    status: str
    """Filter by enabled (running) or paused status, supplied as a comma-separated list; this is not individual run execution status."""

    integration: str
    """Filter by integration provider types, supplied as a comma-separated list."""

    author: str
    """Filter by creator user IDs, supplied as a comma-separated list."""
