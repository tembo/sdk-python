# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import SequenceNotStr

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.sessions.queue_update_response import QueueUpdateResponse
from ...types.sessions import queue_update_params

__all__ = ["QueueResource", "AsyncQueueResource"]


class QueueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueueResourceWithRawResponse:
        return QueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueueResourceWithStreamingResponse:
        return QueueResourceWithStreamingResponse(self)

    def update(
        self,
        session_id: str,
        *,
        message_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueUpdateResponse:
        """
        Replace the order of messages waiting in a session queue.

        Args:
            session_id: Path parameter.
            message_ids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            QueueUpdateResponse: Update a session queue

        Example:
            ```python
            queue = client.sessions.queue.update(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                message_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._put(
            path_template("/v1/sessions/{sessionId}/queue", **{"sessionId": session_id}),
            body=maybe_transform(
                {"message_ids": message_ids},
                queue_update_params.QueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueUpdateResponse,
        )


class AsyncQueueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueueResourceWithRawResponse:
        return AsyncQueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueueResourceWithStreamingResponse:
        return AsyncQueueResourceWithStreamingResponse(self)

    async def update(
        self,
        session_id: str,
        *,
        message_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueUpdateResponse:
        """
        Replace the order of messages waiting in a session queue.

        Args:
            session_id: Path parameter.
            message_ids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            QueueUpdateResponse: Update a session queue

        Example:
            ```python
            queue = await client.sessions.queue.update(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                message_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._put(
            path_template("/v1/sessions/{sessionId}/queue", **{"sessionId": session_id}),
            body=await async_maybe_transform(
                {"message_ids": message_ids},
                queue_update_params.QueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueUpdateResponse,
        )


class QueueResourceWithRawResponse:
    def __init__(self, queue: QueueResource) -> None:
        self._queue = queue

        self.update = to_raw_response_wrapper(
            queue.update,
        )


class AsyncQueueResourceWithRawResponse:
    def __init__(self, queue: AsyncQueueResource) -> None:
        self._queue = queue

        self.update = async_to_raw_response_wrapper(
            queue.update,
        )


class QueueResourceWithStreamingResponse:
    def __init__(self, queue: QueueResource) -> None:
        self._queue = queue

        self.update = to_streamed_response_wrapper(
            queue.update,
        )


class AsyncQueueResourceWithStreamingResponse:
    def __init__(self, queue: AsyncQueueResource) -> None:
        self._queue = queue

        self.update = async_to_streamed_response_wrapper(
            queue.update,
        )
