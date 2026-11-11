# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

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
from ..types.folder_list_response import FolderListResponse
from ..types.folder_create_response import FolderCreateResponse
from ..types import folder_create_params, folder_update_params
from ..types.folder_update_response import FolderUpdateResponse
from ..types.folder_delete_response import FolderDeleteResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List the sidebar folders you use to organize sessions. Use listSessions with folderId to list the sessions in a folder.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderListResponse: List folders

        Example:
            ```python
            folder = client.folders.list()
            ```
        """
        return self._get(
            "/v1/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderListResponse,
        )

    def create(
        self,
        *,
        name: str,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Create a sidebar folder for organizing sessions. New folders go first in your folder list; use createPin to pin one.

        Args:
            name: Folder name shown in the sidebar.
            color: Folder icon color. Defaults to neutral.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderCreateResponse: Create a folder

        Example:
            ```python
            folder = client.folders.create(
                name="x",
            )
            ```
        """
        return self._post(
            "/v1/folders",
            body=maybe_transform(
                {
                    "name": name,
                    "color": color,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    def update(
        self,
        folder_id: str,
        *,
        name: str | Omit = omit,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        placement: folder_update_params.Placement | Omit = omit,
        add_session: folder_update_params.AddSession | Omit = omit,
        remove_session: folder_update_params.RemoveSession | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """
        Rename one of your sidebar folders, change its icon color, move it in your folder list, or add, reorder, or remove its sessions. Use updatePin to move a pinned folder among your pins.

        Args:
            folder_id: Path parameter.
            name: Folder name shown in the sidebar.
            color: Folder icon color, from the same palette as project icons.
            placement: Where to put this folder in your sidebar folder list. Pinned folders are ordered with updatePin instead.
            add_session: Session to put in this folder, taking it out of any other folder of yours, or to reorder within it.
            remove_session: Session to take out of this folder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderUpdateResponse: Update a folder

        Example:
            ```python
            folder = client.folders.update(
                folder_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._patch(
            path_template("/v1/folders/{folderId}", **{"folderId": folder_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "color": color,
                    "placement": placement,
                    "add_session": add_session,
                    "remove_session": remove_session,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete one of your sidebar folders. Its sessions are kept and return to your recent sessions.

        Args:
            folder_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteResponse: Delete a folder

        Example:
            ```python
            folder = client.folders.delete(
                folder_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._delete(
            path_template("/v1/folders/{folderId}", **{"folderId": folder_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListResponse:
        """
        List the sidebar folders you use to organize sessions. Use listSessions with folderId to list the sessions in a folder.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderListResponse: List folders

        Example:
            ```python
            folder = await client.folders.list()
            ```
        """
        return await self._get(
            "/v1/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Create a sidebar folder for organizing sessions. New folders go first in your folder list; use createPin to pin one.

        Args:
            name: Folder name shown in the sidebar.
            color: Folder icon color. Defaults to neutral.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderCreateResponse: Create a folder

        Example:
            ```python
            folder = await client.folders.create(
                name="x",
            )
            ```
        """
        return await self._post(
            "/v1/folders",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "color": color,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    async def update(
        self,
        folder_id: str,
        *,
        name: str | Omit = omit,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        placement: folder_update_params.Placement | Omit = omit,
        add_session: folder_update_params.AddSession | Omit = omit,
        remove_session: folder_update_params.RemoveSession | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """
        Rename one of your sidebar folders, change its icon color, move it in your folder list, or add, reorder, or remove its sessions. Use updatePin to move a pinned folder among your pins.

        Args:
            folder_id: Path parameter.
            name: Folder name shown in the sidebar.
            color: Folder icon color, from the same palette as project icons.
            placement: Where to put this folder in your sidebar folder list. Pinned folders are ordered with updatePin instead.
            add_session: Session to put in this folder, taking it out of any other folder of yours, or to reorder within it.
            remove_session: Session to take out of this folder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderUpdateResponse: Update a folder

        Example:
            ```python
            folder = await client.folders.update(
                folder_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._patch(
            path_template("/v1/folders/{folderId}", **{"folderId": folder_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "color": color,
                    "placement": placement,
                    "add_session": add_session,
                    "remove_session": remove_session,
                },
                folder_update_params.FolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete one of your sidebar folders. Its sessions are kept and return to your recent sessions.

        Args:
            folder_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteResponse: Delete a folder

        Example:
            ```python
            folder = await client.folders.delete(
                folder_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if folder_id is None or (isinstance(folder_id, str) and not folder_id):
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._delete(
            path_template("/v1/folders/{folderId}", **{"folderId": folder_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.list = to_raw_response_wrapper(
            folders.list,
        )
        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.update = to_raw_response_wrapper(
            folders.update,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.list = async_to_raw_response_wrapper(
            folders.list,
        )
        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.update = async_to_raw_response_wrapper(
            folders.update,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.list = to_streamed_response_wrapper(
            folders.list,
        )
        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.update = to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.list = async_to_streamed_response_wrapper(
            folders.list,
        )
        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.update = async_to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
