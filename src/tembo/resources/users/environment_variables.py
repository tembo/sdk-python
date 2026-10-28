# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.users.environment_variable_list_response import EnvironmentVariableListResponse
from ...types.users.environment_variable_create_response import EnvironmentVariableCreateResponse
from ...types.users import environment_variable_create_params
from ...types.users.environment_variable_delete_response import EnvironmentVariableDeleteResponse

__all__ = ["EnvironmentVariablesResource", "AsyncEnvironmentVariablesResource"]


class EnvironmentVariablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentVariablesResourceWithRawResponse:
        return EnvironmentVariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentVariablesResourceWithStreamingResponse:
        return EnvironmentVariablesResourceWithStreamingResponse(self)

    def list(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableListResponse:
        """
        List your personal environment variables in the current organization. Values are never returned.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableListResponse: List personal environment variables

        Example:
            ```python
            environment_variable = client.users.environment_variables.list(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{userId}/environment-variables", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableListResponse,
        )

    def create(
        self,
        user_id: str,
        *,
        key: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableCreateResponse:
        """
        Store an encrypted environment variable that is injected into every session you start in the current organization.

        Args:
            user_id: Path parameter.
            key: Environment variable name, e.g. GITHUB_TOKEN.
            value: Plaintext value to encrypt and store. List operations never return it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableCreateResponse: Create a personal environment variable

        Example:
            ```python
            environment_variable = client.users.environment_variables.create(
                user_id="userId",
                key="x",
                value="x",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{userId}/environment-variables", **{"userId": user_id}),
            body=maybe_transform(
                {
                    "key": key,
                    "value": value,
                },
                environment_variable_create_params.EnvironmentVariableCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableCreateResponse,
        )

    def delete(
        self,
        environment_variable_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableDeleteResponse:
        """
        Permanently delete a personal environment variable. Sessions started afterwards no longer receive it.

        Args:
            environment_variable_id: Path parameter.
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableDeleteResponse: Delete a personal environment variable

        Example:
            ```python
            environment_variable = client.users.environment_variables.delete(
                user_id="userId",
                environment_variable_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if environment_variable_id is None or (
            isinstance(environment_variable_id, str) and not environment_variable_id
        ):
            raise ValueError(
                f"Expected a non-empty value for `environment_variable_id` but received {environment_variable_id!r}"
            )
        return self._delete(
            path_template(
                "/v1/users/{userId}/environment-variables/{environmentVariableId}",
                **{"userId": user_id, "environmentVariableId": environment_variable_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableDeleteResponse,
        )


class AsyncEnvironmentVariablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentVariablesResourceWithRawResponse:
        return AsyncEnvironmentVariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentVariablesResourceWithStreamingResponse:
        return AsyncEnvironmentVariablesResourceWithStreamingResponse(self)

    async def list(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableListResponse:
        """
        List your personal environment variables in the current organization. Values are never returned.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableListResponse: List personal environment variables

        Example:
            ```python
            environment_variable = await client.users.environment_variables.list(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{userId}/environment-variables", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableListResponse,
        )

    async def create(
        self,
        user_id: str,
        *,
        key: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableCreateResponse:
        """
        Store an encrypted environment variable that is injected into every session you start in the current organization.

        Args:
            user_id: Path parameter.
            key: Environment variable name, e.g. GITHUB_TOKEN.
            value: Plaintext value to encrypt and store. List operations never return it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableCreateResponse: Create a personal environment variable

        Example:
            ```python
            environment_variable = await client.users.environment_variables.create(
                user_id="userId",
                key="x",
                value="x",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{userId}/environment-variables", **{"userId": user_id}),
            body=await async_maybe_transform(
                {
                    "key": key,
                    "value": value,
                },
                environment_variable_create_params.EnvironmentVariableCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableCreateResponse,
        )

    async def delete(
        self,
        environment_variable_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableDeleteResponse:
        """
        Permanently delete a personal environment variable. Sessions started afterwards no longer receive it.

        Args:
            environment_variable_id: Path parameter.
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableDeleteResponse: Delete a personal environment variable

        Example:
            ```python
            environment_variable = await client.users.environment_variables.delete(
                user_id="userId",
                environment_variable_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if environment_variable_id is None or (
            isinstance(environment_variable_id, str) and not environment_variable_id
        ):
            raise ValueError(
                f"Expected a non-empty value for `environment_variable_id` but received {environment_variable_id!r}"
            )
        return await self._delete(
            path_template(
                "/v1/users/{userId}/environment-variables/{environmentVariableId}",
                **{"userId": user_id, "environmentVariableId": environment_variable_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableDeleteResponse,
        )


class EnvironmentVariablesResourceWithRawResponse:
    def __init__(self, environment_variables: EnvironmentVariablesResource) -> None:
        self._environment_variables = environment_variables

        self.list = to_raw_response_wrapper(
            environment_variables.list,
        )
        self.create = to_raw_response_wrapper(
            environment_variables.create,
        )
        self.delete = to_raw_response_wrapper(
            environment_variables.delete,
        )


class AsyncEnvironmentVariablesResourceWithRawResponse:
    def __init__(self, environment_variables: AsyncEnvironmentVariablesResource) -> None:
        self._environment_variables = environment_variables

        self.list = async_to_raw_response_wrapper(
            environment_variables.list,
        )
        self.create = async_to_raw_response_wrapper(
            environment_variables.create,
        )
        self.delete = async_to_raw_response_wrapper(
            environment_variables.delete,
        )


class EnvironmentVariablesResourceWithStreamingResponse:
    def __init__(self, environment_variables: EnvironmentVariablesResource) -> None:
        self._environment_variables = environment_variables

        self.list = to_streamed_response_wrapper(
            environment_variables.list,
        )
        self.create = to_streamed_response_wrapper(
            environment_variables.create,
        )
        self.delete = to_streamed_response_wrapper(
            environment_variables.delete,
        )


class AsyncEnvironmentVariablesResourceWithStreamingResponse:
    def __init__(self, environment_variables: AsyncEnvironmentVariablesResource) -> None:
        self._environment_variables = environment_variables

        self.list = async_to_streamed_response_wrapper(
            environment_variables.list,
        )
        self.create = async_to_streamed_response_wrapper(
            environment_variables.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            environment_variables.delete,
        )
