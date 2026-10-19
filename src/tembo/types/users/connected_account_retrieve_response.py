# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConnectedAccountRetrieveResponse"]


class ConnectedAccountRetrieveResponse(BaseModel):
    account_id: str = FieldInfo(alias="accountId")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    id: str

    provider_id: str = FieldInfo(alias="providerId")

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    email: Optional[str] = None

    scopes: List[str]

    username: Optional[str] = None
