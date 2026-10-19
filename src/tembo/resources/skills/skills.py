# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable
from typing_extensions import Literal
from ..._types import SequenceNotStr

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
from .marketplace import (
    MarketplaceResource,
    AsyncMarketplaceResource,
    MarketplaceResourceWithRawResponse,
    AsyncMarketplaceResourceWithRawResponse,
    MarketplaceResourceWithStreamingResponse,
    AsyncMarketplaceResourceWithStreamingResponse,
)
from ...types.skill_list_response import SkillListResponse
from ...types import skill_list_params, skill_create_params, skill_update_params
from ...types.skill_create_response import SkillCreateResponse
from ...types.skill_retrieve_response import SkillRetrieveResponse
from ...types.skill_update_response import SkillUpdateResponse
from ...types.skill_delete_response import SkillDeleteResponse

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    @cached_property
    def marketplace(self) -> MarketplaceResource:
        return MarketplaceResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        return SkillsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        project_id: str | Omit = omit,
        session_id: str | Omit = omit,
        search: str | Omit = omit,
        source: Literal["organization", "repository"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListResponse:
        """
        List organization skills or skills checked into a repository.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            names: Filter by exact skill names.
            repository_ids: Repository IDs to search for checked-in skills, supplied as a comma-separated list.
            project_id: Project whose repositories to search for checked-in skills.
            session_id: Session whose repositories to search for checked-in skills.
            search: Search skills by name, description, or keywords.
            source: organization lists saved organization skills; repository lists checked-in skills from the selected repositories, project, or session.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillListResponse: List skills

        Example:
            ```python
            skill = client.skills.list(
                limit=50,
                source="organization",
            )
            ```
        """
        return self._get(
            "/v1/skills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "names": names,
                        "repository_ids": repository_ids,
                        "project_id": project_id,
                        "session_id": session_id,
                        "search": search,
                        "source": source,
                    },
                    skill_list_params.SkillListParams,
                ),
            ),
            cast_to=SkillListResponse,
        )

    def create(
        self,
        *,
        description: str,
        name: str,
        files: Iterable[skill_create_params.File],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillCreateResponse:
        """
        Create an organization skill with its files.

        Args:
            description: Summary of what the skill does and when to use it.
            name: Display name of the skill.
            files: Complete file set, including a required SKILL.md. On update, replaces all existing files rather than merging them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillCreateResponse: Create a skill

        Example:
            ```python
            skill = client.skills.create(
                description="",
                name="x",
                files=[{"content": "", "filename": "x"}],
            )
            ```
        """
        return self._post(
            "/v1/skills",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "files": files,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
        )

    def retrieve(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillRetrieveResponse:
        """
        Retrieve an organization skill and all of its files.

        Args:
            skill_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillRetrieveResponse: Retrieve a skill

        Example:
            ```python
            skill = client.skills.retrieve(
                skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._get(
            path_template("/v1/skills/{skillId}", **{"skillId": skill_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillRetrieveResponse,
        )

    def update(
        self,
        skill_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        files: Iterable[skill_update_params.File] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillUpdateResponse:
        """
        Update an organization skill. When files are provided, they replace the complete file set.

        Args:
            skill_id: Path parameter.
            description: Summary of what the skill does and when to use it.
            name: Display name of the skill.
            files: Complete file set, including a required SKILL.md. On update, replaces all existing files rather than merging them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillUpdateResponse: Update a skill

        Example:
            ```python
            skill = client.skills.update(
                skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._patch(
            path_template("/v1/skills/{skillId}", **{"skillId": skill_id}),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "files": files,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
        )

    def delete(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillDeleteResponse:
        """
        Delete an organization skill.

        Args:
            skill_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillDeleteResponse: Delete a skill

        Example:
            ```python
            skill = client.skills.delete(
                skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._delete(
            path_template("/v1/skills/{skillId}", **{"skillId": skill_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillDeleteResponse,
        )


class AsyncSkillsResource(AsyncAPIResource):
    @cached_property
    def marketplace(self) -> AsyncMarketplaceResource:
        return AsyncMarketplaceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        repository_ids: SequenceNotStr[str] | Omit = omit,
        project_id: str | Omit = omit,
        session_id: str | Omit = omit,
        search: str | Omit = omit,
        source: Literal["organization", "repository"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListResponse:
        """
        List organization skills or skills checked into a repository.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            names: Filter by exact skill names.
            repository_ids: Repository IDs to search for checked-in skills, supplied as a comma-separated list.
            project_id: Project whose repositories to search for checked-in skills.
            session_id: Session whose repositories to search for checked-in skills.
            search: Search skills by name, description, or keywords.
            source: organization lists saved organization skills; repository lists checked-in skills from the selected repositories, project, or session.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillListResponse: List skills

        Example:
            ```python
            skill = await client.skills.list(
                limit=50,
                source="organization",
            )
            ```
        """
        return await self._get(
            "/v1/skills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "names": names,
                        "repository_ids": repository_ids,
                        "project_id": project_id,
                        "session_id": session_id,
                        "search": search,
                        "source": source,
                    },
                    skill_list_params.SkillListParams,
                ),
            ),
            cast_to=SkillListResponse,
        )

    async def create(
        self,
        *,
        description: str,
        name: str,
        files: Iterable[skill_create_params.File],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillCreateResponse:
        """
        Create an organization skill with its files.

        Args:
            description: Summary of what the skill does and when to use it.
            name: Display name of the skill.
            files: Complete file set, including a required SKILL.md. On update, replaces all existing files rather than merging them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillCreateResponse: Create a skill

        Example:
            ```python
            skill = await client.skills.create(
                description="",
                name="x",
                files=[{"content": "", "filename": "x"}],
            )
            ```
        """
        return await self._post(
            "/v1/skills",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "files": files,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
        )

    async def retrieve(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillRetrieveResponse:
        """
        Retrieve an organization skill and all of its files.

        Args:
            skill_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillRetrieveResponse: Retrieve a skill

        Example:
            ```python
            skill = await client.skills.retrieve(
                skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._get(
            path_template("/v1/skills/{skillId}", **{"skillId": skill_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillRetrieveResponse,
        )

    async def update(
        self,
        skill_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        files: Iterable[skill_update_params.File] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillUpdateResponse:
        """
        Update an organization skill. When files are provided, they replace the complete file set.

        Args:
            skill_id: Path parameter.
            description: Summary of what the skill does and when to use it.
            name: Display name of the skill.
            files: Complete file set, including a required SKILL.md. On update, replaces all existing files rather than merging them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillUpdateResponse: Update a skill

        Example:
            ```python
            skill = await client.skills.update(
                skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._patch(
            path_template("/v1/skills/{skillId}", **{"skillId": skill_id}),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "files": files,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
        )

    async def delete(
        self,
        skill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillDeleteResponse:
        """
        Delete an organization skill.

        Args:
            skill_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SkillDeleteResponse: Delete a skill

        Example:
            ```python
            skill = await client.skills.delete(
                skill_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if skill_id is None or (isinstance(skill_id, str) and not skill_id):
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._delete(
            path_template("/v1/skills/{skillId}", **{"skillId": skill_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillDeleteResponse,
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.list = to_raw_response_wrapper(
            skills.list,
        )
        self.create = to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = to_raw_response_wrapper(
            skills.update,
        )
        self.delete = to_raw_response_wrapper(
            skills.delete,
        )

    @cached_property
    def marketplace(self) -> MarketplaceResourceWithRawResponse:
        return MarketplaceResourceWithRawResponse(self._skills.marketplace)


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.list = async_to_raw_response_wrapper(
            skills.list,
        )
        self.create = async_to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            skills.update,
        )
        self.delete = async_to_raw_response_wrapper(
            skills.delete,
        )

    @cached_property
    def marketplace(self) -> AsyncMarketplaceResourceWithRawResponse:
        return AsyncMarketplaceResourceWithRawResponse(self._skills.marketplace)


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.list = to_streamed_response_wrapper(
            skills.list,
        )
        self.create = to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            skills.update,
        )
        self.delete = to_streamed_response_wrapper(
            skills.delete,
        )

    @cached_property
    def marketplace(self) -> MarketplaceResourceWithStreamingResponse:
        return MarketplaceResourceWithStreamingResponse(self._skills.marketplace)


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.list = async_to_streamed_response_wrapper(
            skills.list,
        )
        self.create = async_to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            skills.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            skills.delete,
        )

    @cached_property
    def marketplace(self) -> AsyncMarketplaceResourceWithStreamingResponse:
        return AsyncMarketplaceResourceWithStreamingResponse(self._skills.marketplace)
