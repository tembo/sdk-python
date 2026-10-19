# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InsightUpdateResponse", "Data", "DataSummary", "DataSummaryChanges", "DataTimeSeries"]


class DataTimeSeries(BaseModel):
    month: str
    """Bucket key: YYYY-MM for 1y, YYYY-MM-DD (UTC) for 7d and 30d, and an ISO 8601 hour start for 1d."""

    prs_with_tembo: int = FieldInfo(alias="prsWithTembo")

    prs_without_tembo: float = FieldInfo(alias="prsWithoutTembo")

    prs_merged: int = FieldInfo(alias="prsMerged")

    prs_created: int = FieldInfo(alias="prsCreated")

    tembo_contribution: float = FieldInfo(alias="temboContribution")


class DataSummaryChanges(BaseModel):
    prs_created: float = FieldInfo(alias="prsCreated")

    prs_merged: float = FieldInfo(alias="prsMerged")

    tasks_completed: float = FieldInfo(alias="tasksCompleted")

    tembo_contribution: float = FieldInfo(alias="temboContribution")


class DataSummary(BaseModel):
    tasks_completed: int = FieldInfo(alias="tasksCompleted")

    prs_created: int = FieldInfo(alias="prsCreated")

    prs_merged: int = FieldInfo(alias="prsMerged")

    tembo_contribution: float = FieldInfo(alias="temboContribution")

    changes: DataSummaryChanges


class Data(BaseModel):
    range: Literal["1d", "7d", "30d", "1y"]

    summary: DataSummary

    time_series: List[DataTimeSeries] = FieldInfo(alias="timeSeries")


class InsightUpdateResponse(BaseModel):
    id: Optional[str] = None

    status: Optional[Literal["syncing", "ready", "failed"]] = None

    range_start: Optional[datetime] = FieldInfo(alias="rangeStart", default=None)

    range_end: Optional[datetime] = FieldInfo(alias="rangeEnd", default=None)

    last_synced_at: Optional[datetime] = FieldInfo(alias="lastSyncedAt", default=None)

    enabled: bool

    data: Optional[Data] = None
