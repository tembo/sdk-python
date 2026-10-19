# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntegrationAuthorizeParams"]


class IntegrationAuthorizeParams(TypedDict, total=False):
    return_url: Annotated[str, PropertyInfo(alias="returnUrl")]
    """URL to return to after provider authorization. Must use HTTPS or localhost HTTP."""

    capability: Literal["confluenceTriggers"]
    """Request authorization for Confluence automation triggers instead of the default integration capability."""
