# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EnvironmentVariableCreateParams"]


class EnvironmentVariableCreateParams(TypedDict, total=False):
    key: Required[str]
    """Environment variable name, e.g. GITHUB_TOKEN."""

    value: Required[str]
    """Plaintext value to encrypt and store. List operations never return it."""
