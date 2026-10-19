# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tip_tap_extension_attributes import TipTapExtensionAttributes

__all__ = ["TipTapMarkParam"]


class TipTapMarkParam(TypedDict, total=False):
    type: Required[str]

    attrs: TipTapExtensionAttributes
