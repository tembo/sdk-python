# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["EnvironmentVariableCreateParams", "Secret"]


class EnvironmentVariableCreateParams(TypedDict, total=False):
    secrets: Required[Iterable[Secret]]
    """Environment variables to add or replace by key, preserving other keys. Values are encrypted and not returned by list operations."""


class Secret(TypedDict, total=False):
    key: Required[str]
    """Environment-variable name."""

    value: Required[str]
    """Secret environment-variable value; stored encrypted and not returned by list operations."""
