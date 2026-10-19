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
from ..types.insight_retrieve_response import InsightRetrieveResponse
from ..types import (
    insight_retrieve_params,
    insight_update_params,
    insight_list_members_params,
    insight_list_repositories_params,
)
from ..types.insight_update_response import InsightUpdateResponse
from ..types.insight_list_members_response import InsightListMembersResponse
from ..types.insight_list_repositories_response import InsightListRepositoriesResponse

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        range: Literal["1d", "7d", "30d", "1y"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightRetrieveResponse:
        """
        Retrieve pull request contribution insights and their collection status for the current organization.

        Args:
            range: Time range to aggregate: last day, 7 days, 30 days, or year. Defaults to 1y.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightRetrieveResponse: Retrieve insights

        Example:
            ```python
            insight = client.insights.retrieve(
                range="1y",
            )
            ```
        """
        return self._get(
            "/v1/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"range": range}, insight_retrieve_params.InsightRetrieveParams),
            ),
            cast_to=InsightRetrieveResponse,
        )

    def update(
        self,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightUpdateResponse:
        """
        Enable or disable pull request insight collection. Enabling starts the initial refresh when needed.

        Args:
            enabled: Enable or disable pull request contribution insight collection. Enabling starts the initial refresh when needed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightUpdateResponse: Update insights

        Example:
            ```python
            insight = client.insights.update(
                enabled=False,
            )
            ```
        """
        return self._patch(
            "/v1/insights",
            body=maybe_transform(
                {"enabled": enabled},
                insight_update_params.InsightUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightUpdateResponse,
        )

    def list_members(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        range: Literal["1d", "7d", "30d", "1y"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightListMembersResponse:
        """
        List organization members included in pull request insights.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            range: Time range to aggregate: last day, 7 days, 30 days, or year. Defaults to 1y.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightListMembersResponse: List insight members

        Example:
            ```python
            insight = client.insights.list_members(
                limit=50,
                range="1y",
            )
            ```
        """
        return self._get(
            "/v1/insights/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "range": range},
                    insight_list_members_params.InsightListMembersParams,
                ),
            ),
            cast_to=InsightListMembersResponse,
        )

    def list_repositories(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        range: Literal["1d", "7d", "30d", "1y"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightListRepositoriesResponse:
        """
        List repositories included in pull request insights for the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            range: Time range to aggregate: last day, 7 days, 30 days, or year. Defaults to 1y.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightListRepositoriesResponse: List insight repositories

        Example:
            ```python
            insight = client.insights.list_repositories(
                limit=50,
                range="1y",
            )
            ```
        """
        return self._get(
            "/v1/insights/repositories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "range": range},
                    insight_list_repositories_params.InsightListRepositoriesParams,
                ),
            ),
            cast_to=InsightListRepositoriesResponse,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        range: Literal["1d", "7d", "30d", "1y"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightRetrieveResponse:
        """
        Retrieve pull request contribution insights and their collection status for the current organization.

        Args:
            range: Time range to aggregate: last day, 7 days, 30 days, or year. Defaults to 1y.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightRetrieveResponse: Retrieve insights

        Example:
            ```python
            insight = await client.insights.retrieve(
                range="1y",
            )
            ```
        """
        return await self._get(
            "/v1/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"range": range}, insight_retrieve_params.InsightRetrieveParams),
            ),
            cast_to=InsightRetrieveResponse,
        )

    async def update(
        self,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightUpdateResponse:
        """
        Enable or disable pull request insight collection. Enabling starts the initial refresh when needed.

        Args:
            enabled: Enable or disable pull request contribution insight collection. Enabling starts the initial refresh when needed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightUpdateResponse: Update insights

        Example:
            ```python
            insight = await client.insights.update(
                enabled=False,
            )
            ```
        """
        return await self._patch(
            "/v1/insights",
            body=await async_maybe_transform(
                {"enabled": enabled},
                insight_update_params.InsightUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightUpdateResponse,
        )

    async def list_members(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        range: Literal["1d", "7d", "30d", "1y"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightListMembersResponse:
        """
        List organization members included in pull request insights.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            range: Time range to aggregate: last day, 7 days, 30 days, or year. Defaults to 1y.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightListMembersResponse: List insight members

        Example:
            ```python
            insight = await client.insights.list_members(
                limit=50,
                range="1y",
            )
            ```
        """
        return await self._get(
            "/v1/insights/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "range": range},
                    insight_list_members_params.InsightListMembersParams,
                ),
            ),
            cast_to=InsightListMembersResponse,
        )

    async def list_repositories(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        range: Literal["1d", "7d", "30d", "1y"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightListRepositoriesResponse:
        """
        List repositories included in pull request insights for the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            range: Time range to aggregate: last day, 7 days, 30 days, or year. Defaults to 1y.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InsightListRepositoriesResponse: List insight repositories

        Example:
            ```python
            insight = await client.insights.list_repositories(
                limit=50,
                range="1y",
            )
            ```
        """
        return await self._get(
            "/v1/insights/repositories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "range": range},
                    insight_list_repositories_params.InsightListRepositoriesParams,
                ),
            ),
            cast_to=InsightListRepositoriesResponse,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.retrieve = to_raw_response_wrapper(
            insights.retrieve,
        )
        self.update = to_raw_response_wrapper(
            insights.update,
        )
        self.list_members = to_raw_response_wrapper(
            insights.list_members,
        )
        self.list_repositories = to_raw_response_wrapper(
            insights.list_repositories,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.retrieve = async_to_raw_response_wrapper(
            insights.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            insights.update,
        )
        self.list_members = async_to_raw_response_wrapper(
            insights.list_members,
        )
        self.list_repositories = async_to_raw_response_wrapper(
            insights.list_repositories,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.retrieve = to_streamed_response_wrapper(
            insights.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            insights.update,
        )
        self.list_members = to_streamed_response_wrapper(
            insights.list_members,
        )
        self.list_repositories = to_streamed_response_wrapper(
            insights.list_repositories,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.retrieve = async_to_streamed_response_wrapper(
            insights.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            insights.update,
        )
        self.list_members = async_to_streamed_response_wrapper(
            insights.list_members,
        )
        self.list_repositories = async_to_streamed_response_wrapper(
            insights.list_repositories,
        )
