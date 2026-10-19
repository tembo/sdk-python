# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MarketplaceRetrieveParams"]


class MarketplaceRetrieveParams(TypedDict, total=False):
    source: Required[str]
    """The source repository in owner/repo format. Domain-only sources cannot be downloaded and return 404."""
