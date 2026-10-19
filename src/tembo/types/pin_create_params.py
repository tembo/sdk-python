# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PinCreateParams", "Placement", "PlacementTarget"]


class PinCreateParams(TypedDict, total=False):
    type: Required[Literal["session", "pull_request", "project"]]
    """Kind of resource to pin or unpin: session, pull_request, or project."""

    id: Required[str]
    """ID of the session, pull request, or project, not a separate pin ID."""

    placement: Placement
    """Position of a new pin relative to another pin. Omit to add it first. Ignored if the resource is already pinned; use updatePin to reorder."""


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
