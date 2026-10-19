# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .trigger_filters import TriggerFilters

__all__ = ["TriggerUpdateResponse"]


class TriggerUpdateResponse(BaseModel):
    id: str

    trigger_name: str = FieldInfo(alias="triggerName")

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    agent_id: str = FieldInfo(alias="agentId")

    trigger_display_name: str = FieldInfo(alias="triggerDisplayName")

    integration_id: Optional[str] = FieldInfo(alias="integrationId", default=None)

    integration_type: Optional[str] = FieldInfo(alias="integrationType", default=None)

    filters: TriggerFilters
    """Conditions that determine whether the selected integration event starts the agent. Available fields depend on the integration and event type."""
