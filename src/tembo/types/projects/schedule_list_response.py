# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScheduleListResponse", "Item"]


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    cron: str

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    id: str

    last_run_at: Optional[datetime] = FieldInfo(alias="lastRunAt", default=None)

    next_run_at: Optional[datetime] = FieldInfo(alias="nextRunAt", default=None)

    timezone: Optional[str] = None

    updated_at: datetime = FieldInfo(alias="updatedAt")

    project_id: str = FieldInfo(alias="projectId")


class ScheduleListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
