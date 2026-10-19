# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional, TYPE_CHECKING

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TipTapImageAttributes"]


class TipTapImageAttributes(BaseModel):
    src: Optional[str] = None

    alt: Optional[str] = None

    title: Optional[str] = None

    width: Optional[str] = None

    data_uploading: Optional[str] = FieldInfo(alias="data-uploading", default=None)

    data_placeholder_id: Optional[str] = FieldInfo(alias="data-placeholder-id", default=None)

    upload_progress: Optional[str] = FieldInfo(alias="upload-progress", default=None)

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
