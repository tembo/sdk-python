# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.sessions.source_list_response import SourceListResponse
from ...types.sessions import source_list_params
from ...types.sessions.source_retrieve_response import SourceRetrieveResponse

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        return SourcesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        enabled: bool | Omit = omit,
        include_total: bool | Omit = omit,
        integration_id: str | Omit = omit,
        search: str | Omit = omit,
        session_id: str | Omit = omit,
        types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """
        List session sources in the authenticated organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            enabled: Filter by whether the source is enabled.
            include_total: Include totalCount for matching sources.
            integration_id: Filter sources belonging to this integration.
            search: Search session source names or types.
            session_id: Find the source associated with an accessible session.
            types: Filter source types, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SourceListResponse: List session sources

        Example:
            ```python
            source = client.sessions.sources.list(
                limit=50,
                include_total=False,
            )
            ```
        """
        return self._get(
            "/v1/sessions/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "enabled": enabled,
                        "include_total": include_total,
                        "integration_id": integration_id,
                        "search": search,
                        "session_id": session_id,
                        "types": types,
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceListResponse,
        )

    def retrieve(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRetrieveResponse:
        """
        Retrieve one session source.

        Args:
            source_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SourceRetrieveResponse: Retrieve a session source

        Example:
            ```python
            source = client.sessions.sources.retrieve(
                source_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if source_id is None or (isinstance(source_id, str) and not source_id):
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            path_template("/v1/sessions/sources/{sourceId}", **{"sourceId": source_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceRetrieveResponse,
        )


class AsyncSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        enabled: bool | Omit = omit,
        include_total: bool | Omit = omit,
        integration_id: str | Omit = omit,
        search: str | Omit = omit,
        session_id: str | Omit = omit,
        types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """
        List session sources in the authenticated organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            enabled: Filter by whether the source is enabled.
            include_total: Include totalCount for matching sources.
            integration_id: Filter sources belonging to this integration.
            search: Search session source names or types.
            session_id: Find the source associated with an accessible session.
            types: Filter source types, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SourceListResponse: List session sources

        Example:
            ```python
            source = await client.sessions.sources.list(
                limit=50,
                include_total=False,
            )
            ```
        """
        return await self._get(
            "/v1/sessions/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "enabled": enabled,
                        "include_total": include_total,
                        "integration_id": integration_id,
                        "search": search,
                        "session_id": session_id,
                        "types": types,
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceListResponse,
        )

    async def retrieve(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRetrieveResponse:
        """
        Retrieve one session source.

        Args:
            source_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SourceRetrieveResponse: Retrieve a session source

        Example:
            ```python
            source = await client.sessions.sources.retrieve(
                source_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if source_id is None or (isinstance(source_id, str) and not source_id):
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            path_template("/v1/sessions/sources/{sourceId}", **{"sourceId": source_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceRetrieveResponse,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.list = to_raw_response_wrapper(
            sources.list,
        )
        self.retrieve = to_raw_response_wrapper(
            sources.retrieve,
        )


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.list = async_to_raw_response_wrapper(
            sources.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sources.retrieve,
        )


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.list = to_streamed_response_wrapper(
            sources.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            sources.retrieve,
        )


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.list = async_to_streamed_response_wrapper(
            sources.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sources.retrieve,
        )
