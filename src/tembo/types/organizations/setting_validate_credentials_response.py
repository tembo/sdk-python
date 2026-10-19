# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["SettingValidateCredentialsResponse"]


class SettingValidateCredentialsResponse(BaseModel):
    valid: bool
    """Whether the supplied credentials passed provider validation."""
