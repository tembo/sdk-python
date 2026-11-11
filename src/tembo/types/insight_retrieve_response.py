# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InsightRetrieveResponse", "Data", "DataSummary", "DataSummaryChanges", "DataTimeSeries"]


class DataTimeSeries(BaseModel):
    month: str
    """Bucket key: YYYY-MM for 1y, YYYY-MM-DD (UTC) for 7d and 30d, and an ISO 8601 hour start for 1d."""

    prs_with_tembo: int = FieldInfo(alias="prsWithTembo")

    prs_without_tembo: float = FieldInfo(alias="prsWithoutTembo")

    prs_merged: int = FieldInfo(alias="prsMerged")

    prs_created: int = FieldInfo(alias="prsCreated")

    tembo_contribution: float = FieldInfo(alias="temboContribution")


class DataSummaryChanges(BaseModel):
    prs_created: Optional[float] = FieldInfo(alias="prsCreated", default=None)

    prs_merged: Optional[float] = FieldInfo(alias="prsMerged", default=None)

    tasks_completed: Optional[float] = FieldInfo(alias="tasksCompleted", default=None)

    tembo_contribution: Optional[float] = FieldInfo(alias="temboContribution", default=None)


class DataSummary(BaseModel):
    tasks_completed: int = FieldInfo(alias="tasksCompleted")

    prs_created: int = FieldInfo(alias="prsCreated")

    prs_merged: int = FieldInfo(alias="prsMerged")

    model_cost_per_pr_usd: Optional[float] = FieldInfo(alias="modelCostPerPrUsd", default=None)
    """Recorded model cost plus VM compute fees in USD across the organization divided by Tembo-created PRs in the selected sync window. Excludes subscription fees and inference billing markup. Null when there are no PRs or no recorded costs."""

    tembo_contribution: float = FieldInfo(alias="temboContribution")

    changes: DataSummaryChanges
    """Recent period compared with the previous one. Null when the previous period has no baseline, such as when the organization joined during it."""


class Data(BaseModel):
    range: Literal["1d", "7d", "30d", "1y"]

    summary: DataSummary

    time_series: List[DataTimeSeries] = FieldInfo(alias="timeSeries")


class InsightRetrieveResponse(BaseModel):
    id: Optional[str] = None

    status: Optional[Literal["syncing", "ready", "failed"]] = None

    range_start: Optional[datetime] = FieldInfo(alias="rangeStart", default=None)

    range_end: Optional[datetime] = FieldInfo(alias="rangeEnd", default=None)

    last_synced_at: Optional[datetime] = FieldInfo(alias="lastSyncedAt", default=None)

    enabled: bool

    data: Optional[Data] = None
