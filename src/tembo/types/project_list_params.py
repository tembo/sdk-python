# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    default_only: Annotated[Literal["true"], PropertyInfo(alias="defaultOnly")]
    """Only projects configured as defaults for at least one VM size."""

    search: str
    """Search project names."""
