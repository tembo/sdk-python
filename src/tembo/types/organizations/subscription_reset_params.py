# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionResetParams"]


class SubscriptionResetParams(TypedDict, total=False):
    idempotency_key: Required[Annotated[str, PropertyInfo(alias="idempotencyKey")]]
    """Unique UUID for this reset attempt. Reuse the same UUID when retrying to avoid redeeming another reset credit."""

    provider: Required[Literal["chatgpt"]]
    """Subscription provider whose rate-limit reset credit to redeem. Currently only chatgpt is supported."""
