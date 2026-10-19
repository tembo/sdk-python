# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Organization display name."""

    slug: str
    """Unique organization URL slug using lowercase letters, numbers, and single hyphens."""
