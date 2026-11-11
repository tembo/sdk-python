# File generated from our OpenAPI spec by Scalar. See README.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FolderCreateResponse"]


class FolderCreateResponse(BaseModel):
    id: str

    name: str

    color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"]
    """Folder icon color, from the same palette as project icons."""

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")
