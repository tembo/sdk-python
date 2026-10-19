# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional, Union
from datetime import datetime

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.api_key_list_response import APIKeyListResponse
from ..types import api_key_list_params, api_key_create_params, api_key_update_params
from ..types.api_key_create_response import APIKeyCreateResponse
from ..types.api_key_retrieve_response import APIKeyRetrieveResponse
from ..types.api_key_update_response import APIKeyUpdateResponse
from ..types.api_key_delete_response import APIKeyDeleteResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """
        List active API keys for the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyListResponse: List API keys

        Example:
            ```python
            api_key = client.api_keys.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/api-keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, api_key_list_params.APIKeyListParams),
            ),
            cast_to=APIKeyListResponse,
        )

    def create(
        self,
        *,
        expires_at: Optional[Union[str, datetime]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateResponse:
        """
        Create an API key for the current organization. Optionally set `expiresAt` to a future timestamp after which the key stops authenticating requests. The complete token is returned only by this operation.

        Args:
            expires_at: Future ISO 8601 expiration timestamp. Omit or use null for a key that does not expire.
            name: Display name for identifying this API key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyCreateResponse: Create an API key

        Example:
            ```python
            api_key = client.api_keys.create()
            ```
        """
        return self._post(
            "/v1/api-keys",
            body=maybe_transform(
                {
                    "expires_at": expires_at,
                    "name": name,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyCreateResponse,
        )

    def retrieve(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRetrieveResponse:
        """
        Retrieve an active API key without exposing its complete token.

        Args:
            api_key_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyRetrieveResponse: Retrieve an API key

        Example:
            ```python
            api_key = client.api_keys.retrieve(
                api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if api_key_id is None or (isinstance(api_key_id, str) and not api_key_id):
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return self._get(
            path_template("/v1/api-keys/{apiKeyId}", **{"apiKeyId": api_key_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRetrieveResponse,
        )

    def update(
        self,
        api_key_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyUpdateResponse:
        """
        Rename an active API key.

        Args:
            api_key_id: Path parameter.
            name: New display name for the API key. This does not rotate its token.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyUpdateResponse: Update an API key

        Example:
            ```python
            api_key = client.api_keys.update(
                api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if api_key_id is None or (isinstance(api_key_id, str) and not api_key_id):
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return self._patch(
            path_template("/v1/api-keys/{apiKeyId}", **{"apiKeyId": api_key_id}),
            body=maybe_transform(
                {"name": name},
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyUpdateResponse,
        )

    def delete(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyDeleteResponse:
        """
        Revoke an active API key so it can no longer authenticate requests.

        Args:
            api_key_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyDeleteResponse: Delete an API key

        Example:
            ```python
            api_key = client.api_keys.delete(
                api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if api_key_id is None or (isinstance(api_key_id, str) and not api_key_id):
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return self._delete(
            path_template("/v1/api-keys/{apiKeyId}", **{"apiKeyId": api_key_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyDeleteResponse,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """
        List active API keys for the current organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyListResponse: List API keys

        Example:
            ```python
            api_key = await client.api_keys.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/api-keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, api_key_list_params.APIKeyListParams
                ),
            ),
            cast_to=APIKeyListResponse,
        )

    async def create(
        self,
        *,
        expires_at: Optional[Union[str, datetime]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateResponse:
        """
        Create an API key for the current organization. Optionally set `expiresAt` to a future timestamp after which the key stops authenticating requests. The complete token is returned only by this operation.

        Args:
            expires_at: Future ISO 8601 expiration timestamp. Omit or use null for a key that does not expire.
            name: Display name for identifying this API key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyCreateResponse: Create an API key

        Example:
            ```python
            api_key = await client.api_keys.create()
            ```
        """
        return await self._post(
            "/v1/api-keys",
            body=await async_maybe_transform(
                {
                    "expires_at": expires_at,
                    "name": name,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyCreateResponse,
        )

    async def retrieve(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRetrieveResponse:
        """
        Retrieve an active API key without exposing its complete token.

        Args:
            api_key_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyRetrieveResponse: Retrieve an API key

        Example:
            ```python
            api_key = await client.api_keys.retrieve(
                api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if api_key_id is None or (isinstance(api_key_id, str) and not api_key_id):
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return await self._get(
            path_template("/v1/api-keys/{apiKeyId}", **{"apiKeyId": api_key_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRetrieveResponse,
        )

    async def update(
        self,
        api_key_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyUpdateResponse:
        """
        Rename an active API key.

        Args:
            api_key_id: Path parameter.
            name: New display name for the API key. This does not rotate its token.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyUpdateResponse: Update an API key

        Example:
            ```python
            api_key = await client.api_keys.update(
                api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if api_key_id is None or (isinstance(api_key_id, str) and not api_key_id):
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return await self._patch(
            path_template("/v1/api-keys/{apiKeyId}", **{"apiKeyId": api_key_id}),
            body=await async_maybe_transform(
                {"name": name},
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyUpdateResponse,
        )

    async def delete(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyDeleteResponse:
        """
        Revoke an active API key so it can no longer authenticate requests.

        Args:
            api_key_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            APIKeyDeleteResponse: Delete an API key

        Example:
            ```python
            api_key = await client.api_keys.delete(
                api_key_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if api_key_id is None or (isinstance(api_key_id, str) and not api_key_id):
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return await self._delete(
            path_template("/v1/api-keys/{apiKeyId}", **{"apiKeyId": api_key_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyDeleteResponse,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            api_keys.update,
        )
        self.delete = to_raw_response_wrapper(
            api_keys.delete,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            api_keys.update,
        )
        self.delete = async_to_raw_response_wrapper(
            api_keys.delete,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            api_keys.update,
        )
        self.delete = to_streamed_response_wrapper(
            api_keys.delete,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            api_keys.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_keys.delete,
        )
