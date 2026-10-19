# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionStopResponse"]


class SessionStopResponse(BaseModel):
    cancelled_sessions: int = FieldInfo(alias="cancelledSessions")

    cancelled_jobs: int = FieldInfo(alias="cancelledJobs")

    stopped_runtime_sessions: int = FieldInfo(alias="stoppedRuntimeSessions")

    interrupted_runtime_turns: int = FieldInfo(alias="interruptedRuntimeTurns")

    cancelled_runtime_turns: int = FieldInfo(alias="cancelledRuntimeTurns")
