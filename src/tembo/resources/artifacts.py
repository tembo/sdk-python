# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List
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
from ..types.artifact_list_response import ArtifactListResponse
from ..types import artifact_list_params, artifact_create_params
from ..types.artifact_create_response import ArtifactCreateResponse
from ..types.artifact_retrieve_response import ArtifactRetrieveResponse
from ..types.artifact_delete_response import ArtifactDeleteResponse

__all__ = ["ArtifactsResource", "AsyncArtifactsResource"]


class ArtifactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArtifactsResourceWithRawResponse:
        return ArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtifactsResourceWithStreamingResponse:
        return ArtifactsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        job_id: str | Omit = omit,
        session_id: str | Omit = omit,
        types: List[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactListResponse:
        """
        List organization artifacts with optional session and type filters.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            job_id: Filter artifacts created by this job.
            session_id: Filter artifacts attached to this session.
            types: Filter artifact types, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactListResponse: List artifacts

        Example:
            ```python
            artifact = client.artifacts.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/artifacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "job_id": job_id, "session_id": session_id, "types": types},
                    artifact_list_params.ArtifactListParams,
                ),
            ),
            cast_to=ArtifactListResponse,
        )

    def create(
        self,
        *,
        title: str,
        description: str | Omit = omit,
        category: Literal[
            "code_walkthrough",
            "bug_report",
            "incident_report",
            "license_audit",
            "data_flow_map",
            "security_findings",
            "cost_map",
            "ux_variations",
            "architecture_map",
            "migration_summary",
            "release_checklist",
            "shipped_summary",
            "rollout_plan",
            "diagram",
            "chart",
            "dashboard",
            "timeline",
            "comparison",
            "report",
        ]
        | Omit = omit,
        output: artifact_create_params.Output,
        related_pull_request_urls: SequenceNotStr[str] | Omit = omit,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactCreateResponse:
        """
        Create a file artifact for a session from inline content or an uploaded asset.

        Args:
            title: Human-readable title for the artifact.
            description: Short description of what the artifact shows.
            category: Artifact category for display and filtering.
            output: Artifact content or a reference to an uploaded asset. The type field selects the required fields.
            related_pull_request_urls: URLs of pull requests related to this artifact.
            session_id: Session to attach the artifact to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactCreateResponse: Create an artifact

        Example:
            ```python
            artifact = client.artifacts.create(
                title="x",
                output={"type": "html", "content": "x"},
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return self._post(
            "/v1/artifacts",
            body=maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "category": category,
                    "output": output,
                    "related_pull_request_urls": related_pull_request_urls,
                    "session_id": session_id,
                },
                artifact_create_params.ArtifactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactCreateResponse,
        )

    def retrieve(
        self,
        artifact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactRetrieveResponse:
        """
        Retrieve an organization artifact by ID.

        Args:
            artifact_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactRetrieveResponse: Retrieve an artifact

        Example:
            ```python
            artifact = client.artifacts.retrieve(
                artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return self._get(
            path_template("/v1/artifacts/{artifactId}", **{"artifactId": artifact_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactRetrieveResponse,
        )

    def delete(
        self,
        artifact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactDeleteResponse:
        """
        Delete an organization artifact and its backing asset when present.

        Args:
            artifact_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactDeleteResponse: Delete an artifact

        Example:
            ```python
            artifact = client.artifacts.delete(
                artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return self._delete(
            path_template("/v1/artifacts/{artifactId}", **{"artifactId": artifact_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactDeleteResponse,
        )


class AsyncArtifactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArtifactsResourceWithRawResponse:
        return AsyncArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtifactsResourceWithStreamingResponse:
        return AsyncArtifactsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        job_id: str | Omit = omit,
        session_id: str | Omit = omit,
        types: List[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactListResponse:
        """
        List organization artifacts with optional session and type filters.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            job_id: Filter artifacts created by this job.
            session_id: Filter artifacts attached to this session.
            types: Filter artifact types, supplied as a comma-separated list.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactListResponse: List artifacts

        Example:
            ```python
            artifact = await client.artifacts.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/artifacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "job_id": job_id, "session_id": session_id, "types": types},
                    artifact_list_params.ArtifactListParams,
                ),
            ),
            cast_to=ArtifactListResponse,
        )

    async def create(
        self,
        *,
        title: str,
        description: str | Omit = omit,
        category: Literal[
            "code_walkthrough",
            "bug_report",
            "incident_report",
            "license_audit",
            "data_flow_map",
            "security_findings",
            "cost_map",
            "ux_variations",
            "architecture_map",
            "migration_summary",
            "release_checklist",
            "shipped_summary",
            "rollout_plan",
            "diagram",
            "chart",
            "dashboard",
            "timeline",
            "comparison",
            "report",
        ]
        | Omit = omit,
        output: artifact_create_params.Output,
        related_pull_request_urls: SequenceNotStr[str] | Omit = omit,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactCreateResponse:
        """
        Create a file artifact for a session from inline content or an uploaded asset.

        Args:
            title: Human-readable title for the artifact.
            description: Short description of what the artifact shows.
            category: Artifact category for display and filtering.
            output: Artifact content or a reference to an uploaded asset. The type field selects the required fields.
            related_pull_request_urls: URLs of pull requests related to this artifact.
            session_id: Session to attach the artifact to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactCreateResponse: Create an artifact

        Example:
            ```python
            artifact = await client.artifacts.create(
                title="x",
                output={"type": "html", "content": "x"},
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return await self._post(
            "/v1/artifacts",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "category": category,
                    "output": output,
                    "related_pull_request_urls": related_pull_request_urls,
                    "session_id": session_id,
                },
                artifact_create_params.ArtifactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactCreateResponse,
        )

    async def retrieve(
        self,
        artifact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactRetrieveResponse:
        """
        Retrieve an organization artifact by ID.

        Args:
            artifact_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactRetrieveResponse: Retrieve an artifact

        Example:
            ```python
            artifact = await client.artifacts.retrieve(
                artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return await self._get(
            path_template("/v1/artifacts/{artifactId}", **{"artifactId": artifact_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactRetrieveResponse,
        )

    async def delete(
        self,
        artifact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactDeleteResponse:
        """
        Delete an organization artifact and its backing asset when present.

        Args:
            artifact_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ArtifactDeleteResponse: Delete an artifact

        Example:
            ```python
            artifact = await client.artifacts.delete(
                artifact_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return await self._delete(
            path_template("/v1/artifacts/{artifactId}", **{"artifactId": artifact_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactDeleteResponse,
        )


class ArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = to_raw_response_wrapper(
            artifacts.list,
        )
        self.create = to_raw_response_wrapper(
            artifacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            artifacts.delete,
        )


class AsyncArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = async_to_raw_response_wrapper(
            artifacts.list,
        )
        self.create = async_to_raw_response_wrapper(
            artifacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            artifacts.delete,
        )


class ArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = to_streamed_response_wrapper(
            artifacts.list,
        )
        self.create = to_streamed_response_wrapper(
            artifacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            artifacts.delete,
        )


class AsyncArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = async_to_streamed_response_wrapper(
            artifacts.list,
        )
        self.create = async_to_streamed_response_wrapper(
            artifacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            artifacts.delete,
        )
