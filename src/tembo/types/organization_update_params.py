# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    name: str
    """Organization display name."""

    slug: str
    """Unique organization URL slug using lowercase letters, numbers, and single hyphens."""

    onboarding_completed: Annotated[bool, PropertyInfo(alias="onboardingCompleted")]
    """Mark organization onboarding as completed or incomplete."""
