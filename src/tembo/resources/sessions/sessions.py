# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional, Union
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
from .sources import (
    SourcesResource,
    AsyncSourcesResource,
    SourcesResourceWithRawResponse,
    AsyncSourcesResourceWithRawResponse,
    SourcesResourceWithStreamingResponse,
    AsyncSourcesResourceWithStreamingResponse,
)
from .diffs import (
    DiffsResource,
    AsyncDiffsResource,
    DiffsResourceWithRawResponse,
    AsyncDiffsResourceWithRawResponse,
    DiffsResourceWithStreamingResponse,
    AsyncDiffsResourceWithStreamingResponse,
)
from .inputs import (
    InputsResource,
    AsyncInputsResource,
    InputsResourceWithRawResponse,
    AsyncInputsResourceWithRawResponse,
    InputsResourceWithStreamingResponse,
    AsyncInputsResourceWithStreamingResponse,
)
from .queue import (
    QueueResource,
    AsyncQueueResource,
    QueueResourceWithRawResponse,
    AsyncQueueResourceWithRawResponse,
    QueueResourceWithStreamingResponse,
    AsyncQueueResourceWithStreamingResponse,
)
from .commands import (
    CommandsResource,
    AsyncCommandsResource,
    CommandsResourceWithRawResponse,
    AsyncCommandsResourceWithRawResponse,
    CommandsResourceWithStreamingResponse,
    AsyncCommandsResourceWithStreamingResponse,
)
from ...types.session_list_response import SessionListResponse
from ...types import (
    session_list_params,
    session_create_params,
    session_update_params,
    session_fork_params,
    session_stop_params,
    session_list_events_params,
)
from ...types.session_create_response import SessionCreateResponse
from ...types.session_retrieve_response import SessionRetrieveResponse
from ...types.session_update_response import SessionUpdateResponse
from ...types.session_delete_response import SessionDeleteResponse
from ...types.session_fork_response import SessionForkResponse
from ...types.session_stop_response import SessionStopResponse
from ...types.session_list_events_response import SessionListEventsResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def sources(self) -> SourcesResource:
        return SourcesResource(self._client)

    @cached_property
    def diffs(self) -> DiffsResource:
        return DiffsResource(self._client)

    @cached_property
    def inputs(self) -> InputsResource:
        return InputsResource(self._client)

    @cached_property
    def queue(self) -> QueueResource:
        return QueueResource(self._client)

    @cached_property
    def commands(self) -> CommandsResource:
        return CommandsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        agent_id: str | Omit = omit,
        created_by: SequenceNotStr[str] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        exclude_pinned: bool | Omit = omit,
        external_ids: SequenceNotStr[str] | Omit = omit,
        has_project: bool | Omit = omit,
        include_archived: bool | Omit = omit,
        include_total: bool | Omit = omit,
        participant: SequenceNotStr[str] | Omit = omit,
        pending_reviewer_keys: SequenceNotStr[str] | Omit = omit,
        project_ids: SequenceNotStr[str] | Omit = omit,
        pull_request_statuses: List[Literal["open", "merged", "closed"]] | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["lastQueuedAt", "createdAt", "updatedAt"] | Omit = omit,
        source_ids: SequenceNotStr[str] | Omit = omit,
        source_types: SequenceNotStr[str] | Omit = omit,
        state: Literal["all", "active", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListResponse:
        """
        List and search sessions, including active or archived sessions, with repository, project, creator, and source filters and cursor pagination.

        Args:
            agent_id: Filter sessions created by this automation agent.
            created_by: Filter by creator IDs, supplied as a comma-separated list.
            created_after: Only sessions created after this ISO 8601 timestamp.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            exclude_pinned: Exclude sessions pinned by the authenticated user.
            external_ids: Filter by external source IDs, supplied as a comma-separated list.
            has_project: Filter by whether a session has an assigned project.
            include_archived: Include archived sessions in the all-state view. Defaults to true; state=archived explicitly selects archived sessions.
            include_total: Include totalCount. Not supported with state=active.
            participant: Filter by participant IDs, supplied as a comma-separated list.
            pending_reviewer_keys: Filter by pending reviewer keys, supplied as a comma-separated list.
            project_ids: Filter by project IDs, supplied as a comma-separated list.
            pull_request_statuses: Filter by linked pull request statuses: open, merged, or closed, supplied as a comma-separated list.
            repository_ids: Filter by repository IDs, supplied as a comma-separated list.
            search: Search session titles, task prompts, kinds, and source names or types.
            sort_by: Timestamp used to sort sessions, newest first.
            source_ids: Filter by session source IDs, supplied as a comma-separated list.
            source_types: Filter by session source types, supplied as a comma-separated list.
            state: Select all sessions, currently active work, or archived sessions. Use archived to find sessions to restore.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionListResponse: List sessions

        Example:
            ```python
            session = client.sessions.list(
                limit=50,
                include_archived=True,
                include_total=False,
                sort_by="lastQueuedAt",
                state="all",
            )
            ```
        """
        return self._get(
            "/v1/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "created_by": created_by,
                        "created_after": created_after,
                        "cursor": cursor,
                        "limit": limit,
                        "exclude_pinned": exclude_pinned,
                        "external_ids": external_ids,
                        "has_project": has_project,
                        "include_archived": include_archived,
                        "include_total": include_total,
                        "participant": participant,
                        "pending_reviewer_keys": pending_reviewer_keys,
                        "project_ids": project_ids,
                        "pull_request_statuses": pull_request_statuses,
                        "repository_ids": repository_ids,
                        "search": search,
                        "sort_by": sort_by,
                        "source_ids": source_ids,
                        "source_types": source_types,
                        "state": state,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    def create(
        self,
        *,
        agent: str | Omit = omit,
        base_branch: Optional[str] | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"] | Omit = omit,
        target_branch: Optional[str] | Omit = omit,
        visibility: Literal["private", "public"] | Omit = omit,
        agent_options: session_create_params.AgentOptions | Omit = omit,
        branch_name: Optional[str] | Omit = omit,
        code_repository_ids: SequenceNotStr[str] | Omit = omit,
        description: str,
        id: str | Omit = omit,
        rich_content: session_create_params.RichContent | Omit = omit,
        pull_request_id: str | Omit = omit,
        queue_right_away: bool | Omit = omit,
        session_mode: Literal["chat", "terminal"] | Omit = omit,
        startup_agent: Literal["claudeCode", "codex", "opencode", "pi", "amp", "cursor"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """
        Create a session for a task. Provide the initial prompt in description and optionally configure its repositories, agent, Build (normal) or Plan (planning) mode, and private or workspace visibility.

        Args:
            agent: Agent and model key to run, such as claudeCode:claude-fable-5-1. Omit to use the default.
            base_branch: Git branch to start work from. Omit or use null for the repository default.
            mcp_servers: MCP server or connection IDs to enable for the session.
            project_id: Project environment to use for the workspace. Omit or use null for the default.
            sandbox_size: VM size for the session workspace.
            target_branch: Default target branch for pull requests created by the session.
            visibility: Session visibility: private or visible to workspace (public).
            agent_options: Agent-specific runtime options, such as reasoning effort.
            branch_name: Git branch for this session. Omit or use null to generate a branch name.
            code_repository_ids: Repository IDs to make available in the session workspace.
            description: Initial task or prompt for the session.
            id: Optional caller-supplied session UUID. Omit to generate one.
            rich_content: Optional rich-text representation of the initial task. Provide description separately.
            pull_request_id: Pull request to associate with the session. Requires richContent.
            queue_right_away: Whether to queue the initial task immediately instead of only creating the session.
            session_mode: Whether to create a chat session or a terminal session.
            startup_agent: Coding agent to start in a terminal session.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionCreateResponse: Create a session

        Example:
            ```python
            session = client.sessions.create(
                agent="claudeCode:claude-fable-5-1",
                base_branch="main",
                mcp_servers=[],
                project_id="your-project-id",
                target_branch="main",
                visibility="private",
                code_repository_ids=["123e4567-e89b-12d3-a456-426614174000"],
                description="Fix the authentication bug in the login component",
            )
            ```
        """
        return self._post(
            "/v1/sessions",
            body=maybe_transform(
                {
                    "agent": agent,
                    "base_branch": base_branch,
                    "mcp_servers": mcp_servers,
                    "project_id": project_id,
                    "sandbox_size": sandbox_size,
                    "target_branch": target_branch,
                    "visibility": visibility,
                    "agent_options": agent_options,
                    "branch_name": branch_name,
                    "code_repository_ids": code_repository_ids,
                    "description": description,
                    "id": id,
                    "rich_content": rich_content,
                    "pull_request_id": pull_request_id,
                    "queue_right_away": queue_right_away,
                    "session_mode": session_mode,
                    "startup_agent": startup_agent,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """
        Retrieve a session you have permission to access.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionRetrieveResponse: Retrieve a session

        Example:
            ```python
            session = client.sessions.retrieve(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/v1/sessions/{sessionId}", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    def update(
        self,
        session_id: str,
        *,
        agent: Optional[str] | Omit = omit,
        agent_options: session_update_params.AgentOptions | Omit = omit,
        base_branch: Optional[str] | Omit = omit,
        branch_name: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        rich_content: Optional[session_update_params.RichContent] | Omit = omit,
        level: int | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        mode: Literal["normal", "planning"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]]
        | Omit = omit,
        target_branch: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["private", "public"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionUpdateResponse:
        """
        Update a session: archive or restore it, set priority, rename it, change agent/model, switch between Build (normal) and Plan (planning) modes, configure its workspace and branches, or change visibility between private and visible to workspace (public). Archiving uses level=0; restoring archived sessions uses level=1 and does not restart work. Use pins to pin or unpin sessions.

        Args:
            session_id: Path parameter.
            agent: Change the agent and model key. Null clears the session override.
            agent_options: Change agent-specific runtime options, such as reasoning effort.
            base_branch: Change the starting Git branch. Null clears the session override.
            branch_name: Change the session Git branch name. Null clears the stored name.
            description: Replace the initial task prompt; only the session creator can change it. Use createMessage to send a follow-up task.
            rich_content: Replace the initial prompt rich-text document, or null to clear it. Only the session creator can change it.
            level: Archive or restore the session and set its priority: 0 archives and stops its VM; 1 restores without restarting work; 2–100 also keep it unarchived and set its priority level. Omit to preserve the current level.
            mcp_servers: Replace the enabled MCP server or connection IDs. An empty array clears the selection.
            mode: Switch between Build (normal) and Plan (planning) modes.
            project_id: Change the project environment used for the workspace. Null clears the session override.
            sandbox_size: Change the workspace VM size. Null clears the session override.
            target_branch: Change the default pull request target branch. Null clears the session override.
            title: Rename the session.
            visibility: Change session visibility: private or visible to workspace (public). Only the session creator can change it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionUpdateResponse: Update a session

        Example:
            ```python
            session = client.sessions.update(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            path_template("/v1/sessions/{sessionId}", **{"sessionId": session_id}),
            body=maybe_transform(
                {
                    "agent": agent,
                    "agent_options": agent_options,
                    "base_branch": base_branch,
                    "branch_name": branch_name,
                    "description": description,
                    "rich_content": rich_content,
                    "level": level,
                    "mcp_servers": mcp_servers,
                    "mode": mode,
                    "project_id": project_id,
                    "sandbox_size": sandbox_size,
                    "target_branch": target_branch,
                    "title": title,
                    "visibility": visibility,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionUpdateResponse,
        )

    def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDeleteResponse:
        """
        Archive a session and stop its VM without permanently deleting it. Equivalent to updateSession with level=0; restore with updateSession and level=1.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionDeleteResponse: Delete a session

        Example:
            ```python
            session = client.sessions.delete(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            path_template("/v1/sessions/{sessionId}", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionDeleteResponse,
        )

    def fork(
        self,
        session_id: str,
        *,
        prompt: str | Omit = omit,
        title: str | Omit = omit,
        queue_right_away: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionForkResponse:
        """
        Create an independent session from a fresh workspace snapshot, or the latest saved snapshot when stopped, without replaying messages or adding context.

        Args:
            session_id: Path parameter.
            prompt: Optional first task for the independent fork. Existing messages are not replayed.
            title: Display title for the forked session.
            queue_right_away: Start the supplied prompt immediately. Without a prompt, the fork waits for a new message.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionForkResponse: Fork a session

        Example:
            ```python
            session = client.sessions.fork(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                queue_right_away=True,
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/v1/sessions/{sessionId}/fork", **{"sessionId": session_id}),
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "title": title,
                    "queue_right_away": queue_right_away,
                },
                session_fork_params.SessionForkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionForkResponse,
        )

    def stop(
        self,
        session_id: str,
        *,
        cancel_queued: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionStopResponse:
        """
        Interrupt active session work without archiving it. Continue with the next queued message, or set cancelQueued=true to cancel pending messages too.

        Args:
            session_id: Path parameter.
            cancel_queued: Also cancel pending queued messages instead of continuing with the next queued message. Does not archive the session.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionStopResponse: Stop a session

        Example:
            ```python
            session = client.sessions.stop(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/v1/sessions/{sessionId}/stop", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cancel_queued": cancel_queued}, session_stop_params.SessionStopParams),
            ),
            cast_to=SessionStopResponse,
        )

    def list_events(
        self,
        session_id: str,
        *,
        cursor: Union[str, int] | Omit = omit,
        limit: int | Omit = omit,
        message_id: Union[str, Literal["null"]] | Omit = omit,
        after: Union[str, int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListEventsResponse:
        """
        List recorded session stream events with cursor pagination.

        Args:
            session_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            message_id: Filter by message ID, or "null" for session-level events.
            after: Only return events recorded after this event ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionListEventsResponse: List session events

        Example:
            ```python
            session = client.sessions.list_events(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/v1/sessions/{sessionId}/events", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "message_id": message_id, "after": after},
                    session_list_events_params.SessionListEventsParams,
                ),
            ),
            cast_to=SessionListEventsResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def sources(self) -> AsyncSourcesResource:
        return AsyncSourcesResource(self._client)

    @cached_property
    def diffs(self) -> AsyncDiffsResource:
        return AsyncDiffsResource(self._client)

    @cached_property
    def inputs(self) -> AsyncInputsResource:
        return AsyncInputsResource(self._client)

    @cached_property
    def queue(self) -> AsyncQueueResource:
        return AsyncQueueResource(self._client)

    @cached_property
    def commands(self) -> AsyncCommandsResource:
        return AsyncCommandsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        agent_id: str | Omit = omit,
        created_by: SequenceNotStr[str] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        exclude_pinned: bool | Omit = omit,
        external_ids: SequenceNotStr[str] | Omit = omit,
        has_project: bool | Omit = omit,
        include_archived: bool | Omit = omit,
        include_total: bool | Omit = omit,
        participant: SequenceNotStr[str] | Omit = omit,
        pending_reviewer_keys: SequenceNotStr[str] | Omit = omit,
        project_ids: SequenceNotStr[str] | Omit = omit,
        pull_request_statuses: List[Literal["open", "merged", "closed"]] | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["lastQueuedAt", "createdAt", "updatedAt"] | Omit = omit,
        source_ids: SequenceNotStr[str] | Omit = omit,
        source_types: SequenceNotStr[str] | Omit = omit,
        state: Literal["all", "active", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListResponse:
        """
        List and search sessions, including active or archived sessions, with repository, project, creator, and source filters and cursor pagination.

        Args:
            agent_id: Filter sessions created by this automation agent.
            created_by: Filter by creator IDs, supplied as a comma-separated list.
            created_after: Only sessions created after this ISO 8601 timestamp.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            exclude_pinned: Exclude sessions pinned by the authenticated user.
            external_ids: Filter by external source IDs, supplied as a comma-separated list.
            has_project: Filter by whether a session has an assigned project.
            include_archived: Include archived sessions in the all-state view. Defaults to true; state=archived explicitly selects archived sessions.
            include_total: Include totalCount. Not supported with state=active.
            participant: Filter by participant IDs, supplied as a comma-separated list.
            pending_reviewer_keys: Filter by pending reviewer keys, supplied as a comma-separated list.
            project_ids: Filter by project IDs, supplied as a comma-separated list.
            pull_request_statuses: Filter by linked pull request statuses: open, merged, or closed, supplied as a comma-separated list.
            repository_ids: Filter by repository IDs, supplied as a comma-separated list.
            search: Search session titles, task prompts, kinds, and source names or types.
            sort_by: Timestamp used to sort sessions, newest first.
            source_ids: Filter by session source IDs, supplied as a comma-separated list.
            source_types: Filter by session source types, supplied as a comma-separated list.
            state: Select all sessions, currently active work, or archived sessions. Use archived to find sessions to restore.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionListResponse: List sessions

        Example:
            ```python
            session = await client.sessions.list(
                limit=50,
                include_archived=True,
                include_total=False,
                sort_by="lastQueuedAt",
                state="all",
            )
            ```
        """
        return await self._get(
            "/v1/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "created_by": created_by,
                        "created_after": created_after,
                        "cursor": cursor,
                        "limit": limit,
                        "exclude_pinned": exclude_pinned,
                        "external_ids": external_ids,
                        "has_project": has_project,
                        "include_archived": include_archived,
                        "include_total": include_total,
                        "participant": participant,
                        "pending_reviewer_keys": pending_reviewer_keys,
                        "project_ids": project_ids,
                        "pull_request_statuses": pull_request_statuses,
                        "repository_ids": repository_ids,
                        "search": search,
                        "sort_by": sort_by,
                        "source_ids": source_ids,
                        "source_types": source_types,
                        "state": state,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    async def create(
        self,
        *,
        agent: str | Omit = omit,
        base_branch: Optional[str] | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"] | Omit = omit,
        target_branch: Optional[str] | Omit = omit,
        visibility: Literal["private", "public"] | Omit = omit,
        agent_options: session_create_params.AgentOptions | Omit = omit,
        branch_name: Optional[str] | Omit = omit,
        code_repository_ids: SequenceNotStr[str] | Omit = omit,
        description: str,
        id: str | Omit = omit,
        rich_content: session_create_params.RichContent | Omit = omit,
        pull_request_id: str | Omit = omit,
        queue_right_away: bool | Omit = omit,
        session_mode: Literal["chat", "terminal"] | Omit = omit,
        startup_agent: Literal["claudeCode", "codex", "opencode", "pi", "amp", "cursor"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """
        Create a session for a task. Provide the initial prompt in description and optionally configure its repositories, agent, Build (normal) or Plan (planning) mode, and private or workspace visibility.

        Args:
            agent: Agent and model key to run, such as claudeCode:claude-fable-5-1. Omit to use the default.
            base_branch: Git branch to start work from. Omit or use null for the repository default.
            mcp_servers: MCP server or connection IDs to enable for the session.
            project_id: Project environment to use for the workspace. Omit or use null for the default.
            sandbox_size: VM size for the session workspace.
            target_branch: Default target branch for pull requests created by the session.
            visibility: Session visibility: private or visible to workspace (public).
            agent_options: Agent-specific runtime options, such as reasoning effort.
            branch_name: Git branch for this session. Omit or use null to generate a branch name.
            code_repository_ids: Repository IDs to make available in the session workspace.
            description: Initial task or prompt for the session.
            id: Optional caller-supplied session UUID. Omit to generate one.
            rich_content: Optional rich-text representation of the initial task. Provide description separately.
            pull_request_id: Pull request to associate with the session. Requires richContent.
            queue_right_away: Whether to queue the initial task immediately instead of only creating the session.
            session_mode: Whether to create a chat session or a terminal session.
            startup_agent: Coding agent to start in a terminal session.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionCreateResponse: Create a session

        Example:
            ```python
            session = await client.sessions.create(
                agent="claudeCode:claude-fable-5-1",
                base_branch="main",
                mcp_servers=[],
                project_id="your-project-id",
                target_branch="main",
                visibility="private",
                code_repository_ids=["123e4567-e89b-12d3-a456-426614174000"],
                description="Fix the authentication bug in the login component",
            )
            ```
        """
        return await self._post(
            "/v1/sessions",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "base_branch": base_branch,
                    "mcp_servers": mcp_servers,
                    "project_id": project_id,
                    "sandbox_size": sandbox_size,
                    "target_branch": target_branch,
                    "visibility": visibility,
                    "agent_options": agent_options,
                    "branch_name": branch_name,
                    "code_repository_ids": code_repository_ids,
                    "description": description,
                    "id": id,
                    "rich_content": rich_content,
                    "pull_request_id": pull_request_id,
                    "queue_right_away": queue_right_away,
                    "session_mode": session_mode,
                    "startup_agent": startup_agent,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    async def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveResponse:
        """
        Retrieve a session you have permission to access.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionRetrieveResponse: Retrieve a session

        Example:
            ```python
            session = await client.sessions.retrieve(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/v1/sessions/{sessionId}", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRetrieveResponse,
        )

    async def update(
        self,
        session_id: str,
        *,
        agent: Optional[str] | Omit = omit,
        agent_options: session_update_params.AgentOptions | Omit = omit,
        base_branch: Optional[str] | Omit = omit,
        branch_name: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        rich_content: Optional[session_update_params.RichContent] | Omit = omit,
        level: int | Omit = omit,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        mode: Literal["normal", "planning"] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]]
        | Omit = omit,
        target_branch: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["private", "public"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionUpdateResponse:
        """
        Update a session: archive or restore it, set priority, rename it, change agent/model, switch between Build (normal) and Plan (planning) modes, configure its workspace and branches, or change visibility between private and visible to workspace (public). Archiving uses level=0; restoring archived sessions uses level=1 and does not restart work. Use pins to pin or unpin sessions.

        Args:
            session_id: Path parameter.
            agent: Change the agent and model key. Null clears the session override.
            agent_options: Change agent-specific runtime options, such as reasoning effort.
            base_branch: Change the starting Git branch. Null clears the session override.
            branch_name: Change the session Git branch name. Null clears the stored name.
            description: Replace the initial task prompt; only the session creator can change it. Use createMessage to send a follow-up task.
            rich_content: Replace the initial prompt rich-text document, or null to clear it. Only the session creator can change it.
            level: Archive or restore the session and set its priority: 0 archives and stops its VM; 1 restores without restarting work; 2–100 also keep it unarchived and set its priority level. Omit to preserve the current level.
            mcp_servers: Replace the enabled MCP server or connection IDs. An empty array clears the selection.
            mode: Switch between Build (normal) and Plan (planning) modes.
            project_id: Change the project environment used for the workspace. Null clears the session override.
            sandbox_size: Change the workspace VM size. Null clears the session override.
            target_branch: Change the default pull request target branch. Null clears the session override.
            title: Rename the session.
            visibility: Change session visibility: private or visible to workspace (public). Only the session creator can change it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionUpdateResponse: Update a session

        Example:
            ```python
            session = await client.sessions.update(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            path_template("/v1/sessions/{sessionId}", **{"sessionId": session_id}),
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "agent_options": agent_options,
                    "base_branch": base_branch,
                    "branch_name": branch_name,
                    "description": description,
                    "rich_content": rich_content,
                    "level": level,
                    "mcp_servers": mcp_servers,
                    "mode": mode,
                    "project_id": project_id,
                    "sandbox_size": sandbox_size,
                    "target_branch": target_branch,
                    "title": title,
                    "visibility": visibility,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionUpdateResponse,
        )

    async def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDeleteResponse:
        """
        Archive a session and stop its VM without permanently deleting it. Equivalent to updateSession with level=0; restore with updateSession and level=1.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionDeleteResponse: Delete a session

        Example:
            ```python
            session = await client.sessions.delete(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            path_template("/v1/sessions/{sessionId}", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionDeleteResponse,
        )

    async def fork(
        self,
        session_id: str,
        *,
        prompt: str | Omit = omit,
        title: str | Omit = omit,
        queue_right_away: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionForkResponse:
        """
        Create an independent session from a fresh workspace snapshot, or the latest saved snapshot when stopped, without replaying messages or adding context.

        Args:
            session_id: Path parameter.
            prompt: Optional first task for the independent fork. Existing messages are not replayed.
            title: Display title for the forked session.
            queue_right_away: Start the supplied prompt immediately. Without a prompt, the fork waits for a new message.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionForkResponse: Fork a session

        Example:
            ```python
            session = await client.sessions.fork(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                queue_right_away=True,
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/v1/sessions/{sessionId}/fork", **{"sessionId": session_id}),
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "title": title,
                    "queue_right_away": queue_right_away,
                },
                session_fork_params.SessionForkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionForkResponse,
        )

    async def stop(
        self,
        session_id: str,
        *,
        cancel_queued: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionStopResponse:
        """
        Interrupt active session work without archiving it. Continue with the next queued message, or set cancelQueued=true to cancel pending messages too.

        Args:
            session_id: Path parameter.
            cancel_queued: Also cancel pending queued messages instead of continuing with the next queued message. Does not archive the session.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionStopResponse: Stop a session

        Example:
            ```python
            session = await client.sessions.stop(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/v1/sessions/{sessionId}/stop", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cancel_queued": cancel_queued}, session_stop_params.SessionStopParams
                ),
            ),
            cast_to=SessionStopResponse,
        )

    async def list_events(
        self,
        session_id: str,
        *,
        cursor: Union[str, int] | Omit = omit,
        limit: int | Omit = omit,
        message_id: Union[str, Literal["null"]] | Omit = omit,
        after: Union[str, int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListEventsResponse:
        """
        List recorded session stream events with cursor pagination.

        Args:
            session_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            message_id: Filter by message ID, or "null" for session-level events.
            after: Only return events recorded after this event ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SessionListEventsResponse: List session events

        Example:
            ```python
            session = await client.sessions.list_events(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/v1/sessions/{sessionId}/events", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "message_id": message_id, "after": after},
                    session_list_events_params.SessionListEventsParams,
                ),
            ),
            cast_to=SessionListEventsResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sessions.update,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )
        self.fork = to_raw_response_wrapper(
            sessions.fork,
        )
        self.stop = to_raw_response_wrapper(
            sessions.stop,
        )
        self.list_events = to_raw_response_wrapper(
            sessions.list_events,
        )

    @cached_property
    def sources(self) -> SourcesResourceWithRawResponse:
        return SourcesResourceWithRawResponse(self._sessions.sources)

    @cached_property
    def diffs(self) -> DiffsResourceWithRawResponse:
        return DiffsResourceWithRawResponse(self._sessions.diffs)

    @cached_property
    def inputs(self) -> InputsResourceWithRawResponse:
        return InputsResourceWithRawResponse(self._sessions.inputs)

    @cached_property
    def queue(self) -> QueueResourceWithRawResponse:
        return QueueResourceWithRawResponse(self._sessions.queue)

    @cached_property
    def commands(self) -> CommandsResourceWithRawResponse:
        return CommandsResourceWithRawResponse(self._sessions.commands)


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sessions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )
        self.fork = async_to_raw_response_wrapper(
            sessions.fork,
        )
        self.stop = async_to_raw_response_wrapper(
            sessions.stop,
        )
        self.list_events = async_to_raw_response_wrapper(
            sessions.list_events,
        )

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithRawResponse:
        return AsyncSourcesResourceWithRawResponse(self._sessions.sources)

    @cached_property
    def diffs(self) -> AsyncDiffsResourceWithRawResponse:
        return AsyncDiffsResourceWithRawResponse(self._sessions.diffs)

    @cached_property
    def inputs(self) -> AsyncInputsResourceWithRawResponse:
        return AsyncInputsResourceWithRawResponse(self._sessions.inputs)

    @cached_property
    def queue(self) -> AsyncQueueResourceWithRawResponse:
        return AsyncQueueResourceWithRawResponse(self._sessions.queue)

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithRawResponse:
        return AsyncCommandsResourceWithRawResponse(self._sessions.commands)


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sessions.update,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )
        self.fork = to_streamed_response_wrapper(
            sessions.fork,
        )
        self.stop = to_streamed_response_wrapper(
            sessions.stop,
        )
        self.list_events = to_streamed_response_wrapper(
            sessions.list_events,
        )

    @cached_property
    def sources(self) -> SourcesResourceWithStreamingResponse:
        return SourcesResourceWithStreamingResponse(self._sessions.sources)

    @cached_property
    def diffs(self) -> DiffsResourceWithStreamingResponse:
        return DiffsResourceWithStreamingResponse(self._sessions.diffs)

    @cached_property
    def inputs(self) -> InputsResourceWithStreamingResponse:
        return InputsResourceWithStreamingResponse(self._sessions.inputs)

    @cached_property
    def queue(self) -> QueueResourceWithStreamingResponse:
        return QueueResourceWithStreamingResponse(self._sessions.queue)

    @cached_property
    def commands(self) -> CommandsResourceWithStreamingResponse:
        return CommandsResourceWithStreamingResponse(self._sessions.commands)


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sessions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )
        self.fork = async_to_streamed_response_wrapper(
            sessions.fork,
        )
        self.stop = async_to_streamed_response_wrapper(
            sessions.stop,
        )
        self.list_events = async_to_streamed_response_wrapper(
            sessions.list_events,
        )

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithStreamingResponse:
        return AsyncSourcesResourceWithStreamingResponse(self._sessions.sources)

    @cached_property
    def diffs(self) -> AsyncDiffsResourceWithStreamingResponse:
        return AsyncDiffsResourceWithStreamingResponse(self._sessions.diffs)

    @cached_property
    def inputs(self) -> AsyncInputsResourceWithStreamingResponse:
        return AsyncInputsResourceWithStreamingResponse(self._sessions.inputs)

    @cached_property
    def queue(self) -> AsyncQueueResourceWithStreamingResponse:
        return AsyncQueueResourceWithStreamingResponse(self._sessions.queue)

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithStreamingResponse:
        return AsyncCommandsResourceWithStreamingResponse(self._sessions.commands)
