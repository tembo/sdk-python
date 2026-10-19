# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List
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
from ...types.projects.build_list_response import BuildListResponse
from ...types.projects import build_list_params, build_create_params
from ...types.projects.build_create_response import BuildCreateResponse
from ...types.projects.build_retrieve_response import BuildRetrieveResponse
from ...types.projects.build_cancel_response import BuildCancelResponse

__all__ = ["BuildsResource", "AsyncBuildsResource"]


class BuildsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BuildsResourceWithRawResponse:
        return BuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BuildsResourceWithStreamingResponse:
        return BuildsResourceWithStreamingResponse(self)

    def list(
        self,
        project_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildListResponse:
        """
        List recent queued, running, and failed project builds.

        Args:
            project_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildListResponse: List project builds

        Example:
            ```python
            build = client.projects.builds.list(
                project_id="projectId",
                limit=50,
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{projectId}/builds", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, build_list_params.BuildListParams),
            ),
            cast_to=BuildListResponse,
        )

    def create(
        self,
        project_id: str,
        *,
        sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        snapshot_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildCreateResponse:
        """
        Build selected project sizes or rebuild one snapshot.

        Args:
            project_id: Path parameter.
            sizes: VM sizes to build. Omit to use the project sizes. Cannot be combined with snapshotId.
            snapshot_id: Rebuild one existing snapshot instead of building project sizes. Cannot be combined with sizes.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildCreateResponse: Create a project build

        Example:
            ```python
            build = client.projects.builds.create(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{projectId}/builds", **{"projectId": project_id}),
            body=maybe_transform(
                {
                    "sizes": sizes,
                    "snapshot_id": snapshot_id,
                },
                build_create_params.BuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildCreateResponse,
        )

    def retrieve(
        self,
        build_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildRetrieveResponse:
        """
        Retrieve project build status.

        Args:
            build_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildRetrieveResponse: Retrieve a project build

        Example:
            ```python
            build = client.projects.builds.retrieve(
                project_id="projectId",
                build_id="buildId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if build_id is None or (isinstance(build_id, str) and not build_id):
            raise ValueError(f"Expected a non-empty value for `build_id` but received {build_id!r}")
        return self._get(
            path_template(
                "/v1/projects/{projectId}/builds/{buildId}", **{"projectId": project_id, "buildId": build_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildRetrieveResponse,
        )

    def cancel(
        self,
        build_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildCancelResponse:
        """
        Cancel an active queued or running project build.

        Args:
            build_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildCancelResponse: Cancel a project build

        Example:
            ```python
            build = client.projects.builds.cancel(
                project_id="projectId",
                build_id="buildId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if build_id is None or (isinstance(build_id, str) and not build_id):
            raise ValueError(f"Expected a non-empty value for `build_id` but received {build_id!r}")
        return self._post(
            path_template(
                "/v1/projects/{projectId}/builds/{buildId}/cancel", **{"projectId": project_id, "buildId": build_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildCancelResponse,
        )


class AsyncBuildsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBuildsResourceWithRawResponse:
        return AsyncBuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBuildsResourceWithStreamingResponse:
        return AsyncBuildsResourceWithStreamingResponse(self)

    async def list(
        self,
        project_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildListResponse:
        """
        List recent queued, running, and failed project builds.

        Args:
            project_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildListResponse: List project builds

        Example:
            ```python
            build = await client.projects.builds.list(
                project_id="projectId",
                limit=50,
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{projectId}/builds", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, build_list_params.BuildListParams
                ),
            ),
            cast_to=BuildListResponse,
        )

    async def create(
        self,
        project_id: str,
        *,
        sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        snapshot_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildCreateResponse:
        """
        Build selected project sizes or rebuild one snapshot.

        Args:
            project_id: Path parameter.
            sizes: VM sizes to build. Omit to use the project sizes. Cannot be combined with snapshotId.
            snapshot_id: Rebuild one existing snapshot instead of building project sizes. Cannot be combined with sizes.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildCreateResponse: Create a project build

        Example:
            ```python
            build = await client.projects.builds.create(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{projectId}/builds", **{"projectId": project_id}),
            body=await async_maybe_transform(
                {
                    "sizes": sizes,
                    "snapshot_id": snapshot_id,
                },
                build_create_params.BuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildCreateResponse,
        )

    async def retrieve(
        self,
        build_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildRetrieveResponse:
        """
        Retrieve project build status.

        Args:
            build_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildRetrieveResponse: Retrieve a project build

        Example:
            ```python
            build = await client.projects.builds.retrieve(
                project_id="projectId",
                build_id="buildId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if build_id is None or (isinstance(build_id, str) and not build_id):
            raise ValueError(f"Expected a non-empty value for `build_id` but received {build_id!r}")
        return await self._get(
            path_template(
                "/v1/projects/{projectId}/builds/{buildId}", **{"projectId": project_id, "buildId": build_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildRetrieveResponse,
        )

    async def cancel(
        self,
        build_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildCancelResponse:
        """
        Cancel an active queued or running project build.

        Args:
            build_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BuildCancelResponse: Cancel a project build

        Example:
            ```python
            build = await client.projects.builds.cancel(
                project_id="projectId",
                build_id="buildId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if build_id is None or (isinstance(build_id, str) and not build_id):
            raise ValueError(f"Expected a non-empty value for `build_id` but received {build_id!r}")
        return await self._post(
            path_template(
                "/v1/projects/{projectId}/builds/{buildId}/cancel", **{"projectId": project_id, "buildId": build_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildCancelResponse,
        )


class BuildsResourceWithRawResponse:
    def __init__(self, builds: BuildsResource) -> None:
        self._builds = builds

        self.list = to_raw_response_wrapper(
            builds.list,
        )
        self.create = to_raw_response_wrapper(
            builds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            builds.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            builds.cancel,
        )


class AsyncBuildsResourceWithRawResponse:
    def __init__(self, builds: AsyncBuildsResource) -> None:
        self._builds = builds

        self.list = async_to_raw_response_wrapper(
            builds.list,
        )
        self.create = async_to_raw_response_wrapper(
            builds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            builds.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            builds.cancel,
        )


class BuildsResourceWithStreamingResponse:
    def __init__(self, builds: BuildsResource) -> None:
        self._builds = builds

        self.list = to_streamed_response_wrapper(
            builds.list,
        )
        self.create = to_streamed_response_wrapper(
            builds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            builds.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            builds.cancel,
        )


class AsyncBuildsResourceWithStreamingResponse:
    def __init__(self, builds: AsyncBuildsResource) -> None:
        self._builds = builds

        self.list = async_to_streamed_response_wrapper(
            builds.list,
        )
        self.create = async_to_streamed_response_wrapper(
            builds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            builds.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            builds.cancel,
        )
