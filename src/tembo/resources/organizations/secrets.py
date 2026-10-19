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
from ...types.organizations.secret_list_response import SecretListResponse
from ...types.organizations import secret_list_params, secret_create_params, secret_update_params
from ...types.organizations.secret_create_response import SecretCreateResponse
from ...types.organizations.secret_retrieve_response import SecretRetrieveResponse
from ...types.organizations.secret_update_response import SecretUpdateResponse
from ...types.organizations.secret_delete_response import SecretDeleteResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self)

    def list(
        self,
        organization_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """
        List redacted organization secret summaries with cursor pagination.

        Args:
            organization_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search secret names. Secret values are never returned.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretListResponse: List organization secrets

        Example:
            ```python
            secret = client.organizations.secrets.list(
                organization_id="organizationId",
                limit=50,
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/v1/organizations/{organizationId}/secrets", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search}, secret_list_params.SecretListParams
                ),
            ),
            cast_to=SecretListResponse,
        )

    def create(
        self,
        organization_id: str,
        *,
        key: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretCreateResponse:
        """
        Create an encrypted organization secret.

        Args:
            organization_id: Path parameter.
            key: Secret name used to reference it in the organization.
            value: Secret plaintext value to encrypt and store. Retrieve and list operations return redacted summaries, not this value.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretCreateResponse: Create an organization secret

        Example:
            ```python
            secret = client.organizations.secrets.create(
                organization_id="organizationId",
                key="x",
                value="x",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template("/v1/organizations/{organizationId}/secrets", **{"organizationId": organization_id}),
            body=maybe_transform(
                {
                    "key": key,
                    "value": value,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretCreateResponse,
        )

    def retrieve(
        self,
        secret_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveResponse:
        """
        Retrieve a redacted organization secret summary.

        Args:
            secret_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretRetrieveResponse: Retrieve an organization secret

        Example:
            ```python
            secret = client.organizations.secrets.retrieve(
                organization_id="organizationId",
                secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if secret_id is None or (isinstance(secret_id, str) and not secret_id):
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._get(
            path_template(
                "/v1/organizations/{organizationId}/secrets/{secretId}",
                **{"organizationId": organization_id, "secretId": secret_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRetrieveResponse,
        )

    def update(
        self,
        secret_id: str,
        *,
        organization_id: str,
        key: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretUpdateResponse:
        """
        Update a secret name, encrypted value, or both.

        Args:
            secret_id: Path parameter.
            organization_id: Path parameter.
            key: Secret name used to reference it in the organization.
            value: Secret plaintext value to encrypt and store. Retrieve and list operations return redacted summaries, not this value.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretUpdateResponse: Update an organization secret

        Example:
            ```python
            secret = client.organizations.secrets.update(
                organization_id="organizationId",
                secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if secret_id is None or (isinstance(secret_id, str) and not secret_id):
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._patch(
            path_template(
                "/v1/organizations/{organizationId}/secrets/{secretId}",
                **{"organizationId": organization_id, "secretId": secret_id},
            ),
            body=maybe_transform(
                {
                    "key": key,
                    "value": value,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretUpdateResponse,
        )

    def delete(
        self,
        secret_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretDeleteResponse:
        """
        Delete an organization secret.

        Args:
            secret_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretDeleteResponse: Delete an organization secret

        Example:
            ```python
            secret = client.organizations.secrets.delete(
                organization_id="organizationId",
                secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if secret_id is None or (isinstance(secret_id, str) and not secret_id):
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._delete(
            path_template(
                "/v1/organizations/{organizationId}/secrets/{secretId}",
                **{"organizationId": organization_id, "secretId": secret_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretDeleteResponse,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def list(
        self,
        organization_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """
        List redacted organization secret summaries with cursor pagination.

        Args:
            organization_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search secret names. Secret values are never returned.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretListResponse: List organization secrets

        Example:
            ```python
            secret = await client.organizations.secrets.list(
                organization_id="organizationId",
                limit=50,
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/v1/organizations/{organizationId}/secrets", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search}, secret_list_params.SecretListParams
                ),
            ),
            cast_to=SecretListResponse,
        )

    async def create(
        self,
        organization_id: str,
        *,
        key: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretCreateResponse:
        """
        Create an encrypted organization secret.

        Args:
            organization_id: Path parameter.
            key: Secret name used to reference it in the organization.
            value: Secret plaintext value to encrypt and store. Retrieve and list operations return redacted summaries, not this value.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretCreateResponse: Create an organization secret

        Example:
            ```python
            secret = await client.organizations.secrets.create(
                organization_id="organizationId",
                key="x",
                value="x",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template("/v1/organizations/{organizationId}/secrets", **{"organizationId": organization_id}),
            body=await async_maybe_transform(
                {
                    "key": key,
                    "value": value,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretCreateResponse,
        )

    async def retrieve(
        self,
        secret_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretRetrieveResponse:
        """
        Retrieve a redacted organization secret summary.

        Args:
            secret_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretRetrieveResponse: Retrieve an organization secret

        Example:
            ```python
            secret = await client.organizations.secrets.retrieve(
                organization_id="organizationId",
                secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if secret_id is None or (isinstance(secret_id, str) and not secret_id):
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._get(
            path_template(
                "/v1/organizations/{organizationId}/secrets/{secretId}",
                **{"organizationId": organization_id, "secretId": secret_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretRetrieveResponse,
        )

    async def update(
        self,
        secret_id: str,
        *,
        organization_id: str,
        key: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretUpdateResponse:
        """
        Update a secret name, encrypted value, or both.

        Args:
            secret_id: Path parameter.
            organization_id: Path parameter.
            key: Secret name used to reference it in the organization.
            value: Secret plaintext value to encrypt and store. Retrieve and list operations return redacted summaries, not this value.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretUpdateResponse: Update an organization secret

        Example:
            ```python
            secret = await client.organizations.secrets.update(
                organization_id="organizationId",
                secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if secret_id is None or (isinstance(secret_id, str) and not secret_id):
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._patch(
            path_template(
                "/v1/organizations/{organizationId}/secrets/{secretId}",
                **{"organizationId": organization_id, "secretId": secret_id},
            ),
            body=await async_maybe_transform(
                {
                    "key": key,
                    "value": value,
                },
                secret_update_params.SecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretUpdateResponse,
        )

    async def delete(
        self,
        secret_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretDeleteResponse:
        """
        Delete an organization secret.

        Args:
            secret_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SecretDeleteResponse: Delete an organization secret

        Example:
            ```python
            secret = await client.organizations.secrets.delete(
                organization_id="organizationId",
                secret_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if secret_id is None or (isinstance(secret_id, str) and not secret_id):
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._delete(
            path_template(
                "/v1/organizations/{organizationId}/secrets/{secretId}",
                **{"organizationId": organization_id, "secretId": secret_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretDeleteResponse,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            secrets.update,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            secrets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            secrets.update,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            secrets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
