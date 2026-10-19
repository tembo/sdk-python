# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    expires_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(alias="expiresAt", format="iso8601")]
    """Future ISO 8601 expiration timestamp. Omit or use null for a key that does not expire."""

    name: str
    """Display name for identifying this API key."""
