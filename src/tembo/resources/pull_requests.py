# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Union
from datetime import datetime
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
from ..types.pull_request_list_response import PullRequestListResponse
from ..types import pull_request_list_params
from ..types.pull_request_retrieve_response import PullRequestRetrieveResponse

__all__ = ["PullRequestsResource", "AsyncPullRequestsResource"]


class PullRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PullRequestsResourceWithRawResponse:
        return PullRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PullRequestsResourceWithStreamingResponse:
        return PullRequestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        author_ids: SequenceNotStr[str] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        exclude_author_ids: SequenceNotStr[str] | Omit = omit,
        exclude_organization_name: str | Omit = omit,
        exclude_returned_author_ids: SequenceNotStr[str] | Omit = omit,
        exclude_reviewer_ids: SequenceNotStr[str] | Omit = omit,
        has_tembo_session: bool | Omit = omit,
        include_authors: bool | Omit = omit,
        include_total: bool | Omit = omit,
        include_stacks: bool | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        reviewer_ids: SequenceNotStr[str] | Omit = omit,
        merged_after: Union[str, datetime] | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["createdAt", "updatedAt"] | Omit = omit,
        state: Literal["open", "returned", "approved", "needs review", "draft", "merged", "closed"] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PullRequestListResponse:
        """
        List pull requests for the authenticated organization with cursor pagination.

        Args:
            author_ids: Filter authors by comma-separated provider:identifier values, such as github:octocat.
            created_after: Only pull requests created after this ISO 8601 timestamp.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            exclude_author_ids: Exclude authors by comma-separated provider:identifier values.
            exclude_organization_name: Exclude pull requests from the named organization within the caller access scope.
            exclude_returned_author_ids: Exclude returned pull requests by these comma-separated provider:identifier author values.
            exclude_reviewer_ids: Exclude pull requests assigned to these comma-separated reviewer identifiers.
            has_tembo_session: When true, only return pull requests with a linked Tembo session.
            include_authors: Request author filter options. Public responses do not include organization-wide author options.
            include_total: Include the total count of matching pull requests.
            include_stacks: Include each open pull request's position in its stack of dependent pull requests. Public responses do not include stacks.
            repository_ids: Filter by repository IDs, supplied as a comma-separated list.
            reviewer_ids: Filter by assigned reviewer identifiers, supplied as a comma-separated list.
            merged_after: Only pull requests merged after this ISO 8601 timestamp.
            search: Search pull requests.
            sort_by: Sort by creation time or last update time.
            state: Filter by lifecycle or review state, including open, returned, approved, needs review, draft, merged, or closed.
            updated_after: Only pull requests updated after this ISO 8601 timestamp.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PullRequestListResponse: List pull requests

        Example:
            ```python
            pull_request = client.pull_requests.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/pull-requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "author_ids": author_ids,
                        "created_after": created_after,
                        "cursor": cursor,
                        "limit": limit,
                        "exclude_author_ids": exclude_author_ids,
                        "exclude_organization_name": exclude_organization_name,
                        "exclude_returned_author_ids": exclude_returned_author_ids,
                        "exclude_reviewer_ids": exclude_reviewer_ids,
                        "has_tembo_session": has_tembo_session,
                        "include_authors": include_authors,
                        "include_total": include_total,
                        "include_stacks": include_stacks,
                        "repository_ids": repository_ids,
                        "reviewer_ids": reviewer_ids,
                        "merged_after": merged_after,
                        "search": search,
                        "sort_by": sort_by,
                        "state": state,
                        "updated_after": updated_after,
                    },
                    pull_request_list_params.PullRequestListParams,
                ),
            ),
            cast_to=PullRequestListResponse,
        )

    def retrieve(
        self,
        pull_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PullRequestRetrieveResponse:
        """
        Retrieve a pull request for the authenticated organization.

        Args:
            pull_request_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PullRequestRetrieveResponse: Retrieve a pull request

        Example:
            ```python
            pull_request = client.pull_requests.retrieve(
                pull_request_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if pull_request_id is None or (isinstance(pull_request_id, str) and not pull_request_id):
            raise ValueError(f"Expected a non-empty value for `pull_request_id` but received {pull_request_id!r}")
        return self._get(
            path_template("/v1/pull-requests/{pullRequestId}", **{"pullRequestId": pull_request_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PullRequestRetrieveResponse,
        )


class AsyncPullRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPullRequestsResourceWithRawResponse:
        return AsyncPullRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPullRequestsResourceWithStreamingResponse:
        return AsyncPullRequestsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        author_ids: SequenceNotStr[str] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        exclude_author_ids: SequenceNotStr[str] | Omit = omit,
        exclude_organization_name: str | Omit = omit,
        exclude_returned_author_ids: SequenceNotStr[str] | Omit = omit,
        exclude_reviewer_ids: SequenceNotStr[str] | Omit = omit,
        has_tembo_session: bool | Omit = omit,
        include_authors: bool | Omit = omit,
        include_total: bool | Omit = omit,
        include_stacks: bool | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        reviewer_ids: SequenceNotStr[str] | Omit = omit,
        merged_after: Union[str, datetime] | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["createdAt", "updatedAt"] | Omit = omit,
        state: Literal["open", "returned", "approved", "needs review", "draft", "merged", "closed"] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PullRequestListResponse:
        """
        List pull requests for the authenticated organization with cursor pagination.

        Args:
            author_ids: Filter authors by comma-separated provider:identifier values, such as github:octocat.
            created_after: Only pull requests created after this ISO 8601 timestamp.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            exclude_author_ids: Exclude authors by comma-separated provider:identifier values.
            exclude_organization_name: Exclude pull requests from the named organization within the caller access scope.
            exclude_returned_author_ids: Exclude returned pull requests by these comma-separated provider:identifier author values.
            exclude_reviewer_ids: Exclude pull requests assigned to these comma-separated reviewer identifiers.
            has_tembo_session: When true, only return pull requests with a linked Tembo session.
            include_authors: Request author filter options. Public responses do not include organization-wide author options.
            include_total: Include the total count of matching pull requests.
            include_stacks: Include each open pull request's position in its stack of dependent pull requests. Public responses do not include stacks.
            repository_ids: Filter by repository IDs, supplied as a comma-separated list.
            reviewer_ids: Filter by assigned reviewer identifiers, supplied as a comma-separated list.
            merged_after: Only pull requests merged after this ISO 8601 timestamp.
            search: Search pull requests.
            sort_by: Sort by creation time or last update time.
            state: Filter by lifecycle or review state, including open, returned, approved, needs review, draft, merged, or closed.
            updated_after: Only pull requests updated after this ISO 8601 timestamp.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PullRequestListResponse: List pull requests

        Example:
            ```python
            pull_request = await client.pull_requests.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/pull-requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "author_ids": author_ids,
                        "created_after": created_after,
                        "cursor": cursor,
                        "limit": limit,
                        "exclude_author_ids": exclude_author_ids,
                        "exclude_organization_name": exclude_organization_name,
                        "exclude_returned_author_ids": exclude_returned_author_ids,
                        "exclude_reviewer_ids": exclude_reviewer_ids,
                        "has_tembo_session": has_tembo_session,
                        "include_authors": include_authors,
                        "include_total": include_total,
                        "include_stacks": include_stacks,
                        "repository_ids": repository_ids,
                        "reviewer_ids": reviewer_ids,
                        "merged_after": merged_after,
                        "search": search,
                        "sort_by": sort_by,
                        "state": state,
                        "updated_after": updated_after,
                    },
                    pull_request_list_params.PullRequestListParams,
                ),
            ),
            cast_to=PullRequestListResponse,
        )

    async def retrieve(
        self,
        pull_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PullRequestRetrieveResponse:
        """
        Retrieve a pull request for the authenticated organization.

        Args:
            pull_request_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PullRequestRetrieveResponse: Retrieve a pull request

        Example:
            ```python
            pull_request = await client.pull_requests.retrieve(
                pull_request_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if pull_request_id is None or (isinstance(pull_request_id, str) and not pull_request_id):
            raise ValueError(f"Expected a non-empty value for `pull_request_id` but received {pull_request_id!r}")
        return await self._get(
            path_template("/v1/pull-requests/{pullRequestId}", **{"pullRequestId": pull_request_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PullRequestRetrieveResponse,
        )


class PullRequestsResourceWithRawResponse:
    def __init__(self, pull_requests: PullRequestsResource) -> None:
        self._pull_requests = pull_requests

        self.list = to_raw_response_wrapper(
            pull_requests.list,
        )
        self.retrieve = to_raw_response_wrapper(
            pull_requests.retrieve,
        )


class AsyncPullRequestsResourceWithRawResponse:
    def __init__(self, pull_requests: AsyncPullRequestsResource) -> None:
        self._pull_requests = pull_requests

        self.list = async_to_raw_response_wrapper(
            pull_requests.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pull_requests.retrieve,
        )


class PullRequestsResourceWithStreamingResponse:
    def __init__(self, pull_requests: PullRequestsResource) -> None:
        self._pull_requests = pull_requests

        self.list = to_streamed_response_wrapper(
            pull_requests.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            pull_requests.retrieve,
        )


class AsyncPullRequestsResourceWithStreamingResponse:
    def __init__(self, pull_requests: AsyncPullRequestsResource) -> None:
        self._pull_requests = pull_requests

        self.list = async_to_streamed_response_wrapper(
            pull_requests.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pull_requests.retrieve,
        )
