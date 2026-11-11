# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RunCreateResponse"]


class RunCreateResponse(BaseModel):
    job_id: str = FieldInfo(alias="jobId")

    run_id: str = FieldInfo(alias="runId")
    """ID of the agent run. Retrieve it with GET /v1/agents/{agentId}/runs/{runId}; its sessionId is set once the run starts its session."""

    agent_id: str = FieldInfo(alias="agentId")

    status: Literal["queued"]
