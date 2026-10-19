# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationSyncAllResponse"]


class IntegrationSyncAllResponse(BaseModel):
    eligible_integration_count: int = FieldInfo(alias="eligibleIntegrationCount")

    integration_sync_job_count: int = FieldInfo(alias="integrationSyncJobCount")

    pull_request_sync_job_count: int = FieldInfo(alias="pullRequestSyncJobCount")
