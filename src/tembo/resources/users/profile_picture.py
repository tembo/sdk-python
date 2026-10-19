# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Mapping, cast
from ..._types import FileTypes

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._files import deepcopy_with_paths
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.users.profile_picture_update_response import ProfilePictureUpdateResponse
from ...types.users import profile_picture_update_params
from ...types.users.profile_picture_delete_response import ProfilePictureDeleteResponse

__all__ = ["ProfilePictureResource", "AsyncProfilePictureResource"]


class ProfilePictureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfilePictureResourceWithRawResponse:
        return ProfilePictureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilePictureResourceWithStreamingResponse:
        return ProfilePictureResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Redirect to a user's profile picture. Signed URLs are valid for one hour.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: Redirect to the user profile picture

        Example:
            ```python
            client.users.profile_picture.retrieve(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{userId}/profile-picture", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update(
        self,
        user_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePictureUpdateResponse:
        """
        Upload a JPEG, PNG, GIF, or WebP profile picture up to 5 MB.

        Args:
            user_id: Path parameter.
            file: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProfilePictureUpdateResponse: Update your profile picture

        Example:
            ```python
            profile_picture = client.users.profile_picture.update(
                user_id="userId",
                file=b"file",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        body = deepcopy_with_paths(
            {
                "file": file,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            path_template("/v1/users/{userId}/profile-picture", **{"userId": user_id}),
            body=maybe_transform(body, profile_picture_update_params.ProfilePictureUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePictureUpdateResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePictureDeleteResponse:
        """
        Delete your profile picture. This succeeds if no picture exists.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProfilePictureDeleteResponse: Delete your profile picture

        Example:
            ```python
            profile_picture = client.users.profile_picture.delete(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            path_template("/v1/users/{userId}/profile-picture", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePictureDeleteResponse,
        )


class AsyncProfilePictureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfilePictureResourceWithRawResponse:
        return AsyncProfilePictureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilePictureResourceWithStreamingResponse:
        return AsyncProfilePictureResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Redirect to a user's profile picture. Signed URLs are valid for one hour.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            object: Redirect to the user profile picture

        Example:
            ```python
            await client.users.profile_picture.retrieve(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{userId}/profile-picture", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update(
        self,
        user_id: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePictureUpdateResponse:
        """
        Upload a JPEG, PNG, GIF, or WebP profile picture up to 5 MB.

        Args:
            user_id: Path parameter.
            file: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProfilePictureUpdateResponse: Update your profile picture

        Example:
            ```python
            profile_picture = await client.users.profile_picture.update(
                user_id="userId",
                file=b"file",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        body = deepcopy_with_paths(
            {
                "file": file,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            path_template("/v1/users/{userId}/profile-picture", **{"userId": user_id}),
            body=await async_maybe_transform(body, profile_picture_update_params.ProfilePictureUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePictureUpdateResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePictureDeleteResponse:
        """
        Delete your profile picture. This succeeds if no picture exists.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProfilePictureDeleteResponse: Delete your profile picture

        Example:
            ```python
            profile_picture = await client.users.profile_picture.delete(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            path_template("/v1/users/{userId}/profile-picture", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePictureDeleteResponse,
        )


class ProfilePictureResourceWithRawResponse:
    def __init__(self, profile_picture: ProfilePictureResource) -> None:
        self._profile_picture = profile_picture

        self.retrieve = to_raw_response_wrapper(
            profile_picture.retrieve,
        )
        self.update = to_raw_response_wrapper(
            profile_picture.update,
        )
        self.delete = to_raw_response_wrapper(
            profile_picture.delete,
        )


class AsyncProfilePictureResourceWithRawResponse:
    def __init__(self, profile_picture: AsyncProfilePictureResource) -> None:
        self._profile_picture = profile_picture

        self.retrieve = async_to_raw_response_wrapper(
            profile_picture.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            profile_picture.update,
        )
        self.delete = async_to_raw_response_wrapper(
            profile_picture.delete,
        )


class ProfilePictureResourceWithStreamingResponse:
    def __init__(self, profile_picture: ProfilePictureResource) -> None:
        self._profile_picture = profile_picture

        self.retrieve = to_streamed_response_wrapper(
            profile_picture.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            profile_picture.update,
        )
        self.delete = to_streamed_response_wrapper(
            profile_picture.delete,
        )


class AsyncProfilePictureResourceWithStreamingResponse:
    def __init__(self, profile_picture: AsyncProfilePictureResource) -> None:
        self._profile_picture = profile_picture

        self.retrieve = async_to_streamed_response_wrapper(
            profile_picture.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            profile_picture.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            profile_picture.delete,
        )
