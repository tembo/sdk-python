# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InsightRetrieveParams"]


class InsightRetrieveParams(TypedDict, total=False):
    range: Literal["1d", "7d", "30d", "1y"]
    """Time range to aggregate: last day, 7 days, 30 days, or year. Defaults to 1y."""
