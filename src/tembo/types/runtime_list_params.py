# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RuntimeListParams"]


class RuntimeListParams(TypedDict, total=False):
    cursor: Literal["claudeCode", "codex", "opencode", "cursor", "amp", "fx", "pi"]
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""
