# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal
from .._types import SequenceNotStr

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
from ..types.repository_list_response import RepositoryListResponse
from ..types import repository_list_params, repository_update_params
from ..types.repository_retrieve_response import RepositoryRetrieveResponse
from ..types.repository_update_response import RepositoryUpdateResponse

__all__ = ["RepositoriesResource", "AsyncRepositoriesResource"]


class RepositoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        enabled: Literal["all", "true", "false"] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        integration_id: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["createdAt", "integration", "name", "pullRequests", "updatedAt"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryListResponse:
        """
        List repositories in the authenticated organization. Defaults to enabled repositories.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            enabled: Select enabled repositories, disabled repositories, or all. The public API defaults to enabled repositories.
            ids: Filter by repository IDs, supplied as a comma-separated list.
            integration_id: Filter repositories belonging to this integration.
            order: Sort direction: ascending or descending.
            search: Search repository names and owners.
            sort: Sort by creation time, integration, name, pull request count, or update time.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryListResponse: List repositories

        Example:
            ```python
            repository = client.repositories.list(
                limit=50,
                enabled="all",
                order="desc",
                sort="pullRequests",
            )
            ```
        """
        return self._get(
            "/v1/repositories",
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
                        "ids": ids,
                        "integration_id": integration_id,
                        "order": order,
                        "search": search,
                        "sort": sort,
                    },
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )

    def retrieve(
        self,
        repository_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryRetrieveResponse:
        """
        Retrieve a repository in the authenticated organization.

        Args:
            repository_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryRetrieveResponse: Retrieve a repository

        Example:
            ```python
            repository = client.repositories.retrieve(
                repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if repository_id is None or (isinstance(repository_id, str) and not repository_id):
            raise ValueError(f"Expected a non-empty value for `repository_id` but received {repository_id!r}")
        return self._get(
            path_template("/v1/repositories/{repositoryId}", **{"repositoryId": repository_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryRetrieveResponse,
        )

    def update(
        self,
        repository_id: str,
        *,
        enabled: bool | Omit = omit,
        base_branch: Optional[str] | Omit = omit,
        target_branch: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryUpdateResponse:
        """
        Update repository configuration or enable or disable it.

        Args:
            repository_id: Path parameter.
            enabled: Enable or disable this repository for Tembo. Disabled by default on creation.
            base_branch: Default Git branch to start sessions from. Null clears the override.
            target_branch: Default target branch for agent-created pull requests. Null clears the override.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryUpdateResponse: Update a repository

        Example:
            ```python
            repository = client.repositories.update(
                repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                enabled=False,
            )
            ```
        """
        if repository_id is None or (isinstance(repository_id, str) and not repository_id):
            raise ValueError(f"Expected a non-empty value for `repository_id` but received {repository_id!r}")
        return self._patch(
            path_template("/v1/repositories/{repositoryId}", **{"repositoryId": repository_id}),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "base_branch": base_branch,
                    "target_branch": target_branch,
                },
                repository_update_params.RepositoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryUpdateResponse,
        )


class AsyncRepositoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        enabled: Literal["all", "true", "false"] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        integration_id: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["createdAt", "integration", "name", "pullRequests", "updatedAt"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryListResponse:
        """
        List repositories in the authenticated organization. Defaults to enabled repositories.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            enabled: Select enabled repositories, disabled repositories, or all. The public API defaults to enabled repositories.
            ids: Filter by repository IDs, supplied as a comma-separated list.
            integration_id: Filter repositories belonging to this integration.
            order: Sort direction: ascending or descending.
            search: Search repository names and owners.
            sort: Sort by creation time, integration, name, pull request count, or update time.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryListResponse: List repositories

        Example:
            ```python
            repository = await client.repositories.list(
                limit=50,
                enabled="all",
                order="desc",
                sort="pullRequests",
            )
            ```
        """
        return await self._get(
            "/v1/repositories",
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
                        "ids": ids,
                        "integration_id": integration_id,
                        "order": order,
                        "search": search,
                        "sort": sort,
                    },
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )

    async def retrieve(
        self,
        repository_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryRetrieveResponse:
        """
        Retrieve a repository in the authenticated organization.

        Args:
            repository_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryRetrieveResponse: Retrieve a repository

        Example:
            ```python
            repository = await client.repositories.retrieve(
                repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if repository_id is None or (isinstance(repository_id, str) and not repository_id):
            raise ValueError(f"Expected a non-empty value for `repository_id` but received {repository_id!r}")
        return await self._get(
            path_template("/v1/repositories/{repositoryId}", **{"repositoryId": repository_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryRetrieveResponse,
        )

    async def update(
        self,
        repository_id: str,
        *,
        enabled: bool | Omit = omit,
        base_branch: Optional[str] | Omit = omit,
        target_branch: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryUpdateResponse:
        """
        Update repository configuration or enable or disable it.

        Args:
            repository_id: Path parameter.
            enabled: Enable or disable this repository for Tembo. Disabled by default on creation.
            base_branch: Default Git branch to start sessions from. Null clears the override.
            target_branch: Default target branch for agent-created pull requests. Null clears the override.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryUpdateResponse: Update a repository

        Example:
            ```python
            repository = await client.repositories.update(
                repository_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                enabled=False,
            )
            ```
        """
        if repository_id is None or (isinstance(repository_id, str) and not repository_id):
            raise ValueError(f"Expected a non-empty value for `repository_id` but received {repository_id!r}")
        return await self._patch(
            path_template("/v1/repositories/{repositoryId}", **{"repositoryId": repository_id}),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "base_branch": base_branch,
                    "target_branch": target_branch,
                },
                repository_update_params.RepositoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryUpdateResponse,
        )


class RepositoriesResourceWithRawResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_raw_response_wrapper(
            repositories.list,
        )
        self.retrieve = to_raw_response_wrapper(
            repositories.retrieve,
        )
        self.update = to_raw_response_wrapper(
            repositories.update,
        )


class AsyncRepositoriesResourceWithRawResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_raw_response_wrapper(
            repositories.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            repositories.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            repositories.update,
        )


class RepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_streamed_response_wrapper(
            repositories.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            repositories.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            repositories.update,
        )


class AsyncRepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_streamed_response_wrapper(
            repositories.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            repositories.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            repositories.update,
        )
