# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["McpConnectionListParams"]


class McpConnectionListParams(TypedDict, total=False):
    connected: bool
    """Filter by whether the MCP connection has completed connection or authorization."""

    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    search: str
    """Search MCP connection names or server URLs."""
