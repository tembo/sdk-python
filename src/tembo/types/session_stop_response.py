# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionStopResponse", "State"]


class State(BaseModel):
    current: Optional[Literal["inProgress", "queued", "completed", "failed", "cancelled"]] = None

    is_queued: bool = FieldInfo(alias="isQueued")

    is_cancelled: bool = FieldInfo(alias="isCancelled")

    is_completed: bool = FieldInfo(alias="isCompleted")

    is_failed: bool = FieldInfo(alias="isFailed")

    in_progress: bool = FieldInfo(alias="inProgress")


class SessionStopResponse(BaseModel):
    cancelled_sessions: int = FieldInfo(alias="cancelledSessions")

    cancelled_jobs: int = FieldInfo(alias="cancelledJobs")

    stopped_runtime_sessions: int = FieldInfo(alias="stoppedRuntimeSessions")

    interrupted_runtime_turns: int = FieldInfo(alias="interruptedRuntimeTurns")

    cancelled_runtime_turns: int = FieldInfo(alias="cancelledRuntimeTurns")

    state: Optional[State] = None
    """Canonical session state after stopping and reconciling queued work."""
