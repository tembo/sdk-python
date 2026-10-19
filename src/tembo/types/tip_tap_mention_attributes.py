# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional, TYPE_CHECKING

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TipTapMentionAttributes", "Metadata"]


class Metadata(BaseModel):
    integration_type: Optional[str] = FieldInfo(alias="integrationType", default=None)

    code_repository_id: Optional[str] = FieldInfo(alias="codeRepositoryId", default=None)

    is_header: Optional[bool] = FieldInfo(alias="isHeader", default=None)

    argument_hint: Optional[str] = FieldInfo(alias="argumentHint", default=None)

    command_name: Optional[str] = FieldInfo(alias="commandName", default=None)

    source: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]


class TipTapMentionAttributes(BaseModel):
    id: Optional[str] = None

    label: Optional[str] = None

    type: Optional[str] = None

    mention_suggestion_char: Optional[str] = FieldInfo(alias="mentionSuggestionChar", default=None)

    metadata: Optional[Metadata] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]
