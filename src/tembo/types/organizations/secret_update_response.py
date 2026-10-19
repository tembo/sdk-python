# File generated from our OpenAPI spec by Scalar. See README.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SecretUpdateResponse"]


class SecretUpdateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    key: str

    updated_at: datetime = FieldInfo(alias="updatedAt")
