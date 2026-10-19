# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SecretUpdateParams"]


class SecretUpdateParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    key: str
    """Secret name used to reference it in the organization."""

    value: str
    """Secret plaintext value to encrypt and store. Retrieve and list operations return redacted summaries, not this value."""
