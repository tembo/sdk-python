# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["UserDeleteParams", "DeletionQuestionnaire"]


class UserDeleteParams(TypedDict, total=False):
    deletion_questionnaire: Annotated[DeletionQuestionnaire, PropertyInfo(alias="deletionQuestionnaire")]
    """Optional account-deletion feedback. Account deletion is queued regardless of whether feedback is supplied."""


class DeletionQuestionnaire(TypedDict, total=False):
    reasons: Required[SequenceNotStr[str]]

    other_reason: Annotated[str, PropertyInfo(alias="otherReason")]

    submitted_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="submittedAt", format="iso8601")]]
