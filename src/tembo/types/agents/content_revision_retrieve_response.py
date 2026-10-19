# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..tip_tap_document import TipTapDocument

__all__ = ["ContentRevisionRetrieveResponse"]


class ContentRevisionRetrieveResponse(BaseModel):
    version: int

    author_id: Optional[str] = FieldInfo(alias="authorId", default=None)

    author_name: Optional[str] = FieldInfo(alias="authorName", default=None)

    source: str

    restored_from_version: Optional[int] = FieldInfo(alias="restoredFromVersion", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    instructions: Optional[TipTapDocument] = None
    """The instruction JSON document saved in this revision. Other agent configuration is not versioned."""
