# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationAuthorizeResponse"]


class IntegrationAuthorizeResponse(BaseModel):
    authorization_url: str = FieldInfo(alias="authorizationUrl")
