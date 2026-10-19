# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProviderDiscoverSnykOrganizationsParams"]


class ProviderDiscoverSnykOrganizationsParams(TypedDict, total=False):
    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]
    """Snyk service-account client ID to validate and use for organization discovery."""

    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]
    """Snyk service-account client secret. Used for discovery without saving an integration."""

    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""
