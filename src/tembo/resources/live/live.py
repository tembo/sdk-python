# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Callable

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.live_authorize_response import LiveAuthorizeResponse
from ...types.websocket_connection_options import WebSocketConnectionOptions
from ...types.websocket_reconnection import ReconnectingEvent, ReconnectingOverrides
from .ws import (
    LiveResourceConnectionManager as LiveResourceConnectionManager,
    AsyncLiveResourceConnectionManager as AsyncLiveResourceConnectionManager,
    LiveResourceConnection as LiveResourceConnection,
    AsyncLiveResourceConnection as AsyncLiveResourceConnection,
)

__all__ = ["LiveResource", "AsyncLiveResource"]


class LiveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveResourceWithRawResponse:
        return LiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveResourceWithStreamingResponse:
        return LiveResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveAuthorizeResponse:
        """
        Issue a 30-second WebSocket ticket for one live connection that multiplexes resource subscriptions.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveAuthorizeResponse: Connection ticket

        Example:
            ```python
            live = client.live.authorize()
            ```
        """
        return self._post(
            "/v1/live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveAuthorizeResponse,
        )

    def connect(
        self,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> LiveResourceConnectionManager:
        return LiveResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
            on_reconnecting=on_reconnecting,
            max_retries=max_retries,
            initial_delay=initial_delay,
            max_delay=max_delay,
            max_queue_size=max_queue_size,
        )


class AsyncLiveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveResourceWithRawResponse:
        return AsyncLiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveResourceWithStreamingResponse:
        return AsyncLiveResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveAuthorizeResponse:
        """
        Issue a 30-second WebSocket ticket for one live connection that multiplexes resource subscriptions.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LiveAuthorizeResponse: Connection ticket

        Example:
            ```python
            live = await client.live.authorize()
            ```
        """
        return await self._post(
            "/v1/live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveAuthorizeResponse,
        )

    def connect(
        self,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> AsyncLiveResourceConnectionManager:
        return AsyncLiveResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
            on_reconnecting=on_reconnecting,
            max_retries=max_retries,
            initial_delay=initial_delay,
            max_delay=max_delay,
            max_queue_size=max_queue_size,
        )


class LiveResourceWithRawResponse:
    def __init__(self, live: LiveResource) -> None:
        self._live = live

        self.authorize = to_raw_response_wrapper(
            live.authorize,
        )


class AsyncLiveResourceWithRawResponse:
    def __init__(self, live: AsyncLiveResource) -> None:
        self._live = live

        self.authorize = async_to_raw_response_wrapper(
            live.authorize,
        )


class LiveResourceWithStreamingResponse:
    def __init__(self, live: LiveResource) -> None:
        self._live = live

        self.authorize = to_streamed_response_wrapper(
            live.authorize,
        )


class AsyncLiveResourceWithStreamingResponse:
    def __init__(self, live: AsyncLiveResource) -> None:
        self._live = live

        self.authorize = async_to_streamed_response_wrapper(
            live.authorize,
        )
