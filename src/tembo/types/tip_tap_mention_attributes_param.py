# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TipTapMentionAttributesParam", "Metadata"]


class TipTapMentionAttributesParam(TypedDict, total=False):
    id: Optional[str]

    label: Optional[str]

    type: Optional[str]

    mention_suggestion_char: Annotated[Optional[str], PropertyInfo(alias="mentionSuggestionChar")]

    metadata: Optional[Metadata]


class Metadata(TypedDict, total=False):
    integration_type: Annotated[str, PropertyInfo(alias="integrationType")]

    code_repository_id: Annotated[str, PropertyInfo(alias="codeRepositoryId")]

    is_header: Annotated[bool, PropertyInfo(alias="isHeader")]

    argument_hint: Annotated[str, PropertyInfo(alias="argumentHint")]

    command_name: Annotated[str, PropertyInfo(alias="commandName")]

    source: str
