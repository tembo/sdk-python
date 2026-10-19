# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BuildCancelResponse"]


class BuildCancelResponse(BaseModel):
    cancelled: Literal[True]

    id: str
