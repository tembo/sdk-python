# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MemberCreateParams"]


class MemberCreateParams(TypedDict, total=False):
    email_address: Required[Annotated[str, PropertyInfo(alias="emailAddress")]]
    """Email address of the user to add or invite."""

    role: Literal["org:admin", "org:member"]
    """Organization role to grant: org:admin or org:member."""
