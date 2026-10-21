# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sessions.command_list_response import CommandListResponse

__all__ = ["CommandsResource", "AsyncCommandsResource"]


class CommandsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandsResourceWithRawResponse:
        return CommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandsResourceWithStreamingResponse:
        return CommandsResourceWithStreamingResponse(self)

    def list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandListResponse:
        """
        List slash commands available to the session runtime.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CommandListResponse: List session commands

        Example:
            ```python
            command = client.sessions.commands.list(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/v1/sessions/{sessionId}/commands", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandListResponse,
        )


class AsyncCommandsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandsResourceWithRawResponse:
        return AsyncCommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandsResourceWithStreamingResponse:
        return AsyncCommandsResourceWithStreamingResponse(self)

    async def list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandListResponse:
        """
        List slash commands available to the session runtime.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CommandListResponse: List session commands

        Example:
            ```python
            command = await client.sessions.commands.list(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/v1/sessions/{sessionId}/commands", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandListResponse,
        )


class CommandsResourceWithRawResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.list = to_raw_response_wrapper(
            commands.list,
        )


class AsyncCommandsResourceWithRawResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.list = async_to_raw_response_wrapper(
            commands.list,
        )


class CommandsResourceWithStreamingResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.list = to_streamed_response_wrapper(
            commands.list,
        )


class AsyncCommandsResourceWithStreamingResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.list = async_to_streamed_response_wrapper(
            commands.list,
        )
