# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.organizations.member_list_response import MemberListResponse
from ...types.organizations import member_list_params, member_create_params, member_update_params
from ...types.organizations.member_create_response import MemberCreateResponse
from ...types.organizations.member_retrieve_response import MemberRetrieveResponse
from ...types.organizations.member_update_response import MemberUpdateResponse
from ...types.organizations.member_delete_response import MemberDeleteResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self)

    def list(
        self,
        organization_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["active", "pending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        List active members or pending invitations with cursor pagination.

        Args:
            organization_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search organization members or invitations.
            status: List active members or pending invitations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberListResponse: List organization members

        Example:
            ```python
            member = client.organizations.members.list(
                organization_id="organizationId",
                limit=50,
                status="active",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/v1/organizations/{organizationId}/members", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search, "status": status},
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    def create(
        self,
        organization_id: str,
        *,
        email_address: str,
        role: Literal["org:admin", "org:member"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberCreateResponse:
        """
        Invite or add a user to an organization with a role.

        Args:
            organization_id: Path parameter.
            email_address: Email address of the user to add or invite.
            role: Organization role to grant: org:admin or org:member.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberCreateResponse: Create an organization member

        Example:
            ```python
            member = client.organizations.members.create(
                organization_id="organizationId",
                email_address="user@example.com",
                role="org:member",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template("/v1/organizations/{organizationId}/members", **{"organizationId": organization_id}),
            body=maybe_transform(
                {
                    "email_address": email_address,
                    "role": role,
                },
                member_create_params.MemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberCreateResponse,
        )

    def retrieve(
        self,
        member_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRetrieveResponse:
        """
        Retrieve an active member or pending member invitation.

        Args:
            member_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberRetrieveResponse: Retrieve an organization member

        Example:
            ```python
            member = client.organizations.members.retrieve(
                organization_id="organizationId",
                member_id="memberId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if member_id is None or (isinstance(member_id, str) and not member_id):
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            path_template(
                "/v1/organizations/{organizationId}/members/{memberId}",
                **{"organizationId": organization_id, "memberId": member_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveResponse,
        )

    def update(
        self,
        member_id: str,
        *,
        organization_id: str,
        role: Literal["org:admin", "org:member"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberUpdateResponse:
        """
        Update an organization member role.

        Args:
            member_id: Path parameter.
            organization_id: Path parameter.
            role: New organization role: org:admin or org:member.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberUpdateResponse: Update an organization member

        Example:
            ```python
            member = client.organizations.members.update(
                organization_id="organizationId",
                member_id="memberId",
                role="org:admin",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if member_id is None or (isinstance(member_id, str) and not member_id):
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._patch(
            path_template(
                "/v1/organizations/{organizationId}/members/{memberId}",
                **{"organizationId": organization_id, "memberId": member_id},
            ),
            body=maybe_transform(
                {"role": role},
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberUpdateResponse,
        )

    def delete(
        self,
        member_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberDeleteResponse:
        """
        Remove an active member or revoke a pending invitation.

        Args:
            member_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberDeleteResponse: Remove an organization member

        Example:
            ```python
            member = client.organizations.members.delete(
                organization_id="organizationId",
                member_id="memberId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if member_id is None or (isinstance(member_id, str) and not member_id):
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._delete(
            path_template(
                "/v1/organizations/{organizationId}/members/{memberId}",
                **{"organizationId": organization_id, "memberId": member_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberDeleteResponse,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self)

    async def list(
        self,
        organization_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["active", "pending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        List active members or pending invitations with cursor pagination.

        Args:
            organization_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search organization members or invitations.
            status: List active members or pending invitations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberListResponse: List organization members

        Example:
            ```python
            member = await client.organizations.members.list(
                organization_id="organizationId",
                limit=50,
                status="active",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/v1/organizations/{organizationId}/members", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search, "status": status},
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    async def create(
        self,
        organization_id: str,
        *,
        email_address: str,
        role: Literal["org:admin", "org:member"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberCreateResponse:
        """
        Invite or add a user to an organization with a role.

        Args:
            organization_id: Path parameter.
            email_address: Email address of the user to add or invite.
            role: Organization role to grant: org:admin or org:member.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberCreateResponse: Create an organization member

        Example:
            ```python
            member = await client.organizations.members.create(
                organization_id="organizationId",
                email_address="user@example.com",
                role="org:member",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template("/v1/organizations/{organizationId}/members", **{"organizationId": organization_id}),
            body=await async_maybe_transform(
                {
                    "email_address": email_address,
                    "role": role,
                },
                member_create_params.MemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberCreateResponse,
        )

    async def retrieve(
        self,
        member_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRetrieveResponse:
        """
        Retrieve an active member or pending member invitation.

        Args:
            member_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberRetrieveResponse: Retrieve an organization member

        Example:
            ```python
            member = await client.organizations.members.retrieve(
                organization_id="organizationId",
                member_id="memberId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if member_id is None or (isinstance(member_id, str) and not member_id):
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            path_template(
                "/v1/organizations/{organizationId}/members/{memberId}",
                **{"organizationId": organization_id, "memberId": member_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveResponse,
        )

    async def update(
        self,
        member_id: str,
        *,
        organization_id: str,
        role: Literal["org:admin", "org:member"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberUpdateResponse:
        """
        Update an organization member role.

        Args:
            member_id: Path parameter.
            organization_id: Path parameter.
            role: New organization role: org:admin or org:member.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberUpdateResponse: Update an organization member

        Example:
            ```python
            member = await client.organizations.members.update(
                organization_id="organizationId",
                member_id="memberId",
                role="org:admin",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if member_id is None or (isinstance(member_id, str) and not member_id):
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._patch(
            path_template(
                "/v1/organizations/{organizationId}/members/{memberId}",
                **{"organizationId": organization_id, "memberId": member_id},
            ),
            body=await async_maybe_transform(
                {"role": role},
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberUpdateResponse,
        )

    async def delete(
        self,
        member_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberDeleteResponse:
        """
        Remove an active member or revoke a pending invitation.

        Args:
            member_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberDeleteResponse: Remove an organization member

        Example:
            ```python
            member = await client.organizations.members.delete(
                organization_id="organizationId",
                member_id="memberId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if member_id is None or (isinstance(member_id, str) and not member_id):
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._delete(
            path_template(
                "/v1/organizations/{organizationId}/members/{memberId}",
                **{"organizationId": organization_id, "memberId": member_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberDeleteResponse,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.create = to_raw_response_wrapper(
            members.create,
        )
        self.retrieve = to_raw_response_wrapper(
            members.retrieve,
        )
        self.update = to_raw_response_wrapper(
            members.update,
        )
        self.delete = to_raw_response_wrapper(
            members.delete,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.create = async_to_raw_response_wrapper(
            members.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            members.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            members.update,
        )
        self.delete = async_to_raw_response_wrapper(
            members.delete,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.create = to_streamed_response_wrapper(
            members.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            members.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            members.update,
        )
        self.delete = to_streamed_response_wrapper(
            members.delete,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.create = async_to_streamed_response_wrapper(
            members.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            members.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            members.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            members.delete,
        )
