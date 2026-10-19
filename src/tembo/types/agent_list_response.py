# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .tip_tap_document import TipTapDocument

__all__ = ["AgentListResponse", "Item", "ItemLastRun", "FilterOptions"]


class FilterOptions(BaseModel):
    total_count: int = FieldInfo(alias="totalCount")

    integration_types: List[str] = FieldInfo(alias="integrationTypes")


class ItemLastRun(BaseModel):
    id: str

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)

    status: str

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    duration_ms: int = FieldInfo(alias="durationMs")
    """Measured duration of the agent run in milliseconds."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)


class Item(BaseModel):
    id: str

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    name: str

    instructions: Optional[TipTapDocument] = None
    """Instructions for the agent as a rich-text document. Mentions can reference integrations used by the agent."""

    agent: Optional[str] = None
    """Runtime and model selection key; not the ID of an agent resource."""

    mcp_servers: List[str] = FieldInfo(alias="mcpServers")
    """Selected MCP server identifiers, including built-in server keys."""

    artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]] = (
        FieldInfo(alias="artifactType", default=None)
    )

    created_at: datetime = FieldInfo(alias="createdAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    last_run: Optional[ItemLastRun] = FieldInfo(alias="lastRun", default=None)

    run_count: int = FieldInfo(alias="runCount")

    schedule_count: int = FieldInfo(alias="scheduleCount")

    trigger_count: int = FieldInfo(alias="triggerCount")

    has_paused_schedule: bool = FieldInfo(alias="hasPausedSchedule")

    has_paused_trigger: bool = FieldInfo(alias="hasPausedTrigger")

    integration_ids: List[str] = FieldInfo(alias="integrationIds")

    integration_types: List[str] = FieldInfo(alias="integrationTypes")

    code_repository_count: int = FieldInfo(alias="codeRepositoryCount")


class AgentListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    filter_options: FilterOptions = FieldInfo(alias="filterOptions")
