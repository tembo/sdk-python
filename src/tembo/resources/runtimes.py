# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.runtime_list_response import RuntimeListResponse
from ..types import runtime_list_params

__all__ = ["RuntimesResource", "AsyncRuntimesResource"]


class RuntimesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RuntimesResourceWithRawResponse:
        return RuntimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RuntimesResourceWithStreamingResponse:
        return RuntimesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Literal["claudeCode", "codex", "opencode", "cursor", "amp", "fx", "pi"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuntimeListResponse:
        """
        List execution runtimes and their compatible model references for the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RuntimeListResponse: List runtimes

        Example:
            ```python
            runtime = client.runtimes.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/runtimes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, runtime_list_params.RuntimeListParams),
            ),
            cast_to=RuntimeListResponse,
        )


class AsyncRuntimesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRuntimesResourceWithRawResponse:
        return AsyncRuntimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRuntimesResourceWithStreamingResponse:
        return AsyncRuntimesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: Literal["claudeCode", "codex", "opencode", "cursor", "amp", "fx", "pi"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuntimeListResponse:
        """
        List execution runtimes and their compatible model references for the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RuntimeListResponse: List runtimes

        Example:
            ```python
            runtime = await client.runtimes.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/runtimes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, runtime_list_params.RuntimeListParams
                ),
            ),
            cast_to=RuntimeListResponse,
        )


class RuntimesResourceWithRawResponse:
    def __init__(self, runtimes: RuntimesResource) -> None:
        self._runtimes = runtimes

        self.list = to_raw_response_wrapper(
            runtimes.list,
        )


class AsyncRuntimesResourceWithRawResponse:
    def __init__(self, runtimes: AsyncRuntimesResource) -> None:
        self._runtimes = runtimes

        self.list = async_to_raw_response_wrapper(
            runtimes.list,
        )


class RuntimesResourceWithStreamingResponse:
    def __init__(self, runtimes: RuntimesResource) -> None:
        self._runtimes = runtimes

        self.list = to_streamed_response_wrapper(
            runtimes.list,
        )


class AsyncRuntimesResourceWithStreamingResponse:
    def __init__(self, runtimes: AsyncRuntimesResource) -> None:
        self._runtimes = runtimes

        self.list = async_to_streamed_response_wrapper(
            runtimes.list,
        )
