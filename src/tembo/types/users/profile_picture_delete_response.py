# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProfilePictureDeleteResponse"]


class ProfilePictureDeleteResponse(BaseModel):
    user_id: str = FieldInfo(alias="userId")

    deleted: Literal[True]
