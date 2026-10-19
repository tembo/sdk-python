# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["PinUpdateParams", "Placement", "PlacementTarget"]


class PinUpdateParams(TypedDict, total=False):
    resource_type: Required[
        Annotated[Literal["session", "pull_request", "project"], PropertyInfo(alias="resourceType")]
    ]
    """Kind of resource to pin or unpin: session, pull_request, or project."""

    placement: Required[Placement]
    """Reorder an existing pin before or after another pin. Use createPin to pin a resource and deletePin to unpin it."""


class PlacementTarget(TypedDict, total=False):
    type: Required[Literal["session", "pull_request", "project"]]
    """Kind of resource to pin or unpin: session, pull_request, or project."""

    id: Required[str]
    """ID of the session, pull request, or project, not a separate pin ID."""


class Placement(TypedDict, total=False):
    target: Required[PlacementTarget]
    """Existing pin to place this pin next to."""

    position: Required[Literal["before", "after"]]
    """Whether to place this pin before or after the target."""
