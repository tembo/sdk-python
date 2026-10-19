# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .tip_tap_document import TipTapDocument
from .agent_options_input import AgentOptionsInput
from .agent_state import AgentState

__all__ = ["AgentRetrieveResponse", "CodeRepository", "LastRun"]


class LastRun(BaseModel):
    id: str

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)

    status: str

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    duration_ms: int = FieldInfo(alias="durationMs")
    """Measured duration of the agent run in milliseconds."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)


class CodeRepository(BaseModel):
    id: str

    name: str

    owner: Optional[str] = None

    integration_id: str = FieldInfo(alias="integrationId")

    integration_type: str = FieldInfo(alias="integrationType")


class AgentRetrieveResponse(BaseModel):
    id: str

    name: str

    key: Optional[str] = None

    sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]] = FieldInfo(
        alias="sandboxSize", default=None
    )

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)

    content_version: int = FieldInfo(alias="contentVersion")

    script: Optional[str] = None

    artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]] = (
        FieldInfo(alias="artifactType", default=None)
    )

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    enabled_at: Optional[datetime] = FieldInfo(alias="enabledAt", default=None)

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    instructions: Optional[TipTapDocument] = None
    """Instructions for the agent as a rich-text document. Mentions can reference integrations used by the agent."""

    agent: Optional[str] = None
    """Runtime and model selection key; not the ID of an agent resource."""

    agent_options: AgentOptionsInput = FieldInfo(alias="agentOptions")
    """Execution settings for the selected agent runtime, including provider-specific options."""

    mcp_servers: List[str] = FieldInfo(alias="mcpServers")
    """Selected MCP server identifiers, including built-in server keys."""

    user_state: Optional[AgentState] = FieldInfo(alias="userState", default=None)
    """User-defined state keyed by name. Values may be any JSON value, including nested objects and arrays. No application-specific keys are required."""

    code_repositories: List[CodeRepository] = FieldInfo(alias="codeRepositories")

    last_run: Optional[LastRun] = FieldInfo(alias="lastRun", default=None)

    run_count: int = FieldInfo(alias="runCount")

    schedule_count: int = FieldInfo(alias="scheduleCount")

    trigger_count: int = FieldInfo(alias="triggerCount")

    has_paused_schedule: bool = FieldInfo(alias="hasPausedSchedule")

    has_paused_trigger: bool = FieldInfo(alias="hasPausedTrigger")

    integration_ids: List[str] = FieldInfo(alias="integrationIds")

    integration_types: List[str] = FieldInfo(alias="integrationTypes")
