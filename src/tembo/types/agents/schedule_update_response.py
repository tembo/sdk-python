# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScheduleUpdateResponse"]


class ScheduleUpdateResponse(BaseModel):
    id: str

    cron: str

    last_run_at: Optional[datetime] = FieldInfo(alias="lastRunAt", default=None)

    next_run_at: Optional[datetime] = FieldInfo(alias="nextRunAt", default=None)

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    agent_id: str = FieldInfo(alias="agentId")
