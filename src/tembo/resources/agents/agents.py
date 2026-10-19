# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Literal
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from .triggers import (
    TriggersResource,
    AsyncTriggersResource,
    TriggersResourceWithRawResponse,
    AsyncTriggersResourceWithRawResponse,
    TriggersResourceWithStreamingResponse,
    AsyncTriggersResourceWithStreamingResponse,
)
from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from .content_revisions import (
    ContentRevisionsResource,
    AsyncContentRevisionsResource,
    ContentRevisionsResourceWithRawResponse,
    AsyncContentRevisionsResourceWithRawResponse,
    ContentRevisionsResourceWithStreamingResponse,
    AsyncContentRevisionsResourceWithStreamingResponse,
)
from ...types.agent_list_response import AgentListResponse
from ...types import agent_list_params, agent_create_params, agent_update_params
from ...types.agent_create_response import AgentCreateResponse
from ...types.tip_tap_document_param import TipTapDocumentParam
from ...types.agent_options_input_param import AgentOptionsInputParam
from ...types.agent_retrieve_response import AgentRetrieveResponse
from ...types.agent_update_response import AgentUpdateResponse
from ...types.agent_state import AgentState
from ...types.agent_delete_response import AgentDeleteResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def schedules(self) -> SchedulesResource:
        return SchedulesResource(self._client)

    @cached_property
    def triggers(self) -> TriggersResource:
        return TriggersResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def content_revisions(self) -> ContentRevisionsResource:
        return ContentRevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        ids: str | Omit = omit,
        search: str | Omit = omit,
        archived: bool | Omit = omit,
        sort: Literal["latestRun", "runCount"] | Omit = omit,
        status: str | Omit = omit,
        integration: str | Omit = omit,
        author: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        List agents available in your organization, with optional search, status, integration, and author filters.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            ids: Filter by agent IDs, supplied as a comma-separated list.
            search: Search agent names.
            archived: true lists archived agents; false or omitted lists unarchived agents. Use this to find agents to restore.
            sort: Sort agents by latest run or run count.
            status: Filter by enabled (running) or paused status, supplied as a comma-separated list; this is not individual run execution status.
            integration: Filter by integration provider types, supplied as a comma-separated list.
            author: Filter by creator user IDs, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentListResponse: List agents

        Example:
            ```python
            agent = client.agents.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "ids": ids,
                        "search": search,
                        "archived": archived,
                        "sort": sort,
                        "status": status,
                        "integration": integration,
                        "author": author,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def create(
        self,
        *,
        name: str | Omit = omit,
        instructions: TipTapDocumentParam | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        agent: str | Omit = omit,
        agent_options: AgentOptionsInputParam | Omit = omit,
        sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]]
        | Omit = omit,
        project_id: Optional[Union[str, Literal["tembo"]]] | Omit = omit,
        artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]]
        | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        triggers: Iterable[agent_create_params.Trigger] | Omit = omit,
        schedules: Iterable[agent_create_params.Schedule] | Omit = omit,
        template_name: Literal[
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
        | Omit = omit,
        source_agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """
        Create an agent from instructions, a template, or another agent. sourceAgentId cannot be combined with other fields. Template creation accepts only templateName, name, and triggers; creation from scratch requires name.

        Args:
            name: Agent display name. Required when creating from scratch.
            instructions: Instructions for the agent as a rich-text document. Mentions can reference integrations used by the agent.
            mcp_servers: MCP server or connection IDs available to agent runs.
            agent: Coding agent and model key used for runs. Omit to use the default.
            agent_options: Agent-specific runtime options, such as reasoning effort.
            sandbox_size: Workspace VM size used for agent runs.
            project_id: Project environment used for agent runs.
            artifact_type: Artifact type produced by this agent.
            repository_ids: Repository IDs available to agent runs.
            triggers: Integration events that automatically start agent runs.
            schedules: Recurring cron schedules that automatically start agent runs.
            template_name: Create from a template discovered with listAgentTemplates. Only name and triggers may also be supplied.
            source_agent_id: Duplicate an existing agent. Must be the only field; cannot be combined with templateName or overrides.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentCreateResponse: Create an agent

        Example:
            ```python
            agent = client.agents.create()
            ```
        """
        return self._post(
            "/v1/agents",
            body=maybe_transform(
                {
                    "name": name,
                    "instructions": instructions,
                    "mcp_servers": mcp_servers,
                    "agent": agent,
                    "agent_options": agent_options,
                    "sandbox_size": sandbox_size,
                    "project_id": project_id,
                    "artifact_type": artifact_type,
                    "repository_ids": repository_ids,
                    "triggers": triggers,
                    "schedules": schedules,
                    "template_name": template_name,
                    "source_agent_id": source_agent_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        Retrieve an agent and its configuration, repository associations, and run summary.

        Args:
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentRetrieveResponse: Retrieve an agent

        Example:
            ```python
            agent = client.agents.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agentId}", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        expected_updated_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        key: Optional[str] | Omit = omit,
        instructions: Optional[TipTapDocumentParam] | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        agent: Optional[str] | Omit = omit,
        agent_options: AgentOptionsInputParam | Omit = omit,
        user_state: AgentState | Omit = omit,
        sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]]
        | Omit = omit,
        project_id: Optional[Union[str, Literal["tembo"]]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        script: Optional[str] | Omit = omit,
        artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]]
        | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateResponse:
        """
        Update agent instructions, model, workspace, repositories, or persistent state; enable or pause the agent; archive or restore it. enabled and archived also control its schedules and triggers. Supply expectedUpdatedAt to reject concurrent changes.

        Args:
            agent_id: Path parameter.
            expected_updated_at: Value of updatedAt from the last retrieved agent. A concurrent change causes a conflict instead of overwriting newer changes.
            name: Rename the agent.
            key: Change the agent lookup key, or null to clear it.
            instructions: Replace the agent instruction document, or null to clear it.
            mcp_servers: Replace the MCP server or connection IDs. An empty array clears the selection.
            agent: Change the coding agent and model key. Null clears the override.
            agent_options: Change agent-specific runtime options, such as reasoning effort.
            user_state: Replace the user-managed persistent agent state.
            sandbox_size: Change the workspace VM size. Null clears the override.
            project_id: Change the project environment for runs. Null clears the override.
            template_id: Change the associated agent template identifier, or null to clear it.
            script: Replace the agent script, or null to clear it.
            artifact_type: Change the artifact type produced by the agent, or null to clear it.
            repository_ids: Replace repository associations. An empty array removes all associations.
            enabled: Enable or pause the agent and its schedules and triggers. Archived agents remain paused until restored.
            archived: Archive with true or restore with false. Archiving disables schedules and triggers; restoring follows the agent enabled state.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentUpdateResponse: Update an agent

        Example:
            ```python
            agent = client.agents.update(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            path_template("/v1/agents/{agentId}", **{"agentId": agent_id}),
            body=maybe_transform(
                {
                    "expected_updated_at": expected_updated_at,
                    "name": name,
                    "key": key,
                    "instructions": instructions,
                    "mcp_servers": mcp_servers,
                    "agent": agent,
                    "agent_options": agent_options,
                    "user_state": user_state,
                    "sandbox_size": sandbox_size,
                    "project_id": project_id,
                    "template_id": template_id,
                    "script": script,
                    "artifact_type": artifact_type,
                    "repository_ids": repository_ids,
                    "enabled": enabled,
                    "archived": archived,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDeleteResponse:
        """
        Archive an agent and disable its scheduled and triggered jobs without permanently deleting it. Restore with updateAgent and archived=false.

        Args:
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentDeleteResponse: Delete an agent

        Example:
            ```python
            agent = client.agents.delete(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            path_template("/v1/agents/{agentId}", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        return AsyncSchedulesResource(self._client)

    @cached_property
    def triggers(self) -> AsyncTriggersResource:
        return AsyncTriggersResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def content_revisions(self) -> AsyncContentRevisionsResource:
        return AsyncContentRevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        ids: str | Omit = omit,
        search: str | Omit = omit,
        archived: bool | Omit = omit,
        sort: Literal["latestRun", "runCount"] | Omit = omit,
        status: str | Omit = omit,
        integration: str | Omit = omit,
        author: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        List agents available in your organization, with optional search, status, integration, and author filters.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            ids: Filter by agent IDs, supplied as a comma-separated list.
            search: Search agent names.
            archived: true lists archived agents; false or omitted lists unarchived agents. Use this to find agents to restore.
            sort: Sort agents by latest run or run count.
            status: Filter by enabled (running) or paused status, supplied as a comma-separated list; this is not individual run execution status.
            integration: Filter by integration provider types, supplied as a comma-separated list.
            author: Filter by creator user IDs, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentListResponse: List agents

        Example:
            ```python
            agent = await client.agents.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "ids": ids,
                        "search": search,
                        "archived": archived,
                        "sort": sort,
                        "status": status,
                        "integration": integration,
                        "author": author,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def create(
        self,
        *,
        name: str | Omit = omit,
        instructions: TipTapDocumentParam | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        agent: str | Omit = omit,
        agent_options: AgentOptionsInputParam | Omit = omit,
        sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]]
        | Omit = omit,
        project_id: Optional[Union[str, Literal["tembo"]]] | Omit = omit,
        artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]]
        | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        triggers: Iterable[agent_create_params.Trigger] | Omit = omit,
        schedules: Iterable[agent_create_params.Schedule] | Omit = omit,
        template_name: Literal[
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
        | Omit = omit,
        source_agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateResponse:
        """
        Create an agent from instructions, a template, or another agent. sourceAgentId cannot be combined with other fields. Template creation accepts only templateName, name, and triggers; creation from scratch requires name.

        Args:
            name: Agent display name. Required when creating from scratch.
            instructions: Instructions for the agent as a rich-text document. Mentions can reference integrations used by the agent.
            mcp_servers: MCP server or connection IDs available to agent runs.
            agent: Coding agent and model key used for runs. Omit to use the default.
            agent_options: Agent-specific runtime options, such as reasoning effort.
            sandbox_size: Workspace VM size used for agent runs.
            project_id: Project environment used for agent runs.
            artifact_type: Artifact type produced by this agent.
            repository_ids: Repository IDs available to agent runs.
            triggers: Integration events that automatically start agent runs.
            schedules: Recurring cron schedules that automatically start agent runs.
            template_name: Create from a template discovered with listAgentTemplates. Only name and triggers may also be supplied.
            source_agent_id: Duplicate an existing agent. Must be the only field; cannot be combined with templateName or overrides.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentCreateResponse: Create an agent

        Example:
            ```python
            agent = await client.agents.create()
            ```
        """
        return await self._post(
            "/v1/agents",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "instructions": instructions,
                    "mcp_servers": mcp_servers,
                    "agent": agent,
                    "agent_options": agent_options,
                    "sandbox_size": sandbox_size,
                    "project_id": project_id,
                    "artifact_type": artifact_type,
                    "repository_ids": repository_ids,
                    "triggers": triggers,
                    "schedules": schedules,
                    "template_name": template_name,
                    "source_agent_id": source_agent_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        Retrieve an agent and its configuration, repository associations, and run summary.

        Args:
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentRetrieveResponse: Retrieve an agent

        Example:
            ```python
            agent = await client.agents.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agentId}", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        expected_updated_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        key: Optional[str] | Omit = omit,
        instructions: Optional[TipTapDocumentParam] | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        agent: Optional[str] | Omit = omit,
        agent_options: AgentOptionsInputParam | Omit = omit,
        user_state: AgentState | Omit = omit,
        sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]]
        | Omit = omit,
        project_id: Optional[Union[str, Literal["tembo"]]] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        script: Optional[str] | Omit = omit,
        artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]]
        | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateResponse:
        """
        Update agent instructions, model, workspace, repositories, or persistent state; enable or pause the agent; archive or restore it. enabled and archived also control its schedules and triggers. Supply expectedUpdatedAt to reject concurrent changes.

        Args:
            agent_id: Path parameter.
            expected_updated_at: Value of updatedAt from the last retrieved agent. A concurrent change causes a conflict instead of overwriting newer changes.
            name: Rename the agent.
            key: Change the agent lookup key, or null to clear it.
            instructions: Replace the agent instruction document, or null to clear it.
            mcp_servers: Replace the MCP server or connection IDs. An empty array clears the selection.
            agent: Change the coding agent and model key. Null clears the override.
            agent_options: Change agent-specific runtime options, such as reasoning effort.
            user_state: Replace the user-managed persistent agent state.
            sandbox_size: Change the workspace VM size. Null clears the override.
            project_id: Change the project environment for runs. Null clears the override.
            template_id: Change the associated agent template identifier, or null to clear it.
            script: Replace the agent script, or null to clear it.
            artifact_type: Change the artifact type produced by the agent, or null to clear it.
            repository_ids: Replace repository associations. An empty array removes all associations.
            enabled: Enable or pause the agent and its schedules and triggers. Archived agents remain paused until restored.
            archived: Archive with true or restore with false. Archiving disables schedules and triggers; restoring follows the agent enabled state.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentUpdateResponse: Update an agent

        Example:
            ```python
            agent = await client.agents.update(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            path_template("/v1/agents/{agentId}", **{"agentId": agent_id}),
            body=await async_maybe_transform(
                {
                    "expected_updated_at": expected_updated_at,
                    "name": name,
                    "key": key,
                    "instructions": instructions,
                    "mcp_servers": mcp_servers,
                    "agent": agent,
                    "agent_options": agent_options,
                    "user_state": user_state,
                    "sandbox_size": sandbox_size,
                    "project_id": project_id,
                    "template_id": template_id,
                    "script": script,
                    "artifact_type": artifact_type,
                    "repository_ids": repository_ids,
                    "enabled": enabled,
                    "archived": archived,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDeleteResponse:
        """
        Archive an agent and disable its scheduled and triggered jobs without permanently deleting it. Restore with updateAgent and archived=false.

        Args:
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentDeleteResponse: Delete an agent

        Example:
            ```python
            agent = await client.agents.delete(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            path_template("/v1/agents/{agentId}", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._agents.templates)

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        return SchedulesResourceWithRawResponse(self._agents.schedules)

    @cached_property
    def triggers(self) -> TriggersResourceWithRawResponse:
        return TriggersResourceWithRawResponse(self._agents.triggers)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._agents.runs)

    @cached_property
    def content_revisions(self) -> ContentRevisionsResourceWithRawResponse:
        return ContentRevisionsResourceWithRawResponse(self._agents.content_revisions)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._agents.templates)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        return AsyncSchedulesResourceWithRawResponse(self._agents.schedules)

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithRawResponse:
        return AsyncTriggersResourceWithRawResponse(self._agents.triggers)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._agents.runs)

    @cached_property
    def content_revisions(self) -> AsyncContentRevisionsResourceWithRawResponse:
        return AsyncContentRevisionsResourceWithRawResponse(self._agents.content_revisions)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._agents.templates)

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        return SchedulesResourceWithStreamingResponse(self._agents.schedules)

    @cached_property
    def triggers(self) -> TriggersResourceWithStreamingResponse:
        return TriggersResourceWithStreamingResponse(self._agents.triggers)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._agents.runs)

    @cached_property
    def content_revisions(self) -> ContentRevisionsResourceWithStreamingResponse:
        return ContentRevisionsResourceWithStreamingResponse(self._agents.content_revisions)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._agents.templates)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        return AsyncSchedulesResourceWithStreamingResponse(self._agents.schedules)

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithStreamingResponse:
        return AsyncTriggersResourceWithStreamingResponse(self._agents.triggers)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._agents.runs)

    @cached_property
    def content_revisions(self) -> AsyncContentRevisionsResourceWithStreamingResponse:
        return AsyncContentRevisionsResourceWithStreamingResponse(self._agents.content_revisions)
