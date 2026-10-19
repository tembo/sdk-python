# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.sessions.diff_list_response import DiffListResponse
from ...types.sessions import diff_list_params
from ...types.sessions.diff_retrieve_response import DiffRetrieveResponse

__all__ = ["DiffsResource", "AsyncDiffsResource"]


class DiffsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiffsResourceWithRawResponse:
        return DiffsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiffsResourceWithStreamingResponse:
        return DiffsResourceWithStreamingResponse(self)

    def list(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        has_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DiffListResponse:
        """
        List recorded session diff metadata with cursor pagination.

        Args:
            session_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            has_changes: Filter by whether a recorded diff contains changes.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DiffListResponse: List session diffs

        Example:
            ```python
            diff = client.sessions.diffs.list(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/v1/sessions/{sessionId}/diffs", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "has_changes": has_changes}, diff_list_params.DiffListParams
                ),
            ),
            cast_to=DiffListResponse,
        )

    def retrieve(
        self,
        diff_id: str,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DiffRetrieveResponse:
        """
        Retrieve one recorded session diff and its content.

        Args:
            diff_id: Path parameter.
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DiffRetrieveResponse: Retrieve a session diff

        Example:
            ```python
            diff = client.sessions.diffs.retrieve(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                diff_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if diff_id is None or (isinstance(diff_id, str) and not diff_id):
            raise ValueError(f"Expected a non-empty value for `diff_id` but received {diff_id!r}")
        return self._get(
            path_template("/v1/sessions/{sessionId}/diffs/{diffId}", **{"sessionId": session_id, "diffId": diff_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiffRetrieveResponse,
        )


class AsyncDiffsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiffsResourceWithRawResponse:
        return AsyncDiffsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiffsResourceWithStreamingResponse:
        return AsyncDiffsResourceWithStreamingResponse(self)

    async def list(
        self,
        session_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        has_changes: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DiffListResponse:
        """
        List recorded session diff metadata with cursor pagination.

        Args:
            session_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            has_changes: Filter by whether a recorded diff contains changes.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DiffListResponse: List session diffs

        Example:
            ```python
            diff = await client.sessions.diffs.list(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/v1/sessions/{sessionId}/diffs", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "has_changes": has_changes}, diff_list_params.DiffListParams
                ),
            ),
            cast_to=DiffListResponse,
        )

    async def retrieve(
        self,
        diff_id: str,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DiffRetrieveResponse:
        """
        Retrieve one recorded session diff and its content.

        Args:
            diff_id: Path parameter.
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DiffRetrieveResponse: Retrieve a session diff

        Example:
            ```python
            diff = await client.sessions.diffs.retrieve(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                diff_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if diff_id is None or (isinstance(diff_id, str) and not diff_id):
            raise ValueError(f"Expected a non-empty value for `diff_id` but received {diff_id!r}")
        return await self._get(
            path_template("/v1/sessions/{sessionId}/diffs/{diffId}", **{"sessionId": session_id, "diffId": diff_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiffRetrieveResponse,
        )


class DiffsResourceWithRawResponse:
    def __init__(self, diffs: DiffsResource) -> None:
        self._diffs = diffs

        self.list = to_raw_response_wrapper(
            diffs.list,
        )
        self.retrieve = to_raw_response_wrapper(
            diffs.retrieve,
        )


class AsyncDiffsResourceWithRawResponse:
    def __init__(self, diffs: AsyncDiffsResource) -> None:
        self._diffs = diffs

        self.list = async_to_raw_response_wrapper(
            diffs.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            diffs.retrieve,
        )


class DiffsResourceWithStreamingResponse:
    def __init__(self, diffs: DiffsResource) -> None:
        self._diffs = diffs

        self.list = to_streamed_response_wrapper(
            diffs.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            diffs.retrieve,
        )


class AsyncDiffsResourceWithStreamingResponse:
    def __init__(self, diffs: AsyncDiffsResource) -> None:
        self._diffs = diffs

        self.list = async_to_streamed_response_wrapper(
            diffs.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            diffs.retrieve,
        )
