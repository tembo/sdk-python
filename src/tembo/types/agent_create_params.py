# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional, Union
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .agent_options_input_param import AgentOptionsInputParam

__all__ = ["AgentCreateParams", "Trigger", "Schedule"]


class AgentCreateParams(TypedDict, total=False):
    name: str
    """Agent display name. Required when creating from scratch."""

    instructions: "TipTapDocumentParam"
    """Instructions for the agent as a rich-text document. Mentions can reference integrations used by the agent."""

    mcp_servers: Annotated[SequenceNotStr[str], PropertyInfo(alias="mcpServers")]
    """MCP server or connection IDs available to agent runs."""

    agent: str
    """Coding agent and model key used for runs. Omit to use the default."""

    agent_options: Annotated[AgentOptionsInputParam, PropertyInfo(alias="agentOptions")]
    """Agent-specific runtime options, such as reasoning effort."""

    sandbox_size: Annotated[
        Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]],
        PropertyInfo(alias="sandboxSize"),
    ]
    """Workspace VM size used for agent runs."""

    project_id: Annotated[Optional[Union[str, Literal["tembo"]]], PropertyInfo(alias="projectId")]
    """Project environment used for agent runs."""

    artifact_type: Annotated[
        Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]],
        PropertyInfo(alias="artifactType"),
    ]
    """Artifact type produced by this agent."""

    repository_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="repositoryIds")]
    """Repository IDs available to agent runs."""

    triggers: Iterable[Trigger]
    """Integration events that automatically start agent runs."""

    schedules: Iterable[Schedule]
    """Recurring cron schedules that automatically start agent runs."""

    template_name: Annotated[
        Literal[
            "addTestCoverage",
            "addTestCoverageFromJira",
            "autoAgentsMdMaintainer",
            "autoDocsMaintainer",
            "publicApiReleaseMaintainer",
            "commitOfTheDay",
            "customerHealthMonitoringAgent",
            "deadCodeCleanup",
            "dependencySweepAgent",
            "autoFixCi",
            "autoFixSentryError",
            "dailySlackChangelog",
            "duplicateTicketDetector",
            "fixBugsReportedInSlack",
            "enrichGithubIssue",
            "enrichJiraIssue",
            "enrichLinearIssue",
            "hubspotCallTaskCoach",
            "hubspotEmailTaskDrafter",
            "hubspotTicketToLinearBug",
            "prDescription",
            "prReview",
            "pagePerformanceReport",
            "prioritizeSentry",
            "productFaqAgent",
            "productFinanceAgent",
            "queryPerformanceReport",
            "securityFixFromJira",
            "securityScan",
            "skillProgressionMap",
            "slackChannelListener",
            "slopCop",
            "testAudit",
            "staleCodeComments",
            "stalePullRequestNotifier",
            "summarizeChangesDaily",
            "triageNewJiraBug",
        ],
        PropertyInfo(alias="templateName"),
    ]
    """Create from a template discovered with listAgentTemplates. Only name and triggers may also be supplied."""

    source_agent_id: Annotated[str, PropertyInfo(alias="sourceAgentId")]
    """Duplicate an existing agent. Must be the only field; cannot be combined with templateName or overrides."""


class Schedule(TypedDict, total=False):
    cron: Required[str]
    """Cron expression for recurring agent runs. Agent enabled and archived state controls whether the schedule runs."""


class Trigger(TypedDict, total=False):
    name: Required[str]
    """Integration event name. Use listIntegrationTriggers to discover supported triggers."""

    integration_type: Annotated[str, PropertyInfo(alias="integrationType")]
    """Provider type for the trigger, such as github or slack."""

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]
    """Connected integration that supplies trigger events."""

    filters: "TriggerFiltersParam"
    """Event-specific trigger filters. Use retrieveIntegrationTrigger and listIntegrationTriggerFilterOptions to discover supported fields and values."""


from .tip_tap_document_param import TipTapDocumentParam
from .agents.trigger_filters_param import TriggerFiltersParam
from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_code_block_node_param import TipTapCodeBlockNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
