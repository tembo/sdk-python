# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SessionDocumentNodeParam", "Mark"]


class SessionDocumentNodeParam(TypedDict, total=False):
    type: str

    text: str

    attrs: Dict[str, object]

    marks: Iterable[Mark]

    content: Iterable["SessionDocumentNodeParam"]


class Mark(TypedDict, total=False):
    type: Required[str]

    attrs: Dict[str, object]
