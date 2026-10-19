# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TipTapLinkMarkParam", "Attrs"]


class TipTapLinkMarkParam(TypedDict, total=False):
    type: Required[Literal["link"]]

    attrs: Attrs


_AttrsReservedKeywords = TypedDict(
    "_AttrsReservedKeywords",
    {
        "class": Optional[str],
    },
    total=False,
)


class Attrs(_AttrsReservedKeywords, total=False):
    href: Optional[str]

    target: Optional[str]

    rel: Optional[str]

    title: Optional[str]
