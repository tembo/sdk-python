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
from ...types.users.connected_account_list_response import ConnectedAccountListResponse
from ...types.users import connected_account_list_params
from ...types.users.connected_account_retrieve_response import ConnectedAccountRetrieveResponse

__all__ = ["ConnectedAccountsResource", "AsyncConnectedAccountsResource"]


class ConnectedAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectedAccountsResourceWithRawResponse:
        return ConnectedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectedAccountsResourceWithStreamingResponse:
        return ConnectedAccountsResourceWithStreamingResponse(self)

    def list(
        self,
        user_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedAccountListResponse:
        """
        List the user identity-provider accounts without returning credentials.

        Args:
            user_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ConnectedAccountListResponse: List user connected accounts

        Example:
            ```python
            connected_account = client.users.connected_accounts.list(
                user_id="userId",
                limit=50,
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{userId}/connected-accounts", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit}, connected_account_list_params.ConnectedAccountListParams
                ),
            ),
            cast_to=ConnectedAccountListResponse,
        )

    def retrieve(
        self,
        connected_account_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedAccountRetrieveResponse:
        """
        Retrieve one identity-provider account without returning credentials.

        Args:
            connected_account_id: Path parameter.
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ConnectedAccountRetrieveResponse: Retrieve a user connected account

        Example:
            ```python
            connected_account = client.users.connected_accounts.retrieve(
                user_id="userId",
                connected_account_id="connectedAccountId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if connected_account_id is None or (isinstance(connected_account_id, str) and not connected_account_id):
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return self._get(
            path_template(
                "/v1/users/{userId}/connected-accounts/{connectedAccountId}",
                **{"userId": user_id, "connectedAccountId": connected_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountRetrieveResponse,
        )


class AsyncConnectedAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectedAccountsResourceWithRawResponse:
        return AsyncConnectedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectedAccountsResourceWithStreamingResponse:
        return AsyncConnectedAccountsResourceWithStreamingResponse(self)

    async def list(
        self,
        user_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedAccountListResponse:
        """
        List the user identity-provider accounts without returning credentials.

        Args:
            user_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ConnectedAccountListResponse: List user connected accounts

        Example:
            ```python
            connected_account = await client.users.connected_accounts.list(
                user_id="userId",
                limit=50,
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{userId}/connected-accounts", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, connected_account_list_params.ConnectedAccountListParams
                ),
            ),
            cast_to=ConnectedAccountListResponse,
        )

    async def retrieve(
        self,
        connected_account_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedAccountRetrieveResponse:
        """
        Retrieve one identity-provider account without returning credentials.

        Args:
            connected_account_id: Path parameter.
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ConnectedAccountRetrieveResponse: Retrieve a user connected account

        Example:
            ```python
            connected_account = await client.users.connected_accounts.retrieve(
                user_id="userId",
                connected_account_id="connectedAccountId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if connected_account_id is None or (isinstance(connected_account_id, str) and not connected_account_id):
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return await self._get(
            path_template(
                "/v1/users/{userId}/connected-accounts/{connectedAccountId}",
                **{"userId": user_id, "connectedAccountId": connected_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccountRetrieveResponse,
        )


class ConnectedAccountsResourceWithRawResponse:
    def __init__(self, connected_accounts: ConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.list = to_raw_response_wrapper(
            connected_accounts.list,
        )
        self.retrieve = to_raw_response_wrapper(
            connected_accounts.retrieve,
        )


class AsyncConnectedAccountsResourceWithRawResponse:
    def __init__(self, connected_accounts: AsyncConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.list = async_to_raw_response_wrapper(
            connected_accounts.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connected_accounts.retrieve,
        )


class ConnectedAccountsResourceWithStreamingResponse:
    def __init__(self, connected_accounts: ConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.list = to_streamed_response_wrapper(
            connected_accounts.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            connected_accounts.retrieve,
        )


class AsyncConnectedAccountsResourceWithStreamingResponse:
    def __init__(self, connected_accounts: AsyncConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.list = async_to_streamed_response_wrapper(
            connected_accounts.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connected_accounts.retrieve,
        )
