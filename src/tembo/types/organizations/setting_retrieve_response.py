# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SettingRetrieveResponse", "Settings"]


class Settings(BaseModel):
    clone_depth: int = FieldInfo(alias="cloneDepth")
    """Git clone history depth used for repositories."""

    commit_instructions: str = FieldInfo(alias="commitInstructions")
    """Organization instructions for agent commit messages."""

    custom_system_prompt: str = FieldInfo(alias="customSystemPrompt")
    """Custom system instructions supplied to organization agents."""

    default_agent: str = FieldInfo(alias="defaultAgent")
    """Default coding agent and model key for the organization."""

    default_keep_alive_minutes: int = FieldInfo(alias="defaultKeepAliveMinutes")
    """Default VM keep-alive duration in minutes. 0 preserves built-in per-source durations."""

    default_sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"] = FieldInfo(
        alias="defaultSandboxSize"
    )
    """Default VM size for organization sessions."""

    delete_branch_when_pr_closed: bool = FieldInfo(alias="deleteBranchWhenPrClosed")
    """Delete agent-created branches when their pull requests close."""

    draft_prs: bool = FieldInfo(alias="draftPrs")
    """Create agent pull requests as drafts by default."""

    enable_coderabbit_bot: bool = FieldInfo(alias="enableCoderabbitBot")
    """Enable handling of CodeRabbit bot feedback."""

    enable_cursor_bot: bool = FieldInfo(alias="enableCursorBot")
    """Enable handling of Cursor bot feedback."""

    enable_gemini_code_assist_bot: bool = FieldInfo(alias="enableGeminiCodeAssistBot")
    """Enable handling of Gemini Code Assist bot feedback."""

    enable_github_actions_bot: bool = FieldInfo(alias="enableGithubActionsBot")
    """Enable handling of GitHub Actions bot feedback."""

    enable_graphite_bot: bool = FieldInfo(alias="enableGraphiteBot")
    """Enable handling of Graphite bot feedback."""

    enable_greptile_bot: bool = FieldInfo(alias="enableGreptileBot")
    """Enable handling of Greptile bot feedback."""

    experimental_mcp: bool = FieldInfo(alias="experimentalMcp")
    """Enable experimental MCP features for the organization."""

    fallback_to_api_on_subscription_limit: bool = FieldInfo(alias="fallbackToApiOnSubscriptionLimit")
    """Use the API key or Tembo inference when every connected subscription is out of usage."""

    feature_mention_author: bool = FieldInfo(alias="featureMentionAuthor")
    """Enable mentioning the author in supported integration responses."""

    max_bot_reviews: int = FieldInfo(alias="maxBotReviews")
    """Maximum number of bot review iterations."""

    max_solutions: int = FieldInfo(alias="maxSolutions")
    """Maximum number of generated solutions."""

    on_demand_max_credit_usage: float = FieldInfo(alias="onDemandMaxCreditUsage")

    pg_stat_statements_reset_frequency: str = FieldInfo(alias="pgStatStatementsResetFrequency")
    """Reset frequency for PostgreSQL pg_stat_statements collection."""

    pm_system_prompt: str = FieldInfo(alias="pmSystemPrompt")
    """Custom system instructions for the project-management agent."""

    pr_title_instructions: str = FieldInfo(alias="prTitleInstructions")
    """Organization instructions for agent pull request titles."""

    pull_request_insights_enabled: bool = FieldInfo(alias="pullRequestInsightsEnabled")
    """Enable or disable pull request contribution insight collection."""

    should_sign_commits: bool = FieldInfo(alias="shouldSignCommits")
    """Sign agent-created commits when signing credentials are configured."""

    slack_review_on_tembo: bool = FieldInfo(alias="slackReviewOnTembo")
    """Use Tembo review links in Slack review notifications."""

    slow_query_threshold_ms: float = FieldInfo(alias="slowQueryThresholdMs")
    """Threshold in milliseconds for identifying slow database queries."""

    ssh_public_keys: str = FieldInfo(alias="sshPublicKeys")
    """SSH public keys authorized for organization workspace access."""

    weekly_report_enabled: bool = FieldInfo(alias="weeklyReportEnabled")
    """Enable or disable the organization weekly report."""


class SettingRetrieveResponse(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")

    settings: Settings
