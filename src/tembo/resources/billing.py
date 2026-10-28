# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Union
from datetime import datetime
from typing_extensions import Literal
from .._types import SequenceNotStr

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
from ..types.billing_retrieve_response import BillingRetrieveResponse
from ..types.billing_list_usage_response import BillingListUsageResponse
from ..types import billing_list_usage_params

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveResponse:
        """
        Retrieve billing and credit information for the organization.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingRetrieveResponse: Retrieve billing

        Example:
            ```python
            billing = client.billing.retrieve()
            ```
        """
        return self._get(
            "/v1/billing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveResponse,
        )

    def list_usage(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        type: Literal["all", "sessions", "warm-pool"] | Omit = omit,
        session_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        created_by: SequenceNotStr[str] | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListUsageResponse:
        """
        List session usage by default, or include warm pool compute with the type filter. Uses cursor pagination.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            type: Usage types to include. Defaults to sessions for backwards compatibility.
            session_id: Filter billing usage to this session.
            created_after: Include sessions created or warm pool runtime at or after this ISO 8601 timestamp.
            created_before: Include sessions created or warm pool runtime before this ISO 8601 timestamp.
            created_by: Filter by creator IDs, supplied as a comma-separated list.
            models: Filter by model names, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingListUsageResponse: List billing usage

        Example:
            ```python
            billing = client.billing.list_usage(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "type": type,
                        "session_id": session_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "created_by": created_by,
                        "models": models,
                    },
                    billing_list_usage_params.BillingListUsageParams,
                ),
            ),
            cast_to=BillingListUsageResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveResponse:
        """
        Retrieve billing and credit information for the organization.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingRetrieveResponse: Retrieve billing

        Example:
            ```python
            billing = await client.billing.retrieve()
            ```
        """
        return await self._get(
            "/v1/billing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveResponse,
        )

    async def list_usage(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        type: Literal["all", "sessions", "warm-pool"] | Omit = omit,
        session_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        created_by: SequenceNotStr[str] | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListUsageResponse:
        """
        List session usage by default, or include warm pool compute with the type filter. Uses cursor pagination.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            type: Usage types to include. Defaults to sessions for backwards compatibility.
            session_id: Filter billing usage to this session.
            created_after: Include sessions created or warm pool runtime at or after this ISO 8601 timestamp.
            created_before: Include sessions created or warm pool runtime before this ISO 8601 timestamp.
            created_by: Filter by creator IDs, supplied as a comma-separated list.
            models: Filter by model names, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BillingListUsageResponse: List billing usage

        Example:
            ```python
            billing = await client.billing.list_usage(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "type": type,
                        "session_id": session_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "created_by": created_by,
                        "models": models,
                    },
                    billing_list_usage_params.BillingListUsageParams,
                ),
            ),
            cast_to=BillingListUsageResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.retrieve = to_raw_response_wrapper(
            billing.retrieve,
        )
        self.list_usage = to_raw_response_wrapper(
            billing.list_usage,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.retrieve = async_to_raw_response_wrapper(
            billing.retrieve,
        )
        self.list_usage = async_to_raw_response_wrapper(
            billing.list_usage,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.retrieve = to_streamed_response_wrapper(
            billing.retrieve,
        )
        self.list_usage = to_streamed_response_wrapper(
            billing.list_usage,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.retrieve = async_to_streamed_response_wrapper(
            billing.retrieve,
        )
        self.list_usage = async_to_streamed_response_wrapper(
            billing.list_usage,
        )
