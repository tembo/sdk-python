# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TipTapImageAttributesParam"]


class TipTapImageAttributesParam(TypedDict, total=False):
    src: Optional[str]

    alt: Optional[str]

    title: Optional[str]

    width: Optional[str]

    data_uploading: Annotated[Optional[str], PropertyInfo(alias="data-uploading")]

    data_placeholder_id: Annotated[Optional[str], PropertyInfo(alias="data-placeholder-id")]

    upload_progress: Annotated[Optional[str], PropertyInfo(alias="upload-progress")]
