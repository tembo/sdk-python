# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..tip_tap_document import TipTapDocument
from .trigger_filters import TriggerFilters

__all__ = ["TemplateRetrieveResponse", "Trigger"]


class Trigger(BaseModel):
    name: str

    display_name: str = FieldInfo(alias="displayName")

    integration_type: str = FieldInfo(alias="integrationType")

    filters: Optional[TriggerFilters] = None
    """Conditions that determine whether the selected integration event starts the agent. Available fields depend on the integration and event type."""


class TemplateRetrieveResponse(BaseModel):
    name: Literal[
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
    ]

    title: str

    description: str

    label: Literal["Code Review", "Productivity", "Documentation", "Reporting", "Monitoring", "Management"]

    instructions: TipTapDocument
    """Instructions for the agent as a rich-text document. Mentions can reference integrations used by the agent."""

    connected_apps: List[str] = FieldInfo(alias="connectedApps")

    artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]] = (
        FieldInfo(alias="artifactType", default=None)
    )

    agent: str

    triggers: Optional[List[Trigger]] = None

    schedules: Optional[List[str]] = None

    required_params: Optional[List[Literal["repository"]]] = FieldInfo(alias="requiredParams", default=None)
