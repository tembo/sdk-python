# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    amp_api_key: Annotated[str, PropertyInfo(alias="ampApiKey")]
    """API key for Amp agent access."""

    anthropic_api_key: Annotated[str, PropertyInfo(alias="anthropicApiKey")]
    """Anthropic API key for organization-provided inference."""

    aws_bedrock_access_key_id: Annotated[str, PropertyInfo(alias="awsBedrockAccessKeyId")]
    """AWS access key ID for Bedrock inference."""

    aws_bedrock_region: Annotated[str, PropertyInfo(alias="awsBedrockRegion")]
    """AWS region for Bedrock inference."""

    aws_bedrock_secret_access_key: Annotated[str, PropertyInfo(alias="awsBedrockSecretAccessKey")]
    """AWS secret access key for Bedrock inference."""

    clone_depth: Annotated[int, PropertyInfo(alias="cloneDepth")]
    """Git clone history depth used for repositories."""

    commit_instructions: Annotated[str, PropertyInfo(alias="commitInstructions")]
    """Organization instructions for agent commit messages."""

    cursor_api_key: Annotated[str, PropertyInfo(alias="cursorApiKey")]
    """API key for Cursor agent access."""

    custom_system_prompt: Annotated[str, PropertyInfo(alias="customSystemPrompt")]
    """Custom system instructions supplied to organization agents."""

    default_agent: Annotated[str, PropertyInfo(alias="defaultAgent")]
    """Default coding agent and model key for the organization."""

    default_keep_alive_minutes: Annotated[int, PropertyInfo(alias="defaultKeepAliveMinutes")]
    """Default VM keep-alive duration in minutes. 0 preserves built-in per-source durations."""

    default_sandbox_size: Annotated[
        Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"],
        PropertyInfo(alias="defaultSandboxSize"),
    ]
    """Default VM size for organization sessions."""

    delete_branch_when_pr_closed: Annotated[bool, PropertyInfo(alias="deleteBranchWhenPrClosed")]
    """Delete agent-created branches when their pull requests close."""

    draft_prs: Annotated[bool, PropertyInfo(alias="draftPrs")]
    """Create agent pull requests as drafts by default."""

    enable_coderabbit_bot: Annotated[bool, PropertyInfo(alias="enableCoderabbitBot")]
    """Enable handling of CodeRabbit bot feedback."""

    enable_cursor_bot: Annotated[bool, PropertyInfo(alias="enableCursorBot")]
    """Enable handling of Cursor bot feedback."""

    enable_gemini_code_assist_bot: Annotated[bool, PropertyInfo(alias="enableGeminiCodeAssistBot")]
    """Enable handling of Gemini Code Assist bot feedback."""

    enable_github_actions_bot: Annotated[bool, PropertyInfo(alias="enableGithubActionsBot")]
    """Enable handling of GitHub Actions bot feedback."""

    enable_graphite_bot: Annotated[bool, PropertyInfo(alias="enableGraphiteBot")]
    """Enable handling of Graphite bot feedback."""

    enable_greptile_bot: Annotated[bool, PropertyInfo(alias="enableGreptileBot")]
    """Enable handling of Greptile bot feedback."""

    experimental_mcp: Annotated[bool, PropertyInfo(alias="experimentalMcp")]
    """Enable experimental MCP features for the organization."""

    feature_mention_author: Annotated[bool, PropertyInfo(alias="featureMentionAuthor")]
    """Enable mentioning the author in supported integration responses."""

    gcp_vertex_ai_location: Annotated[str, PropertyInfo(alias="gcpVertexAiLocation")]
    """Google Cloud location for Vertex AI inference."""

    gcp_vertex_ai_project: Annotated[str, PropertyInfo(alias="gcpVertexAiProject")]
    """Google Cloud project for Vertex AI inference."""

    gcp_vertex_ai_service_account_json: Annotated[str, PropertyInfo(alias="gcpVertexAiServiceAccountJson")]
    """Service-account JSON credentials for Vertex AI inference."""

    kernel_api_key: Annotated[str, PropertyInfo(alias="kernelApiKey")]
    """API key for Kernel browser access."""

    max_bot_reviews: Annotated[int, PropertyInfo(alias="maxBotReviews")]
    """Maximum number of bot review iterations."""

    max_solutions: Annotated[int, PropertyInfo(alias="maxSolutions")]
    """Maximum number of generated solutions."""

    openai_api_key: Annotated[str, PropertyInfo(alias="openaiApiKey")]
    """OpenAI API key for organization-provided inference."""

    xai_api_key: Annotated[str, PropertyInfo(alias="xaiApiKey")]
    """xAI API key for organization-provided inference."""

    openrouter_api_key: Annotated[str, PropertyInfo(alias="openrouterApiKey")]
    """OpenRouter API key for organization-provided inference."""

    pg_stat_statements_reset_frequency: Annotated[str, PropertyInfo(alias="pgStatStatementsResetFrequency")]
    """Reset frequency for PostgreSQL pg_stat_statements collection."""

    pm_system_prompt: Annotated[str, PropertyInfo(alias="pmSystemPrompt")]
    """Custom system instructions for the project-management agent."""

    pr_title_instructions: Annotated[str, PropertyInfo(alias="prTitleInstructions")]
    """Organization instructions for agent pull request titles."""

    pull_request_insights_enabled: Annotated[bool, PropertyInfo(alias="pullRequestInsightsEnabled")]
    """Enable or disable pull request contribution insight collection."""

    should_sign_commits: Annotated[bool, PropertyInfo(alias="shouldSignCommits")]
    """Sign agent-created commits when signing credentials are configured."""

    slack_review_on_tembo: Annotated[bool, PropertyInfo(alias="slackReviewOnTembo")]
    """Use Tembo review links in Slack review notifications."""

    slow_query_threshold_ms: Annotated[float, PropertyInfo(alias="slowQueryThresholdMs")]
    """Threshold in milliseconds for identifying slow database queries."""

    ssh_public_keys: Annotated[str, PropertyInfo(alias="sshPublicKeys")]
    """SSH public keys authorized for organization workspace access."""

    weekly_report_enabled: Annotated[bool, PropertyInfo(alias="weeklyReportEnabled")]
    """Enable or disable the organization weekly report."""
