# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional

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
from ...types.projects.snapshot_list_response import SnapshotListResponse
from ...types.projects import snapshot_list_params, snapshot_update_params
from ...types.projects.snapshot_retrieve_response import SnapshotRetrieveResponse
from ...types.projects.snapshot_update_response import SnapshotUpdateResponse
from ...types.projects.snapshot_delete_response import SnapshotDeleteResponse

__all__ = ["SnapshotsResource", "AsyncSnapshotsResource"]


class SnapshotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self)

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
    ) -> SnapshotListResponse:
        """
        List recent VM snapshots built for a project.

        Args:
            project_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotListResponse: List project snapshots

        Example:
            ```python
            snapshot = client.projects.snapshots.list(
                project_id="projectId",
                limit=50,
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{projectId}/snapshots", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, snapshot_list_params.SnapshotListParams),
            ),
            cast_to=SnapshotListResponse,
        )

    def retrieve(
        self,
        snapshot_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        Retrieve one project snapshot.

        Args:
            snapshot_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotRetrieveResponse: Retrieve a project snapshot

        Example:
            ```python
            snapshot = client.projects.snapshots.retrieve(
                project_id="projectId",
                snapshot_id="snapshotId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if snapshot_id is None or (isinstance(snapshot_id, str) and not snapshot_id):
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._get(
            path_template(
                "/v1/projects/{projectId}/snapshots/{snapshotId}",
                **{"projectId": project_id, "snapshotId": snapshot_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    def update(
        self,
        snapshot_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        pinned: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotUpdateResponse:
        """
        Rename a snapshot or choose whether it is pinned.

        Args:
            snapshot_id: Path parameter.
            project_id: Path parameter.
            name: Rename the snapshot, or null to clear its name.
            pinned: Pin the snapshot with true to retain it, or unpin with false. This is separate from user sidebar resource pins.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotUpdateResponse: Update a project snapshot

        Example:
            ```python
            snapshot = client.projects.snapshots.update(
                project_id="projectId",
                snapshot_id="snapshotId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if snapshot_id is None or (isinstance(snapshot_id, str) and not snapshot_id):
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._patch(
            path_template(
                "/v1/projects/{projectId}/snapshots/{snapshotId}",
                **{"projectId": project_id, "snapshotId": snapshot_id},
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "pinned": pinned,
                },
                snapshot_update_params.SnapshotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotUpdateResponse,
        )

    def delete(
        self,
        snapshot_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotDeleteResponse:
        """
        Delete a project snapshot.

        Args:
            snapshot_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotDeleteResponse: Delete a project snapshot

        Example:
            ```python
            snapshot = client.projects.snapshots.delete(
                project_id="projectId",
                snapshot_id="snapshotId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if snapshot_id is None or (isinstance(snapshot_id, str) and not snapshot_id):
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._delete(
            path_template(
                "/v1/projects/{projectId}/snapshots/{snapshotId}",
                **{"projectId": project_id, "snapshotId": snapshot_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotDeleteResponse,
        )


class AsyncSnapshotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self)

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
    ) -> SnapshotListResponse:
        """
        List recent VM snapshots built for a project.

        Args:
            project_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotListResponse: List project snapshots

        Example:
            ```python
            snapshot = await client.projects.snapshots.list(
                project_id="projectId",
                limit=50,
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{projectId}/snapshots", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, snapshot_list_params.SnapshotListParams
                ),
            ),
            cast_to=SnapshotListResponse,
        )

    async def retrieve(
        self,
        snapshot_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotRetrieveResponse:
        """
        Retrieve one project snapshot.

        Args:
            snapshot_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotRetrieveResponse: Retrieve a project snapshot

        Example:
            ```python
            snapshot = await client.projects.snapshots.retrieve(
                project_id="projectId",
                snapshot_id="snapshotId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if snapshot_id is None or (isinstance(snapshot_id, str) and not snapshot_id):
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._get(
            path_template(
                "/v1/projects/{projectId}/snapshots/{snapshotId}",
                **{"projectId": project_id, "snapshotId": snapshot_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotRetrieveResponse,
        )

    async def update(
        self,
        snapshot_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        pinned: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotUpdateResponse:
        """
        Rename a snapshot or choose whether it is pinned.

        Args:
            snapshot_id: Path parameter.
            project_id: Path parameter.
            name: Rename the snapshot, or null to clear its name.
            pinned: Pin the snapshot with true to retain it, or unpin with false. This is separate from user sidebar resource pins.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotUpdateResponse: Update a project snapshot

        Example:
            ```python
            snapshot = await client.projects.snapshots.update(
                project_id="projectId",
                snapshot_id="snapshotId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if snapshot_id is None or (isinstance(snapshot_id, str) and not snapshot_id):
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._patch(
            path_template(
                "/v1/projects/{projectId}/snapshots/{snapshotId}",
                **{"projectId": project_id, "snapshotId": snapshot_id},
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "pinned": pinned,
                },
                snapshot_update_params.SnapshotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotUpdateResponse,
        )

    async def delete(
        self,
        snapshot_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotDeleteResponse:
        """
        Delete a project snapshot.

        Args:
            snapshot_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SnapshotDeleteResponse: Delete a project snapshot

        Example:
            ```python
            snapshot = await client.projects.snapshots.delete(
                project_id="projectId",
                snapshot_id="snapshotId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if snapshot_id is None or (isinstance(snapshot_id, str) and not snapshot_id):
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._delete(
            path_template(
                "/v1/projects/{projectId}/snapshots/{snapshotId}",
                **{"projectId": project_id, "snapshotId": snapshot_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapshotDeleteResponse,
        )


class SnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = to_raw_response_wrapper(
            snapshots.list,
        )
        self.retrieve = to_raw_response_wrapper(
            snapshots.retrieve,
        )
        self.update = to_raw_response_wrapper(
            snapshots.update,
        )
        self.delete = to_raw_response_wrapper(
            snapshots.delete,
        )


class AsyncSnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = async_to_raw_response_wrapper(
            snapshots.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            snapshots.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            snapshots.update,
        )
        self.delete = async_to_raw_response_wrapper(
            snapshots.delete,
        )


class SnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = to_streamed_response_wrapper(
            snapshots.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            snapshots.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            snapshots.update,
        )
        self.delete = to_streamed_response_wrapper(
            snapshots.delete,
        )


class AsyncSnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.list = async_to_streamed_response_wrapper(
            snapshots.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            snapshots.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            snapshots.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            snapshots.delete,
        )
