# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Union
from typing_extensions import Literal, overload

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform, required_args
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organizations.setting_retrieve_response import SettingRetrieveResponse
from ...types.organizations.setting_update_response import SettingUpdateResponse
from ...types.organizations import setting_update_params, setting_validate_credentials_params
from ...types.organizations.setting_validate_credentials_response import SettingValidateCredentialsResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingRetrieveResponse:
        """
        Retrieve effective organization settings, including defaults for settings that have not been configured.

        Args:
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingRetrieveResponse: Retrieve organization settings

        Example:
            ```python
            setting = client.organizations.settings.retrieve(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/v1/organizations/{organizationId}/settings", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    def update(
        self,
        organization_id: str,
        *,
        amp_api_key: str | Omit = omit,
        anthropic_api_key: str | Omit = omit,
        aws_bedrock_access_key_id: str | Omit = omit,
        aws_bedrock_region: str | Omit = omit,
        aws_bedrock_secret_access_key: str | Omit = omit,
        clone_depth: int | Omit = omit,
        commit_instructions: str | Omit = omit,
        cursor_api_key: str | Omit = omit,
        custom_system_prompt: str | Omit = omit,
        default_agent: str | Omit = omit,
        default_keep_alive_minutes: int | Omit = omit,
        default_sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"] | Omit = omit,
        delete_branch_when_pr_closed: bool | Omit = omit,
        draft_prs: bool | Omit = omit,
        enable_coderabbit_bot: bool | Omit = omit,
        enable_cursor_bot: bool | Omit = omit,
        enable_gemini_code_assist_bot: bool | Omit = omit,
        enable_github_actions_bot: bool | Omit = omit,
        enable_graphite_bot: bool | Omit = omit,
        enable_greptile_bot: bool | Omit = omit,
        experimental_mcp: bool | Omit = omit,
        feature_mention_author: bool | Omit = omit,
        gcp_vertex_ai_location: str | Omit = omit,
        gcp_vertex_ai_project: str | Omit = omit,
        gcp_vertex_ai_service_account_json: str | Omit = omit,
        kernel_api_key: str | Omit = omit,
        max_bot_reviews: int | Omit = omit,
        max_solutions: int | Omit = omit,
        openai_api_key: str | Omit = omit,
        xai_api_key: str | Omit = omit,
        openrouter_api_key: str | Omit = omit,
        pg_stat_statements_reset_frequency: str | Omit = omit,
        pm_system_prompt: str | Omit = omit,
        pr_title_instructions: str | Omit = omit,
        pull_request_insights_enabled: bool | Omit = omit,
        should_sign_commits: bool | Omit = omit,
        slack_review_on_tembo: bool | Omit = omit,
        slow_query_threshold_ms: float | Omit = omit,
        ssh_public_keys: str | Omit = omit,
        weekly_report_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateResponse:
        """
        Configure organization defaults for agent/model, VM size and keep-alive; inference credentials; agent prompts and commit/PR instructions; bot feedback, signing, reports, and insights. Only supplied settings are changed.

        Args:
            organization_id: Path parameter.
            amp_api_key: API key for Amp agent access.
            anthropic_api_key: Anthropic API key for organization-provided inference.
            aws_bedrock_access_key_id: AWS access key ID for Bedrock inference.
            aws_bedrock_region: AWS region for Bedrock inference.
            aws_bedrock_secret_access_key: AWS secret access key for Bedrock inference.
            clone_depth: Git clone history depth used for repositories.
            commit_instructions: Organization instructions for agent commit messages.
            cursor_api_key: API key for Cursor agent access.
            custom_system_prompt: Custom system instructions supplied to organization agents.
            default_agent: Default coding agent and model key for the organization.
            default_keep_alive_minutes: Default VM keep-alive duration in minutes. 0 preserves built-in per-source durations.
            default_sandbox_size: Default VM size for organization sessions.
            delete_branch_when_pr_closed: Delete agent-created branches when their pull requests close.
            draft_prs: Create agent pull requests as drafts by default.
            enable_coderabbit_bot: Enable handling of CodeRabbit bot feedback.
            enable_cursor_bot: Enable handling of Cursor bot feedback.
            enable_gemini_code_assist_bot: Enable handling of Gemini Code Assist bot feedback.
            enable_github_actions_bot: Enable handling of GitHub Actions bot feedback.
            enable_graphite_bot: Enable handling of Graphite bot feedback.
            enable_greptile_bot: Enable handling of Greptile bot feedback.
            experimental_mcp: Enable experimental MCP features for the organization.
            feature_mention_author: Enable mentioning the author in supported integration responses.
            gcp_vertex_ai_location: Google Cloud location for Vertex AI inference.
            gcp_vertex_ai_project: Google Cloud project for Vertex AI inference.
            gcp_vertex_ai_service_account_json: Service-account JSON credentials for Vertex AI inference.
            kernel_api_key: API key for Kernel browser access.
            max_bot_reviews: Maximum number of bot review iterations.
            max_solutions: Maximum number of generated solutions.
            openai_api_key: OpenAI API key for organization-provided inference.
            xai_api_key: xAI API key for organization-provided inference.
            openrouter_api_key: OpenRouter API key for organization-provided inference.
            pg_stat_statements_reset_frequency: Reset frequency for PostgreSQL pg_stat_statements collection.
            pm_system_prompt: Custom system instructions for the project-management agent.
            pr_title_instructions: Organization instructions for agent pull request titles.
            pull_request_insights_enabled: Enable or disable pull request contribution insight collection.
            should_sign_commits: Sign agent-created commits when signing credentials are configured.
            slack_review_on_tembo: Use Tembo review links in Slack review notifications.
            slow_query_threshold_ms: Threshold in milliseconds for identifying slow database queries.
            ssh_public_keys: SSH public keys authorized for organization workspace access.
            weekly_report_enabled: Enable or disable the organization weekly report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingUpdateResponse: Update organization settings

        Example:
            ```python
            setting = client.organizations.settings.update(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._patch(
            path_template("/v1/organizations/{organizationId}/settings", **{"organizationId": organization_id}),
            body=maybe_transform(
                {
                    "amp_api_key": amp_api_key,
                    "anthropic_api_key": anthropic_api_key,
                    "aws_bedrock_access_key_id": aws_bedrock_access_key_id,
                    "aws_bedrock_region": aws_bedrock_region,
                    "aws_bedrock_secret_access_key": aws_bedrock_secret_access_key,
                    "clone_depth": clone_depth,
                    "commit_instructions": commit_instructions,
                    "cursor_api_key": cursor_api_key,
                    "custom_system_prompt": custom_system_prompt,
                    "default_agent": default_agent,
                    "default_keep_alive_minutes": default_keep_alive_minutes,
                    "default_sandbox_size": default_sandbox_size,
                    "delete_branch_when_pr_closed": delete_branch_when_pr_closed,
                    "draft_prs": draft_prs,
                    "enable_coderabbit_bot": enable_coderabbit_bot,
                    "enable_cursor_bot": enable_cursor_bot,
                    "enable_gemini_code_assist_bot": enable_gemini_code_assist_bot,
                    "enable_github_actions_bot": enable_github_actions_bot,
                    "enable_graphite_bot": enable_graphite_bot,
                    "enable_greptile_bot": enable_greptile_bot,
                    "experimental_mcp": experimental_mcp,
                    "feature_mention_author": feature_mention_author,
                    "gcp_vertex_ai_location": gcp_vertex_ai_location,
                    "gcp_vertex_ai_project": gcp_vertex_ai_project,
                    "gcp_vertex_ai_service_account_json": gcp_vertex_ai_service_account_json,
                    "kernel_api_key": kernel_api_key,
                    "max_bot_reviews": max_bot_reviews,
                    "max_solutions": max_solutions,
                    "openai_api_key": openai_api_key,
                    "xai_api_key": xai_api_key,
                    "openrouter_api_key": openrouter_api_key,
                    "pg_stat_statements_reset_frequency": pg_stat_statements_reset_frequency,
                    "pm_system_prompt": pm_system_prompt,
                    "pr_title_instructions": pr_title_instructions,
                    "pull_request_insights_enabled": pull_request_insights_enabled,
                    "should_sign_commits": should_sign_commits,
                    "slack_review_on_tembo": slack_review_on_tembo,
                    "slow_query_threshold_ms": slow_query_threshold_ms,
                    "ssh_public_keys": ssh_public_keys,
                    "weekly_report_enabled": weekly_report_enabled,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateResponse,
        )

    @overload
    def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["anthropic"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["openai"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["xai"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["openrouter"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["aws-bedrock"],
        access_key_id: str,
        secret_access_key: str,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["gcp-vertex-ai"],
        service_account_json: str,
        project: str,
        location: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @required_args(
        ["api_key", "provider"],
        ["access_key_id", "provider", "region", "secret_access_key"],
        ["location", "project", "provider", "service_account_json"],
    )
    def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Union[
            Literal["anthropic"],
            Literal["openai"],
            Literal["xai"],
            Literal["openrouter"],
            Literal["aws-bedrock"],
            Literal["gcp-vertex-ai"],
        ],
        api_key: str | Omit = omit,
        access_key_id: str | Omit = omit,
        secret_access_key: str | Omit = omit,
        region: str | Omit = omit,
        service_account_json: str | Omit = omit,
        project: str | Omit = omit,
        location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse:
        """
        Validate supplied inference provider credentials for an organization without saving them. The provider must be available on the organization’s plan.

        Args:
            organization_id: Path parameter.
            provider: Validate Anthropic API credentials without saving them.
            api_key: The Anthropic API key.
            access_key_id: The AWS access key ID.
            secret_access_key: The AWS secret access key.
            region: The AWS region.
            service_account_json: The GCP service account JSON.
            project: The GCP project ID.
            location: The Vertex AI location.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingValidateCredentialsResponse: Validate organization provider credentials

        Example:
            ```python
            setting = client.organizations.settings.validate_credentials(
                organization_id="organizationId",
                provider="anthropic",
                api_key="",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template(
                "/v1/organizations/{organizationId}/settings/validate-credentials",
                **{"organizationId": organization_id},
            ),
            body=maybe_transform(
                {
                    "provider": provider,
                    "api_key": api_key,
                    "access_key_id": access_key_id,
                    "secret_access_key": secret_access_key,
                    "region": region,
                    "service_account_json": service_account_json,
                    "project": project,
                    "location": location,
                },
                setting_validate_credentials_params.SettingValidateCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingValidateCredentialsResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingRetrieveResponse:
        """
        Retrieve effective organization settings, including defaults for settings that have not been configured.

        Args:
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingRetrieveResponse: Retrieve organization settings

        Example:
            ```python
            setting = await client.organizations.settings.retrieve(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/v1/organizations/{organizationId}/settings", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    async def update(
        self,
        organization_id: str,
        *,
        amp_api_key: str | Omit = omit,
        anthropic_api_key: str | Omit = omit,
        aws_bedrock_access_key_id: str | Omit = omit,
        aws_bedrock_region: str | Omit = omit,
        aws_bedrock_secret_access_key: str | Omit = omit,
        clone_depth: int | Omit = omit,
        commit_instructions: str | Omit = omit,
        cursor_api_key: str | Omit = omit,
        custom_system_prompt: str | Omit = omit,
        default_agent: str | Omit = omit,
        default_keep_alive_minutes: int | Omit = omit,
        default_sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"] | Omit = omit,
        delete_branch_when_pr_closed: bool | Omit = omit,
        draft_prs: bool | Omit = omit,
        enable_coderabbit_bot: bool | Omit = omit,
        enable_cursor_bot: bool | Omit = omit,
        enable_gemini_code_assist_bot: bool | Omit = omit,
        enable_github_actions_bot: bool | Omit = omit,
        enable_graphite_bot: bool | Omit = omit,
        enable_greptile_bot: bool | Omit = omit,
        experimental_mcp: bool | Omit = omit,
        feature_mention_author: bool | Omit = omit,
        gcp_vertex_ai_location: str | Omit = omit,
        gcp_vertex_ai_project: str | Omit = omit,
        gcp_vertex_ai_service_account_json: str | Omit = omit,
        kernel_api_key: str | Omit = omit,
        max_bot_reviews: int | Omit = omit,
        max_solutions: int | Omit = omit,
        openai_api_key: str | Omit = omit,
        xai_api_key: str | Omit = omit,
        openrouter_api_key: str | Omit = omit,
        pg_stat_statements_reset_frequency: str | Omit = omit,
        pm_system_prompt: str | Omit = omit,
        pr_title_instructions: str | Omit = omit,
        pull_request_insights_enabled: bool | Omit = omit,
        should_sign_commits: bool | Omit = omit,
        slack_review_on_tembo: bool | Omit = omit,
        slow_query_threshold_ms: float | Omit = omit,
        ssh_public_keys: str | Omit = omit,
        weekly_report_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateResponse:
        """
        Configure organization defaults for agent/model, VM size and keep-alive; inference credentials; agent prompts and commit/PR instructions; bot feedback, signing, reports, and insights. Only supplied settings are changed.

        Args:
            organization_id: Path parameter.
            amp_api_key: API key for Amp agent access.
            anthropic_api_key: Anthropic API key for organization-provided inference.
            aws_bedrock_access_key_id: AWS access key ID for Bedrock inference.
            aws_bedrock_region: AWS region for Bedrock inference.
            aws_bedrock_secret_access_key: AWS secret access key for Bedrock inference.
            clone_depth: Git clone history depth used for repositories.
            commit_instructions: Organization instructions for agent commit messages.
            cursor_api_key: API key for Cursor agent access.
            custom_system_prompt: Custom system instructions supplied to organization agents.
            default_agent: Default coding agent and model key for the organization.
            default_keep_alive_minutes: Default VM keep-alive duration in minutes. 0 preserves built-in per-source durations.
            default_sandbox_size: Default VM size for organization sessions.
            delete_branch_when_pr_closed: Delete agent-created branches when their pull requests close.
            draft_prs: Create agent pull requests as drafts by default.
            enable_coderabbit_bot: Enable handling of CodeRabbit bot feedback.
            enable_cursor_bot: Enable handling of Cursor bot feedback.
            enable_gemini_code_assist_bot: Enable handling of Gemini Code Assist bot feedback.
            enable_github_actions_bot: Enable handling of GitHub Actions bot feedback.
            enable_graphite_bot: Enable handling of Graphite bot feedback.
            enable_greptile_bot: Enable handling of Greptile bot feedback.
            experimental_mcp: Enable experimental MCP features for the organization.
            feature_mention_author: Enable mentioning the author in supported integration responses.
            gcp_vertex_ai_location: Google Cloud location for Vertex AI inference.
            gcp_vertex_ai_project: Google Cloud project for Vertex AI inference.
            gcp_vertex_ai_service_account_json: Service-account JSON credentials for Vertex AI inference.
            kernel_api_key: API key for Kernel browser access.
            max_bot_reviews: Maximum number of bot review iterations.
            max_solutions: Maximum number of generated solutions.
            openai_api_key: OpenAI API key for organization-provided inference.
            xai_api_key: xAI API key for organization-provided inference.
            openrouter_api_key: OpenRouter API key for organization-provided inference.
            pg_stat_statements_reset_frequency: Reset frequency for PostgreSQL pg_stat_statements collection.
            pm_system_prompt: Custom system instructions for the project-management agent.
            pr_title_instructions: Organization instructions for agent pull request titles.
            pull_request_insights_enabled: Enable or disable pull request contribution insight collection.
            should_sign_commits: Sign agent-created commits when signing credentials are configured.
            slack_review_on_tembo: Use Tembo review links in Slack review notifications.
            slow_query_threshold_ms: Threshold in milliseconds for identifying slow database queries.
            ssh_public_keys: SSH public keys authorized for organization workspace access.
            weekly_report_enabled: Enable or disable the organization weekly report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingUpdateResponse: Update organization settings

        Example:
            ```python
            setting = await client.organizations.settings.update(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._patch(
            path_template("/v1/organizations/{organizationId}/settings", **{"organizationId": organization_id}),
            body=await async_maybe_transform(
                {
                    "amp_api_key": amp_api_key,
                    "anthropic_api_key": anthropic_api_key,
                    "aws_bedrock_access_key_id": aws_bedrock_access_key_id,
                    "aws_bedrock_region": aws_bedrock_region,
                    "aws_bedrock_secret_access_key": aws_bedrock_secret_access_key,
                    "clone_depth": clone_depth,
                    "commit_instructions": commit_instructions,
                    "cursor_api_key": cursor_api_key,
                    "custom_system_prompt": custom_system_prompt,
                    "default_agent": default_agent,
                    "default_keep_alive_minutes": default_keep_alive_minutes,
                    "default_sandbox_size": default_sandbox_size,
                    "delete_branch_when_pr_closed": delete_branch_when_pr_closed,
                    "draft_prs": draft_prs,
                    "enable_coderabbit_bot": enable_coderabbit_bot,
                    "enable_cursor_bot": enable_cursor_bot,
                    "enable_gemini_code_assist_bot": enable_gemini_code_assist_bot,
                    "enable_github_actions_bot": enable_github_actions_bot,
                    "enable_graphite_bot": enable_graphite_bot,
                    "enable_greptile_bot": enable_greptile_bot,
                    "experimental_mcp": experimental_mcp,
                    "feature_mention_author": feature_mention_author,
                    "gcp_vertex_ai_location": gcp_vertex_ai_location,
                    "gcp_vertex_ai_project": gcp_vertex_ai_project,
                    "gcp_vertex_ai_service_account_json": gcp_vertex_ai_service_account_json,
                    "kernel_api_key": kernel_api_key,
                    "max_bot_reviews": max_bot_reviews,
                    "max_solutions": max_solutions,
                    "openai_api_key": openai_api_key,
                    "xai_api_key": xai_api_key,
                    "openrouter_api_key": openrouter_api_key,
                    "pg_stat_statements_reset_frequency": pg_stat_statements_reset_frequency,
                    "pm_system_prompt": pm_system_prompt,
                    "pr_title_instructions": pr_title_instructions,
                    "pull_request_insights_enabled": pull_request_insights_enabled,
                    "should_sign_commits": should_sign_commits,
                    "slack_review_on_tembo": slack_review_on_tembo,
                    "slow_query_threshold_ms": slow_query_threshold_ms,
                    "ssh_public_keys": ssh_public_keys,
                    "weekly_report_enabled": weekly_report_enabled,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateResponse,
        )

    @overload
    async def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["anthropic"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    async def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["openai"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    async def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["xai"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    async def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["openrouter"],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    async def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["aws-bedrock"],
        access_key_id: str,
        secret_access_key: str,
        region: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @overload
    async def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Literal["gcp-vertex-ai"],
        service_account_json: str,
        project: str,
        location: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse: ...

    @required_args(
        ["api_key", "provider"],
        ["access_key_id", "provider", "region", "secret_access_key"],
        ["location", "project", "provider", "service_account_json"],
    )
    async def validate_credentials(
        self,
        organization_id: str,
        *,
        provider: Union[
            Literal["anthropic"],
            Literal["openai"],
            Literal["xai"],
            Literal["openrouter"],
            Literal["aws-bedrock"],
            Literal["gcp-vertex-ai"],
        ],
        api_key: str | Omit = omit,
        access_key_id: str | Omit = omit,
        secret_access_key: str | Omit = omit,
        region: str | Omit = omit,
        service_account_json: str | Omit = omit,
        project: str | Omit = omit,
        location: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingValidateCredentialsResponse:
        """
        Validate supplied inference provider credentials for an organization without saving them. The provider must be available on the organization’s plan.

        Args:
            organization_id: Path parameter.
            provider: Validate Anthropic API credentials without saving them.
            api_key: The Anthropic API key.
            access_key_id: The AWS access key ID.
            secret_access_key: The AWS secret access key.
            region: The AWS region.
            service_account_json: The GCP service account JSON.
            project: The GCP project ID.
            location: The Vertex AI location.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SettingValidateCredentialsResponse: Validate organization provider credentials

        Example:
            ```python
            setting = await client.organizations.settings.validate_credentials(
                organization_id="organizationId",
                provider="anthropic",
                api_key="",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template(
                "/v1/organizations/{organizationId}/settings/validate-credentials",
                **{"organizationId": organization_id},
            ),
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "api_key": api_key,
                    "access_key_id": access_key_id,
                    "secret_access_key": secret_access_key,
                    "region": region,
                    "service_account_json": service_account_json,
                    "project": project,
                    "location": location,
                },
                setting_validate_credentials_params.SettingValidateCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingValidateCredentialsResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_raw_response_wrapper(
            settings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.validate_credentials = to_raw_response_wrapper(
            settings.validate_credentials,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_raw_response_wrapper(
            settings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.validate_credentials = async_to_raw_response_wrapper(
            settings.validate_credentials,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.validate_credentials = to_streamed_response_wrapper(
            settings.validate_credentials,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.validate_credentials = async_to_streamed_response_wrapper(
            settings.validate_credentials,
        )
