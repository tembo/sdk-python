# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

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
from ...types.organizations.subscription_retrieve_response import SubscriptionRetrieveResponse
from ...types.organizations.subscription_reset_response import SubscriptionResetResponse
from ...types.organizations import subscription_reset_params

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionRetrieveResponse:
        """
        Retrieve connection statuses and available ChatGPT and Claude usage. Provider usage errors are reported without failing the response.

        Args:
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubscriptionRetrieveResponse: Retrieve organization subscriptions

        Example:
            ```python
            subscription = client.organizations.subscriptions.retrieve(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/v1/organizations/{organizationId}/subscriptions", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveResponse,
        )

    def reset(
        self,
        organization_id: str,
        *,
        idempotency_key: str,
        provider: Literal["chatgpt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResetResponse:
        """
        Redeem an earned ChatGPT rate-limit reset.

        Args:
            organization_id: Path parameter.
            idempotency_key: Unique UUID for this reset attempt. Reuse the same UUID when retrying to avoid redeeming another reset credit.
            provider: Subscription provider whose rate-limit reset credit to redeem. Currently only chatgpt is supported.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubscriptionResetResponse: Reset organization subscription usage

        Example:
            ```python
            subscription = client.organizations.subscriptions.reset(
                organization_id="organizationId",
                idempotency_key="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                provider="chatgpt",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template(
                "/v1/organizations/{organizationId}/subscriptions/reset", **{"organizationId": organization_id}
            ),
            body=maybe_transform(
                {
                    "idempotency_key": idempotency_key,
                    "provider": provider,
                },
                subscription_reset_params.SubscriptionResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResetResponse,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionRetrieveResponse:
        """
        Retrieve connection statuses and available ChatGPT and Claude usage. Provider usage errors are reported without failing the response.

        Args:
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubscriptionRetrieveResponse: Retrieve organization subscriptions

        Example:
            ```python
            subscription = await client.organizations.subscriptions.retrieve(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/v1/organizations/{organizationId}/subscriptions", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveResponse,
        )

    async def reset(
        self,
        organization_id: str,
        *,
        idempotency_key: str,
        provider: Literal["chatgpt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResetResponse:
        """
        Redeem an earned ChatGPT rate-limit reset.

        Args:
            organization_id: Path parameter.
            idempotency_key: Unique UUID for this reset attempt. Reuse the same UUID when retrying to avoid redeeming another reset credit.
            provider: Subscription provider whose rate-limit reset credit to redeem. Currently only chatgpt is supported.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SubscriptionResetResponse: Reset organization subscription usage

        Example:
            ```python
            subscription = await client.organizations.subscriptions.reset(
                organization_id="organizationId",
                idempotency_key="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                provider="chatgpt",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template(
                "/v1/organizations/{organizationId}/subscriptions/reset", **{"organizationId": organization_id}
            ),
            body=await async_maybe_transform(
                {
                    "idempotency_key": idempotency_key,
                    "provider": provider,
                },
                subscription_reset_params.SubscriptionResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResetResponse,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.retrieve = to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.reset = to_raw_response_wrapper(
            subscriptions.reset,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.retrieve = async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.reset = async_to_raw_response_wrapper(
            subscriptions.reset,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.retrieve = to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.reset = to_streamed_response_wrapper(
            subscriptions.reset,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.retrieve = async_to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.reset = async_to_streamed_response_wrapper(
            subscriptions.reset,
        )
