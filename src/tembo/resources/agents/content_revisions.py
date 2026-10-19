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
from ...types.agents.content_revision_list_response import ContentRevisionListResponse
from ...types.agents import content_revision_list_params, content_revision_restore_params
from ...types.agents.content_revision_retrieve_response import ContentRevisionRetrieveResponse
from ...types.agents.content_revision_restore_response import ContentRevisionRestoreResponse

__all__ = ["ContentRevisionsResource", "AsyncContentRevisionsResource"]


class ContentRevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentRevisionsResourceWithRawResponse:
        return ContentRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentRevisionsResourceWithStreamingResponse:
        return ContentRevisionsResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentRevisionListResponse:
        """
        List saved revisions of an agent’s instruction JSON document, newest first. Revisions do not include other agent configuration. Author details are redacted from public API responses.

        Args:
            agent_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ContentRevisionListResponse: List agent instruction revisions

        Example:
            ```python
            content_revision = client.agents.content_revisions.list(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agentId}/content-revisions", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit}, content_revision_list_params.ContentRevisionListParams
                ),
            ),
            cast_to=ContentRevisionListResponse,
        )

    def retrieve(
        self,
        version: int,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentRevisionRetrieveResponse:
        """
        Retrieve the instruction JSON document saved in one revision. Other agent configuration is not included. Author details are redacted from public API responses.

        Args:
            version: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ContentRevisionRetrieveResponse: Retrieve an agent instruction revision

        Example:
            ```python
            content_revision = client.agents.content_revisions.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                version=1,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if version is None or (isinstance(version, str) and not version):
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._get(
            path_template(
                "/v1/agents/{agentId}/content-revisions/{version}", **{"agentId": agent_id, "version": version}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentRevisionRetrieveResponse,
        )

    def restore(
        self,
        version: int,
        *,
        agent_id: str,
        expected_content_version: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentRevisionRestoreResponse:
        """
        Restore a saved instruction JSON document and its mentioned integrations, without reverting other agent configuration. A changed document creates a new revision attributed to the caller. Supply the agent’s current contentVersion as expectedContentVersion; a concurrent instruction change returns 409.

        Args:
            version: Path parameter.
            agent_id: Path parameter.
            expected_content_version: The agent’s current instruction version, used to reject a restore if the instructions have changed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ContentRevisionRestoreResponse: Restore agent instructions

        Example:
            ```python
            content_revision = client.agents.content_revisions.restore(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                version=1,
                expected_content_version=1,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if version is None or (isinstance(version, str) and not version):
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._post(
            path_template(
                "/v1/agents/{agentId}/content-revisions/{version}/restore", **{"agentId": agent_id, "version": version}
            ),
            body=maybe_transform(
                {"expected_content_version": expected_content_version},
                content_revision_restore_params.ContentRevisionRestoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentRevisionRestoreResponse,
        )


class AsyncContentRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentRevisionsResourceWithRawResponse:
        return AsyncContentRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentRevisionsResourceWithStreamingResponse:
        return AsyncContentRevisionsResourceWithStreamingResponse(self)

    async def list(
        self,
        agent_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentRevisionListResponse:
        """
        List saved revisions of an agent’s instruction JSON document, newest first. Revisions do not include other agent configuration. Author details are redacted from public API responses.

        Args:
            agent_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ContentRevisionListResponse: List agent instruction revisions

        Example:
            ```python
            content_revision = await client.agents.content_revisions.list(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agentId}/content-revisions", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, content_revision_list_params.ContentRevisionListParams
                ),
            ),
            cast_to=ContentRevisionListResponse,
        )

    async def retrieve(
        self,
        version: int,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentRevisionRetrieveResponse:
        """
        Retrieve the instruction JSON document saved in one revision. Other agent configuration is not included. Author details are redacted from public API responses.

        Args:
            version: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ContentRevisionRetrieveResponse: Retrieve an agent instruction revision

        Example:
            ```python
            content_revision = await client.agents.content_revisions.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                version=1,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if version is None or (isinstance(version, str) and not version):
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._get(
            path_template(
                "/v1/agents/{agentId}/content-revisions/{version}", **{"agentId": agent_id, "version": version}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentRevisionRetrieveResponse,
        )

    async def restore(
        self,
        version: int,
        *,
        agent_id: str,
        expected_content_version: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentRevisionRestoreResponse:
        """
        Restore a saved instruction JSON document and its mentioned integrations, without reverting other agent configuration. A changed document creates a new revision attributed to the caller. Supply the agent’s current contentVersion as expectedContentVersion; a concurrent instruction change returns 409.

        Args:
            version: Path parameter.
            agent_id: Path parameter.
            expected_content_version: The agent’s current instruction version, used to reject a restore if the instructions have changed.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ContentRevisionRestoreResponse: Restore agent instructions

        Example:
            ```python
            content_revision = await client.agents.content_revisions.restore(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                version=1,
                expected_content_version=1,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if version is None or (isinstance(version, str) and not version):
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._post(
            path_template(
                "/v1/agents/{agentId}/content-revisions/{version}/restore", **{"agentId": agent_id, "version": version}
            ),
            body=await async_maybe_transform(
                {"expected_content_version": expected_content_version},
                content_revision_restore_params.ContentRevisionRestoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentRevisionRestoreResponse,
        )


class ContentRevisionsResourceWithRawResponse:
    def __init__(self, content_revisions: ContentRevisionsResource) -> None:
        self._content_revisions = content_revisions

        self.list = to_raw_response_wrapper(
            content_revisions.list,
        )
        self.retrieve = to_raw_response_wrapper(
            content_revisions.retrieve,
        )
        self.restore = to_raw_response_wrapper(
            content_revisions.restore,
        )


class AsyncContentRevisionsResourceWithRawResponse:
    def __init__(self, content_revisions: AsyncContentRevisionsResource) -> None:
        self._content_revisions = content_revisions

        self.list = async_to_raw_response_wrapper(
            content_revisions.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            content_revisions.retrieve,
        )
        self.restore = async_to_raw_response_wrapper(
            content_revisions.restore,
        )


class ContentRevisionsResourceWithStreamingResponse:
    def __init__(self, content_revisions: ContentRevisionsResource) -> None:
        self._content_revisions = content_revisions

        self.list = to_streamed_response_wrapper(
            content_revisions.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            content_revisions.retrieve,
        )
        self.restore = to_streamed_response_wrapper(
            content_revisions.restore,
        )


class AsyncContentRevisionsResourceWithStreamingResponse:
    def __init__(self, content_revisions: AsyncContentRevisionsResource) -> None:
        self._content_revisions = content_revisions

        self.list = async_to_streamed_response_wrapper(
            content_revisions.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            content_revisions.retrieve,
        )
        self.restore = async_to_streamed_response_wrapper(
            content_revisions.restore,
        )
