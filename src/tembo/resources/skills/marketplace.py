# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

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
from ...types.skills.marketplace_list_response import MarketplaceListResponse
from ...types.skills import marketplace_list_params, marketplace_retrieve_params
from ...types.skills.marketplace_retrieve_response import MarketplaceRetrieveResponse

__all__ = ["MarketplaceResource", "AsyncMarketplaceResource"]


class MarketplaceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketplaceResourceWithRawResponse:
        return MarketplaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketplaceResourceWithStreamingResponse:
        return MarketplaceResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Literal[""] | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketplaceListResponse:
        """
        List popular marketplace skills or search the catalog. Results have no continuation cursor.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search the marketplace catalog. Omit to list popular skills.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketplaceListResponse: List marketplace skills

        Example:
            ```python
            marketplace = client.skills.marketplace.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/skills/marketplace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search}, marketplace_list_params.MarketplaceListParams
                ),
            ),
            cast_to=MarketplaceListResponse,
        )

    def retrieve(
        self,
        skill_id: str,
        *,
        source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketplaceRetrieveResponse:
        """
        Retrieve the files and content hash for a marketplace skill. This does not install the skill.

        Args:
            skill_id: Path parameter.
            source: The source repository in owner/repo format. Domain-only sources cannot be downloaded and return 404.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketplaceRetrieveResponse: Retrieve a marketplace skill

        Example:
            ```python
            marketplace = client.skills.marketplace.retrieve(
                skill_id="skillId",
                source="source",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._get(
            path_template("/v1/skills/marketplace/{skillId}", **{"skillId": skill_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"source": source}, marketplace_retrieve_params.MarketplaceRetrieveParams),
            ),
            cast_to=MarketplaceRetrieveResponse,
        )


class AsyncMarketplaceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketplaceResourceWithRawResponse:
        return AsyncMarketplaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketplaceResourceWithStreamingResponse:
        return AsyncMarketplaceResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: Literal[""] | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketplaceListResponse:
        """
        List popular marketplace skills or search the catalog. Results have no continuation cursor.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search the marketplace catalog. Omit to list popular skills.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketplaceListResponse: List marketplace skills

        Example:
            ```python
            marketplace = await client.skills.marketplace.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/skills/marketplace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search}, marketplace_list_params.MarketplaceListParams
                ),
            ),
            cast_to=MarketplaceListResponse,
        )

    async def retrieve(
        self,
        skill_id: str,
        *,
        source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketplaceRetrieveResponse:
        """
        Retrieve the files and content hash for a marketplace skill. This does not install the skill.

        Args:
            skill_id: Path parameter.
            source: The source repository in owner/repo format. Domain-only sources cannot be downloaded and return 404.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MarketplaceRetrieveResponse: Retrieve a marketplace skill

        Example:
            ```python
            marketplace = await client.skills.marketplace.retrieve(
                skill_id="skillId",
                source="source",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._get(
            path_template("/v1/skills/marketplace/{skillId}", **{"skillId": skill_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"source": source}, marketplace_retrieve_params.MarketplaceRetrieveParams
                ),
            ),
            cast_to=MarketplaceRetrieveResponse,
        )


class MarketplaceResourceWithRawResponse:
    def __init__(self, marketplace: MarketplaceResource) -> None:
        self._marketplace = marketplace

        self.list = to_raw_response_wrapper(
            marketplace.list,
        )
        self.retrieve = to_raw_response_wrapper(
            marketplace.retrieve,
        )


class AsyncMarketplaceResourceWithRawResponse:
    def __init__(self, marketplace: AsyncMarketplaceResource) -> None:
        self._marketplace = marketplace

        self.list = async_to_raw_response_wrapper(
            marketplace.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            marketplace.retrieve,
        )


class MarketplaceResourceWithStreamingResponse:
    def __init__(self, marketplace: MarketplaceResource) -> None:
        self._marketplace = marketplace

        self.list = to_streamed_response_wrapper(
            marketplace.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            marketplace.retrieve,
        )


class AsyncMarketplaceResourceWithStreamingResponse:
    def __init__(self, marketplace: AsyncMarketplaceResource) -> None:
        self._marketplace = marketplace

        self.list = async_to_streamed_response_wrapper(
            marketplace.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            marketplace.retrieve,
        )
