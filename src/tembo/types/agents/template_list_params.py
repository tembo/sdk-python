# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    cursor: Literal[
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
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""
