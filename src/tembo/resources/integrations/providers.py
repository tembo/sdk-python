# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.integrations.provider_list_response import ProviderListResponse
from ...types.integrations import provider_list_params, provider_discover_snyk_organizations_params
from ...types.integrations.provider_discover_snyk_organizations_response import (
    ProviderDiscoverSnykOrganizationsResponse,
)

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        return ProvidersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        return_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        List providers available to the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            return_url: URL to return to after provider authorization. Must use HTTPS or localhost HTTP.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProviderListResponse: List integration providers

        Example:
            ```python
            provider = client.integrations.providers.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/integrations/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "return_url": return_url},
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )

    def discover_snyk_organizations(
        self,
        *,
        client_id: str,
        client_secret: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderDiscoverSnykOrganizationsResponse:
        """
        Validate Snyk service-account credentials and list accessible organizations.

        Args:
            client_id: Snyk service-account client ID to validate and use for organization discovery.
            client_secret: Snyk service-account client secret. Used for discovery without saving an integration.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProviderDiscoverSnykOrganizationsResponse: Discover Snyk organizations

        Example:
            ```python
            provider = client.integrations.providers.discover_snyk_organizations(
                client_id="x",
                client_secret="x",
                limit=50,
            )
            ```
        """
        return self._post(
            "/v1/integrations/providers/snyk/organizations",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "cursor": cursor,
                    "limit": limit,
                },
                provider_discover_snyk_organizations_params.ProviderDiscoverSnykOrganizationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderDiscoverSnykOrganizationsResponse,
        )


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        return AsyncProvidersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        return_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        List providers available to the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            return_url: URL to return to after provider authorization. Must use HTTPS or localhost HTTP.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProviderListResponse: List integration providers

        Example:
            ```python
            provider = await client.integrations.providers.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/integrations/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "return_url": return_url},
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )

    async def discover_snyk_organizations(
        self,
        *,
        client_id: str,
        client_secret: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderDiscoverSnykOrganizationsResponse:
        """
        Validate Snyk service-account credentials and list accessible organizations.

        Args:
            client_id: Snyk service-account client ID to validate and use for organization discovery.
            client_secret: Snyk service-account client secret. Used for discovery without saving an integration.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProviderDiscoverSnykOrganizationsResponse: Discover Snyk organizations

        Example:
            ```python
            provider = await client.integrations.providers.discover_snyk_organizations(
                client_id="x",
                client_secret="x",
                limit=50,
            )
            ```
        """
        return await self._post(
            "/v1/integrations/providers/snyk/organizations",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "cursor": cursor,
                    "limit": limit,
                },
                provider_discover_snyk_organizations_params.ProviderDiscoverSnykOrganizationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderDiscoverSnykOrganizationsResponse,
        )


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.list = to_raw_response_wrapper(
            providers.list,
        )
        self.discover_snyk_organizations = to_raw_response_wrapper(
            providers.discover_snyk_organizations,
        )


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.list = async_to_raw_response_wrapper(
            providers.list,
        )
        self.discover_snyk_organizations = async_to_raw_response_wrapper(
            providers.discover_snyk_organizations,
        )


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.list = to_streamed_response_wrapper(
            providers.list,
        )
        self.discover_snyk_organizations = to_streamed_response_wrapper(
            providers.discover_snyk_organizations,
        )


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.list = async_to_streamed_response_wrapper(
            providers.list,
        )
        self.discover_snyk_organizations = async_to_streamed_response_wrapper(
            providers.discover_snyk_organizations,
        )
