# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RunCreateResponse"]


class RunCreateResponse(BaseModel):
    job_id: str = FieldInfo(alias="jobId")

    agent_id: str = FieldInfo(alias="agentId")

    status: Literal["queued"]
