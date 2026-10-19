# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable

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
from ...types.projects.environment_variable_list_response import EnvironmentVariableListResponse
from ...types.projects.environment_variable_create_response import EnvironmentVariableCreateResponse
from ...types.projects import environment_variable_create_params
from ...types.projects.environment_variable_delete_response import EnvironmentVariableDeleteResponse

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
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableListResponse:
        """
        List environment-variable names without exposing values.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableListResponse: List project environment variables

        Example:
            ```python
            environment_variable = client.projects.environment_variables.list(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{projectId}/environment-variables", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableListResponse,
        )

    def create(
        self,
        project_id: str,
        *,
        secrets: Iterable[environment_variable_create_params.Secret],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableCreateResponse:
        """
        Create one or more encrypted project environment variables.

        Args:
            project_id: Path parameter.
            secrets: Environment variables to add or replace by key, preserving other keys. Values are encrypted and not returned by list operations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableCreateResponse: Create project environment variables

        Example:
            ```python
            environment_variable = client.projects.environment_variables.create(
                project_id="projectId",
                secrets=[{"key": "", "value": "x"}],
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{projectId}/environment-variables", **{"projectId": project_id}),
            body=maybe_transform(
                {"secrets": secrets},
                environment_variable_create_params.EnvironmentVariableCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableCreateResponse,
        )

    def delete(
        self,
        key: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableDeleteResponse:
        """
        Delete one encrypted project environment variable.

        Args:
            key: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableDeleteResponse: Delete a project environment variable

        Example:
            ```python
            environment_variable = client.projects.environment_variables.delete(
                project_id="projectId",
                key="key",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if key is None or (isinstance(key, str) and not key):
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._delete(
            path_template(
                "/v1/projects/{projectId}/environment-variables/{key}", **{"projectId": project_id, "key": key}
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
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableListResponse:
        """
        List environment-variable names without exposing values.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableListResponse: List project environment variables

        Example:
            ```python
            environment_variable = await client.projects.environment_variables.list(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{projectId}/environment-variables", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableListResponse,
        )

    async def create(
        self,
        project_id: str,
        *,
        secrets: Iterable[environment_variable_create_params.Secret],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableCreateResponse:
        """
        Create one or more encrypted project environment variables.

        Args:
            project_id: Path parameter.
            secrets: Environment variables to add or replace by key, preserving other keys. Values are encrypted and not returned by list operations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableCreateResponse: Create project environment variables

        Example:
            ```python
            environment_variable = await client.projects.environment_variables.create(
                project_id="projectId",
                secrets=[{"key": "", "value": "x"}],
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{projectId}/environment-variables", **{"projectId": project_id}),
            body=await async_maybe_transform(
                {"secrets": secrets},
                environment_variable_create_params.EnvironmentVariableCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentVariableCreateResponse,
        )

    async def delete(
        self,
        key: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentVariableDeleteResponse:
        """
        Delete one encrypted project environment variable.

        Args:
            key: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            EnvironmentVariableDeleteResponse: Delete a project environment variable

        Example:
            ```python
            environment_variable = await client.projects.environment_variables.delete(
                project_id="projectId",
                key="key",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if key is None or (isinstance(key, str) and not key):
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._delete(
            path_template(
                "/v1/projects/{projectId}/environment-variables/{key}", **{"projectId": project_id, "key": key}
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
