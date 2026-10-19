# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationRetrieveSyncStatusResponse"]


class IntegrationRetrieveSyncStatusResponse(BaseModel):
    active_job_count: int = FieldInfo(alias="activeJobCount")

    eligible_integration_count: int = FieldInfo(alias="eligibleIntegrationCount")
