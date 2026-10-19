# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationListSentryEnvironmentsResponse"]


class IntegrationListSentryEnvironmentsResponse(BaseModel):
    items: List[str]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
