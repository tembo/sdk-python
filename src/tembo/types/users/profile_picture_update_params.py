# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict
from ..._types import FileTypes

__all__ = ["ProfilePictureUpdateParams"]


class ProfilePictureUpdateParams(TypedDict, total=False):
    file: Required[FileTypes]
