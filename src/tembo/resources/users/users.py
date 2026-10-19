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
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .connected_accounts import (
    ConnectedAccountsResource,
    AsyncConnectedAccountsResource,
    ConnectedAccountsResourceWithRawResponse,
    AsyncConnectedAccountsResourceWithRawResponse,
    ConnectedAccountsResourceWithStreamingResponse,
    AsyncConnectedAccountsResourceWithStreamingResponse,
)
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)
from .profile_picture import (
    ProfilePictureResource,
    AsyncProfilePictureResource,
    ProfilePictureResourceWithRawResponse,
    AsyncProfilePictureResourceWithRawResponse,
    ProfilePictureResourceWithStreamingResponse,
    AsyncProfilePictureResourceWithStreamingResponse,
)
from ...types.user_me_response import UserMeResponse
from ...types.user_retrieve_response import UserRetrieveResponse
from ...types.user_delete_response import UserDeleteResponse
from ...types import user_delete_params

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def connected_accounts(self) -> ConnectedAccountsResource:
        return ConnectedAccountsResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def profile_picture(self) -> ProfilePictureResource:
        return ProfilePictureResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self)

    def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserMeResponse:
        """
        Retrieve the authenticated user.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserMeResponse: Retrieve the current user

        Example:
            ```python
            user = client.users.me()
            ```
        """
        return self._get(
            "/v1/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserMeResponse,
        )

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
    ) -> UserRetrieveResponse:
        """
        Retrieve a user profile visible to the caller.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserRetrieveResponse: Retrieve a user

        Example:
            ```python
            user = client.users.retrieve(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{userId}", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        deletion_questionnaire: user_delete_params.DeletionQuestionnaire | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Queue permanent deletion of your user account.

        Args:
            user_id: Path parameter.
            deletion_questionnaire: Optional account-deletion feedback. Account deletion is queued regardless of whether feedback is supplied.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserDeleteResponse: Delete a user

        Example:
            ```python
            user = client.users.delete(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            path_template("/v1/users/{userId}", **{"userId": user_id}),
            body=maybe_transform(
                {"deletion_questionnaire": deletion_questionnaire},
                user_delete_params.UserDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def connected_accounts(self) -> AsyncConnectedAccountsResource:
        return AsyncConnectedAccountsResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def profile_picture(self) -> AsyncProfilePictureResource:
        return AsyncProfilePictureResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self)

    async def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserMeResponse:
        """
        Retrieve the authenticated user.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserMeResponse: Retrieve the current user

        Example:
            ```python
            user = await client.users.me()
            ```
        """
        return await self._get(
            "/v1/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserMeResponse,
        )

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
    ) -> UserRetrieveResponse:
        """
        Retrieve a user profile visible to the caller.

        Args:
            user_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserRetrieveResponse: Retrieve a user

        Example:
            ```python
            user = await client.users.retrieve(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{userId}", **{"userId": user_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        deletion_questionnaire: user_delete_params.DeletionQuestionnaire | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Queue permanent deletion of your user account.

        Args:
            user_id: Path parameter.
            deletion_questionnaire: Optional account-deletion feedback. Account deletion is queued regardless of whether feedback is supplied.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UserDeleteResponse: Delete a user

        Example:
            ```python
            user = await client.users.delete(
                user_id="userId",
            )
            ```
        """
        if user_id is None or (isinstance(user_id, str) and not user_id):
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            path_template("/v1/users/{userId}", **{"userId": user_id}),
            body=await async_maybe_transform(
                {"deletion_questionnaire": deletion_questionnaire},
                user_delete_params.UserDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.me = to_raw_response_wrapper(
            users.me,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._users.settings)

    @cached_property
    def connected_accounts(self) -> ConnectedAccountsResourceWithRawResponse:
        return ConnectedAccountsResourceWithRawResponse(self._users.connected_accounts)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._users.subscriptions)

    @cached_property
    def profile_picture(self) -> ProfilePictureResourceWithRawResponse:
        return ProfilePictureResourceWithRawResponse(self._users.profile_picture)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.me = async_to_raw_response_wrapper(
            users.me,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._users.settings)

    @cached_property
    def connected_accounts(self) -> AsyncConnectedAccountsResourceWithRawResponse:
        return AsyncConnectedAccountsResourceWithRawResponse(self._users.connected_accounts)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._users.subscriptions)

    @cached_property
    def profile_picture(self) -> AsyncProfilePictureResourceWithRawResponse:
        return AsyncProfilePictureResourceWithRawResponse(self._users.profile_picture)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.me = to_streamed_response_wrapper(
            users.me,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._users.settings)

    @cached_property
    def connected_accounts(self) -> ConnectedAccountsResourceWithStreamingResponse:
        return ConnectedAccountsResourceWithStreamingResponse(self._users.connected_accounts)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._users.subscriptions)

    @cached_property
    def profile_picture(self) -> ProfilePictureResourceWithStreamingResponse:
        return ProfilePictureResourceWithStreamingResponse(self._users.profile_picture)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.me = async_to_streamed_response_wrapper(
            users.me,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._users.settings)

    @cached_property
    def connected_accounts(self) -> AsyncConnectedAccountsResourceWithStreamingResponse:
        return AsyncConnectedAccountsResourceWithStreamingResponse(self._users.connected_accounts)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._users.subscriptions)

    @cached_property
    def profile_picture(self) -> AsyncProfilePictureResourceWithStreamingResponse:
        return AsyncProfilePictureResourceWithStreamingResponse(self._users.profile_picture)
