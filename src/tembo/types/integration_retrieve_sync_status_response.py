# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationRetrieveSyncStatusResponse"]


class IntegrationRetrieveSyncStatusResponse(BaseModel):
    has_active_jobs: bool = FieldInfo(alias="hasActiveJobs")

    eligible_integration_count: int = FieldInfo(alias="eligibleIntegrationCount")
