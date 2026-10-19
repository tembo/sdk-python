# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["IntegrationListParams"]


class IntegrationListParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    enabled: bool
    """Filter by whether integrations are enabled."""

    has_enabled_repositories: Annotated[bool, PropertyInfo(alias="hasEnabledRepositories")]
    """Filter by whether integrations have enabled repositories."""

    ids: SequenceNotStr[str]
    """Filter by integration IDs, supplied as a comma-separated list."""

    search: str
    """Search integration provider types and external IDs."""

    type: SequenceNotStr[str]
    """Filter provider types, supplied as a comma-separated list."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Only integrations created after this ISO 8601 timestamp."""

    exclude_organization_name: Annotated[str, PropertyInfo(alias="excludeOrganizationName")]
    """Exclude integrations belonging to the named organization within the caller access scope."""

    include_total: Annotated[bool, PropertyInfo(alias="includeTotal")]
    """Include totalCount for matching integrations."""
