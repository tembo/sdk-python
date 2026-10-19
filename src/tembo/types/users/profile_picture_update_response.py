# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProfilePictureUpdateResponse"]


class ProfilePictureUpdateResponse(BaseModel):
    user_id: str = FieldInfo(alias="userId")

    url: str
