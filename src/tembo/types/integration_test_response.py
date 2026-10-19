# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["IntegrationTestResponse"]


class IntegrationTestResponse(BaseModel):
    healthy: bool

    message: str
