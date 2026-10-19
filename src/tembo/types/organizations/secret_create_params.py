# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    key: Required[str]
    """Secret name used to reference it in the organization."""

    value: Required[str]
    """Secret plaintext value to encrypt and store. Retrieve and list operations return redacted summaries, not this value."""
