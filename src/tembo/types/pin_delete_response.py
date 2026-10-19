# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PinDeleteResponse"]


class PinDeleteResponse(BaseModel):
    type: Literal["session", "pull_request", "project"]
    """Kind of resource to pin or unpin: session, pull_request, or project."""

    id: str
    """ID of the session, pull request, or project, not a separate pin ID."""

    deleted: Literal[True]
