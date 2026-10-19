# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationSyncResponse"]


class IntegrationSyncResponse(BaseModel):
    integration_id: str = FieldInfo(alias="integrationId")

    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)

    mode: Literal["immediate", "queued"]
