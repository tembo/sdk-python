# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal
from .._types import SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.message_list_response import MessageListResponse
from ..types import message_list_params, message_create_params, message_update_params
from ..types.message_create_response import MessageCreateResponse
from ..types.agent_options_input_param import AgentOptionsInputParam
from ..types.tip_tap_document_param import TipTapDocumentParam
from ..types.message_retrieve_response import MessageRetrieveResponse
from ..types.message_update_response import MessageUpdateResponse
from ..types.message_delete_response import MessageDeleteResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        session_id: str | Omit = omit,
        thread_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        List organization messages with optional session and thread filters.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            session_id: Filter messages belonging to this session.
            thread_id: Filter messages belonging to this thread.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageListResponse: List messages

        Example:
            ```python
            message = client.messages.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "session_id": session_id, "thread_id": thread_id},
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def create(
        self,
        *,
        artifact_id: str | Omit = omit,
        content: str,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        pull_request_id: str | Omit = omit,
        session_id: str,
        agent_options: AgentOptionsInputParam | Omit = omit,
        delivery_mode: Literal["queue", "steer"] | Omit = omit,
        rich_content: TipTapDocumentParam | Omit = omit,
        slash_command: message_create_params.SlashCommand | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse:
        """
        Send a task or follow-up message to an existing session, resume work, or steer an active agent turn using deliveryMode.

        Args:
            artifact_id: Artifact to associate with this message.
            content: Text of the task, follow-up, or steering instruction to send to the session agent.
            mcp_servers: MCP server or connection IDs selected for this message.
            pull_request_id: Pull request to associate with this message.
            session_id: Session to receive this message. Use this operation to continue work in an existing session.
            agent_options: Agent-specific runtime options for this message, such as reasoning effort.
            delivery_mode: queue adds a follow-up task; steer sends guidance to an active agent turn when supported.
            rich_content: Optional rich-text representation of the message. Provide the required text content separately.
            slash_command: Structured slash command to execute with this message.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageCreateResponse: Create a message

        Example:
            ```python
            message = client.messages.create(
                content="x",
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return self._post(
            "/v1/messages",
            body=maybe_transform(
                {
                    "artifact_id": artifact_id,
                    "content": content,
                    "mcp_servers": mcp_servers,
                    "pull_request_id": pull_request_id,
                    "session_id": session_id,
                    "agent_options": agent_options,
                    "delivery_mode": delivery_mode,
                    "rich_content": rich_content,
                    "slash_command": slash_command,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieve an organization message by ID.

        Args:
            message_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageRetrieveResponse: Retrieve a message

        Example:
            ```python
            message = client.messages.retrieve(
                message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if message_id is None or (isinstance(message_id, str) and not message_id):
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/v1/messages/{messageId}", **{"messageId": message_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def update(
        self,
        message_id: str,
        *,
        content: str | Omit = omit,
        rich_content: Optional[TipTapDocumentParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update message content before its queued processing has started.

        Args:
            message_id: Path parameter.
            content: Replace the text of a queued message before processing starts.
            rich_content: Replace the queued message rich-text document, or null to clear it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageUpdateResponse: Update a message

        Example:
            ```python
            message = client.messages.update(
                message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if message_id is None or (isinstance(message_id, str) and not message_id):
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._patch(
            path_template("/v1/messages/{messageId}", **{"messageId": message_id}),
            body=maybe_transform(
                {
                    "content": content,
                    "rich_content": rich_content,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDeleteResponse:
        """
        Delete a message and cancel its queued jobs, runtime turns, and active sandbox sessions.

        Args:
            message_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageDeleteResponse: Delete a message

        Example:
            ```python
            message = client.messages.delete(
                message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if message_id is None or (isinstance(message_id, str) and not message_id):
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            path_template("/v1/messages/{messageId}", **{"messageId": message_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDeleteResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        session_id: str | Omit = omit,
        thread_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        List organization messages with optional session and thread filters.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            session_id: Filter messages belonging to this session.
            thread_id: Filter messages belonging to this thread.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageListResponse: List messages

        Example:
            ```python
            message = await client.messages.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "session_id": session_id, "thread_id": thread_id},
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def create(
        self,
        *,
        artifact_id: str | Omit = omit,
        content: str,
        mcp_servers: SequenceNotStr[str] | Omit = omit,
        pull_request_id: str | Omit = omit,
        session_id: str,
        agent_options: AgentOptionsInputParam | Omit = omit,
        delivery_mode: Literal["queue", "steer"] | Omit = omit,
        rich_content: TipTapDocumentParam | Omit = omit,
        slash_command: message_create_params.SlashCommand | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse:
        """
        Send a task or follow-up message to an existing session, resume work, or steer an active agent turn using deliveryMode.

        Args:
            artifact_id: Artifact to associate with this message.
            content: Text of the task, follow-up, or steering instruction to send to the session agent.
            mcp_servers: MCP server or connection IDs selected for this message.
            pull_request_id: Pull request to associate with this message.
            session_id: Session to receive this message. Use this operation to continue work in an existing session.
            agent_options: Agent-specific runtime options for this message, such as reasoning effort.
            delivery_mode: queue adds a follow-up task; steer sends guidance to an active agent turn when supported.
            rich_content: Optional rich-text representation of the message. Provide the required text content separately.
            slash_command: Structured slash command to execute with this message.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageCreateResponse: Create a message

        Example:
            ```python
            message = await client.messages.create(
                content="x",
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return await self._post(
            "/v1/messages",
            body=await async_maybe_transform(
                {
                    "artifact_id": artifact_id,
                    "content": content,
                    "mcp_servers": mcp_servers,
                    "pull_request_id": pull_request_id,
                    "session_id": session_id,
                    "agent_options": agent_options,
                    "delivery_mode": delivery_mode,
                    "rich_content": rich_content,
                    "slash_command": slash_command,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    async def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieve an organization message by ID.

        Args:
            message_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageRetrieveResponse: Retrieve a message

        Example:
            ```python
            message = await client.messages.retrieve(
                message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if message_id is None or (isinstance(message_id, str) and not message_id):
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/v1/messages/{messageId}", **{"messageId": message_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def update(
        self,
        message_id: str,
        *,
        content: str | Omit = omit,
        rich_content: Optional[TipTapDocumentParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """
        Update message content before its queued processing has started.

        Args:
            message_id: Path parameter.
            content: Replace the text of a queued message before processing starts.
            rich_content: Replace the queued message rich-text document, or null to clear it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageUpdateResponse: Update a message

        Example:
            ```python
            message = await client.messages.update(
                message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if message_id is None or (isinstance(message_id, str) and not message_id):
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._patch(
            path_template("/v1/messages/{messageId}", **{"messageId": message_id}),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "rich_content": rich_content,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    async def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDeleteResponse:
        """
        Delete a message and cancel its queued jobs, runtime turns, and active sandbox sessions.

        Args:
            message_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MessageDeleteResponse: Delete a message

        Example:
            ```python
            message = await client.messages.delete(
                message_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if message_id is None or (isinstance(message_id, str) and not message_id):
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            path_template("/v1/messages/{messageId}", **{"messageId": message_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDeleteResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )
