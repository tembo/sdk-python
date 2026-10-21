# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = ["InputUpdateParams"]


class InputUpdateParams(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    answers: Required[Dict[str, SequenceNotStr[str]]]
    """Answers keyed by question ID. Send an empty object to skip the questions."""
