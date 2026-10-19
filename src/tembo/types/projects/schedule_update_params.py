# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    cron: str
    """Replace the recurring project build cron expression."""

    enabled: bool
    """Enable or pause scheduled project builds."""

    timezone: Optional[str]
    """Timezone for the cron schedule, or null to clear it."""
