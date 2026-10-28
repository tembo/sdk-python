# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, List, Optional
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
from .environment_variables import (
    EnvironmentVariablesResource,
    AsyncEnvironmentVariablesResource,
    EnvironmentVariablesResourceWithRawResponse,
    AsyncEnvironmentVariablesResourceWithRawResponse,
    EnvironmentVariablesResourceWithStreamingResponse,
    AsyncEnvironmentVariablesResourceWithStreamingResponse,
)
from .snapshots import (
    SnapshotsResource,
    AsyncSnapshotsResource,
    SnapshotsResourceWithRawResponse,
    AsyncSnapshotsResourceWithRawResponse,
    SnapshotsResourceWithStreamingResponse,
    AsyncSnapshotsResourceWithStreamingResponse,
)
from .builds import (
    BuildsResource,
    AsyncBuildsResource,
    BuildsResourceWithRawResponse,
    AsyncBuildsResourceWithRawResponse,
    BuildsResourceWithStreamingResponse,
    AsyncBuildsResourceWithStreamingResponse,
)
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from ...types.project_update_defaults_response import ProjectUpdateDefaultsResponse
from ...types import project_update_defaults_params, project_list_params, project_create_params, project_update_params
from ...types.project_list_response import ProjectListResponse
from ...types.project_create_response import ProjectCreateResponse
from ...types.project_retrieve_response import ProjectRetrieveResponse
from ...types.project_update_response import ProjectUpdateResponse
from ...types.project_delete_response import ProjectDeleteResponse
from ...types.project_duplicate_response import ProjectDuplicateResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def environment_variables(self) -> EnvironmentVariablesResource:
        return EnvironmentVariablesResource(self._client)

    @cached_property
    def snapshots(self) -> SnapshotsResource:
        return SnapshotsResource(self._client)

    @cached_property
    def builds(self) -> BuildsResource:
        return BuildsResource(self._client)

    @cached_property
    def schedules(self) -> SchedulesResource:
        return SchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self)

    def update_defaults(
        self,
        *,
        project_id: Optional[str],
        sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUpdateDefaultsResponse:
        """
        Choose the default project and sandbox size for the organization.

        Args:
            project_id: Project to make the organization default, or null to clear the default.
            sandbox_size: Default workspace VM size for the organization.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectUpdateDefaultsResponse: Update project defaults

        Example:
            ```python
            project = client.projects.update_defaults(
                project_id="x",
                sandbox_size="nano",
            )
            ```
        """
        return self._put(
            "/v1/projects/defaults",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "sandbox_size": sandbox_size,
                },
                project_update_defaults_params.ProjectUpdateDefaultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateDefaultsResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        default_only: Literal["true"] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListResponse:
        """
        List projects in the authenticated organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            default_only: Only projects configured as defaults for at least one VM size.
            search: Search project names.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectListResponse: List projects

        Example:
            ```python
            project = client.projects.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "default_only": default_only, "search": search},
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    def create(
        self,
        *,
        description: Optional[str] | Omit = omit,
        name: str,
        setup_script: Optional[str] | Omit = omit,
        code_repository_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        agent_instructions: Optional[str] | Omit = omit,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        icon: Literal[
            "folder",
            "code",
            "terminal",
            "book",
            "brain",
            "bug",
            "building",
            "cloud",
            "globe",
            "idea",
            "tools",
            "magic",
            "processor",
            "sandbox",
            "server",
            "tasks",
            "tactics",
            "images",
            "database",
            "api",
            "mobile",
            "package",
        ]
        | Omit = omit,
        include_deps: bool | Omit = omit,
        include_skills: bool | Omit = omit,
        onboarding_default: bool | Omit = omit,
        run_now: bool | Omit = omit,
        schedule: project_create_params.Schedule | Omit = omit,
        sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        resource_settings: project_create_params.ResourceSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """
        Create a reusable project environment.

        Args:
            description: Short project description, or null to clear it.
            name: Project display name.
            setup_script: Setup script to run while building the environment, or null to clear it.
            code_repository_ids: Repository IDs included in the project environment. On update, replaces the repository selection.
            agent_instructions: Instructions supplied to agents using this project, or null to clear them.
            color: Project display color.
            icon: Project display icon.
            include_deps: Deprecated and ignored. Project builds always install dependencies.
            include_skills: Deprecated and ignored. Project builds always include skills.
            onboarding_default: Make this project the onboarding default for the organization.
            run_now: Queue initial snapshot builds immediately when a build host is available. Defaults to false.
            schedule: Recurring schedule for rebuilding the project environment.
            sizes: Workspace VM sizes to build for this project.
            resource_settings: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectCreateResponse: Create a project

        Example:
            ```python
            project = client.projects.create(
                name="x",
                sizes=["medium"],
                resource_settings={"automaticSizing": False},
            )
            ```
        """
        return self._post(
            "/v1/projects",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "setup_script": setup_script,
                    "code_repository_ids": code_repository_ids,
                    "agent_instructions": agent_instructions,
                    "color": color,
                    "icon": icon,
                    "include_deps": include_deps,
                    "include_skills": include_skills,
                    "onboarding_default": onboarding_default,
                    "run_now": run_now,
                    "schedule": schedule,
                    "sizes": sizes,
                    "resource_settings": resource_settings,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Retrieve project configuration. Use the project subresources to list snapshots, builds, schedules, and environment variables.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectRetrieveResponse: Retrieve a project

        Example:
            ```python
            project = client.projects.retrieve(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{projectId}", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    def update(
        self,
        project_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        setup_script: Optional[str] | Omit = omit,
        code_repository_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        agent_instructions: Optional[str] | Omit = omit,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        icon: Literal[
            "folder",
            "code",
            "terminal",
            "book",
            "brain",
            "bug",
            "building",
            "cloud",
            "globe",
            "idea",
            "tools",
            "magic",
            "processor",
            "sandbox",
            "server",
            "tasks",
            "tactics",
            "images",
            "database",
            "api",
            "mobile",
            "package",
        ]
        | Omit = omit,
        include_deps: bool | Omit = omit,
        include_skills: bool | Omit = omit,
        resource_settings: project_update_params.ResourceSettings | Omit = omit,
        default_for_sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        environment_variables: Dict[str, str] | Omit = omit,
        schedule: project_update_params.Schedule | Omit = omit,
        sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        warm_pool_schedule: Optional[project_update_params.WarmPoolSchedule] | Omit = omit,
        warm_pool_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUpdateResponse:
        """
        Update project repositories, setup script, agent instructions, environment variables, VM sizes and defaults; enable or pause scheduled builds or the warm pool; rename or customize its appearance.

        Args:
            project_id: Path parameter.
            description: Short project description, or null to clear it.
            name: Project display name.
            setup_script: Setup script to run while building the environment, or null to clear it.
            code_repository_ids: Repository IDs included in the project environment. On update, replaces the repository selection.
            agent_instructions: Instructions supplied to agents using this project, or null to clear them.
            color: Project display color.
            icon: Project display icon.
            include_deps: Deprecated and ignored. Project builds always install dependencies.
            include_skills: Deprecated and ignored. Project builds always include skills.
            resource_settings: Body parameter.
            default_for_sizes: VM sizes for which this project is the organization default. An empty array removes its default assignments.
            environment_variables: Replace the complete environment-variable map. Use createProjectEnvironmentVariables to add or replace individual keys instead.
            schedule: Change the project build schedule, including enabling or pausing it.
            sizes: Replace the workspace VM sizes built for this project.
            warm_pool_schedule: Weekly availability for prewarmed VMs. Null means always on; days use 0=Sunday. Overnight windows end the following day.
            warm_pool_enabled: Enable or disable prewarmed VMs for this project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectUpdateResponse: Update a project

        Example:
            ```python
            project = client.projects.update(
                project_id="projectId",
                resource_settings={"automaticSizing": False},
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._patch(
            path_template("/v1/projects/{projectId}", **{"projectId": project_id}),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "setup_script": setup_script,
                    "code_repository_ids": code_repository_ids,
                    "agent_instructions": agent_instructions,
                    "color": color,
                    "icon": icon,
                    "include_deps": include_deps,
                    "include_skills": include_skills,
                    "resource_settings": resource_settings,
                    "default_for_sizes": default_for_sizes,
                    "environment_variables": environment_variables,
                    "schedule": schedule,
                    "sizes": sizes,
                    "warm_pool_schedule": warm_pool_schedule,
                    "warm_pool_enabled": warm_pool_enabled,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateResponse,
        )

    def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectDeleteResponse:
        """
        Archive a project, remove its default VM-size assignments, and disable its build schedule. This does not permanently delete the project record.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectDeleteResponse: Delete a project

        Example:
            ```python
            project = client.projects.delete(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._delete(
            path_template("/v1/projects/{projectId}", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDeleteResponse,
        )

    def duplicate(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectDuplicateResponse:
        """
        Create a new project with the same configuration, environment variables, and schedule as an existing project. Snapshots are not copied.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectDuplicateResponse: Duplicate a project

        Example:
            ```python
            project = client.projects.duplicate(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{projectId}/duplicate", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDuplicateResponse,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def environment_variables(self) -> AsyncEnvironmentVariablesResource:
        return AsyncEnvironmentVariablesResource(self._client)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResource:
        return AsyncSnapshotsResource(self._client)

    @cached_property
    def builds(self) -> AsyncBuildsResource:
        return AsyncBuildsResource(self._client)

    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        return AsyncSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def update_defaults(
        self,
        *,
        project_id: Optional[str],
        sandbox_size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUpdateDefaultsResponse:
        """
        Choose the default project and sandbox size for the organization.

        Args:
            project_id: Project to make the organization default, or null to clear the default.
            sandbox_size: Default workspace VM size for the organization.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectUpdateDefaultsResponse: Update project defaults

        Example:
            ```python
            project = await client.projects.update_defaults(
                project_id="x",
                sandbox_size="nano",
            )
            ```
        """
        return await self._put(
            "/v1/projects/defaults",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "sandbox_size": sandbox_size,
                },
                project_update_defaults_params.ProjectUpdateDefaultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateDefaultsResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        default_only: Literal["true"] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListResponse:
        """
        List projects in the authenticated organization.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            default_only: Only projects configured as defaults for at least one VM size.
            search: Search project names.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectListResponse: List projects

        Example:
            ```python
            project = await client.projects.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "default_only": default_only, "search": search},
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    async def create(
        self,
        *,
        description: Optional[str] | Omit = omit,
        name: str,
        setup_script: Optional[str] | Omit = omit,
        code_repository_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        agent_instructions: Optional[str] | Omit = omit,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        icon: Literal[
            "folder",
            "code",
            "terminal",
            "book",
            "brain",
            "bug",
            "building",
            "cloud",
            "globe",
            "idea",
            "tools",
            "magic",
            "processor",
            "sandbox",
            "server",
            "tasks",
            "tactics",
            "images",
            "database",
            "api",
            "mobile",
            "package",
        ]
        | Omit = omit,
        include_deps: bool | Omit = omit,
        include_skills: bool | Omit = omit,
        onboarding_default: bool | Omit = omit,
        run_now: bool | Omit = omit,
        schedule: project_create_params.Schedule | Omit = omit,
        sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        resource_settings: project_create_params.ResourceSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """
        Create a reusable project environment.

        Args:
            description: Short project description, or null to clear it.
            name: Project display name.
            setup_script: Setup script to run while building the environment, or null to clear it.
            code_repository_ids: Repository IDs included in the project environment. On update, replaces the repository selection.
            agent_instructions: Instructions supplied to agents using this project, or null to clear them.
            color: Project display color.
            icon: Project display icon.
            include_deps: Deprecated and ignored. Project builds always install dependencies.
            include_skills: Deprecated and ignored. Project builds always include skills.
            onboarding_default: Make this project the onboarding default for the organization.
            run_now: Queue initial snapshot builds immediately when a build host is available. Defaults to false.
            schedule: Recurring schedule for rebuilding the project environment.
            sizes: Workspace VM sizes to build for this project.
            resource_settings: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectCreateResponse: Create a project

        Example:
            ```python
            project = await client.projects.create(
                name="x",
                sizes=["medium"],
                resource_settings={"automaticSizing": False},
            )
            ```
        """
        return await self._post(
            "/v1/projects",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "setup_script": setup_script,
                    "code_repository_ids": code_repository_ids,
                    "agent_instructions": agent_instructions,
                    "color": color,
                    "icon": icon,
                    "include_deps": include_deps,
                    "include_skills": include_skills,
                    "onboarding_default": onboarding_default,
                    "run_now": run_now,
                    "schedule": schedule,
                    "sizes": sizes,
                    "resource_settings": resource_settings,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    async def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Retrieve project configuration. Use the project subresources to list snapshots, builds, schedules, and environment variables.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectRetrieveResponse: Retrieve a project

        Example:
            ```python
            project = await client.projects.retrieve(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{projectId}", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    async def update(
        self,
        project_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        setup_script: Optional[str] | Omit = omit,
        code_repository_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        agent_instructions: Optional[str] | Omit = omit,
        color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"] | Omit = omit,
        icon: Literal[
            "folder",
            "code",
            "terminal",
            "book",
            "brain",
            "bug",
            "building",
            "cloud",
            "globe",
            "idea",
            "tools",
            "magic",
            "processor",
            "sandbox",
            "server",
            "tasks",
            "tactics",
            "images",
            "database",
            "api",
            "mobile",
            "package",
        ]
        | Omit = omit,
        include_deps: bool | Omit = omit,
        include_skills: bool | Omit = omit,
        resource_settings: project_update_params.ResourceSettings | Omit = omit,
        default_for_sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        environment_variables: Dict[str, str] | Omit = omit,
        schedule: project_update_params.Schedule | Omit = omit,
        sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]] | Omit = omit,
        warm_pool_schedule: Optional[project_update_params.WarmPoolSchedule] | Omit = omit,
        warm_pool_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUpdateResponse:
        """
        Update project repositories, setup script, agent instructions, environment variables, VM sizes and defaults; enable or pause scheduled builds or the warm pool; rename or customize its appearance.

        Args:
            project_id: Path parameter.
            description: Short project description, or null to clear it.
            name: Project display name.
            setup_script: Setup script to run while building the environment, or null to clear it.
            code_repository_ids: Repository IDs included in the project environment. On update, replaces the repository selection.
            agent_instructions: Instructions supplied to agents using this project, or null to clear them.
            color: Project display color.
            icon: Project display icon.
            include_deps: Deprecated and ignored. Project builds always install dependencies.
            include_skills: Deprecated and ignored. Project builds always include skills.
            resource_settings: Body parameter.
            default_for_sizes: VM sizes for which this project is the organization default. An empty array removes its default assignments.
            environment_variables: Replace the complete environment-variable map. Use createProjectEnvironmentVariables to add or replace individual keys instead.
            schedule: Change the project build schedule, including enabling or pausing it.
            sizes: Replace the workspace VM sizes built for this project.
            warm_pool_schedule: Weekly availability for prewarmed VMs. Null means always on; days use 0=Sunday. Overnight windows end the following day.
            warm_pool_enabled: Enable or disable prewarmed VMs for this project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectUpdateResponse: Update a project

        Example:
            ```python
            project = await client.projects.update(
                project_id="projectId",
                resource_settings={"automaticSizing": False},
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._patch(
            path_template("/v1/projects/{projectId}", **{"projectId": project_id}),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "setup_script": setup_script,
                    "code_repository_ids": code_repository_ids,
                    "agent_instructions": agent_instructions,
                    "color": color,
                    "icon": icon,
                    "include_deps": include_deps,
                    "include_skills": include_skills,
                    "resource_settings": resource_settings,
                    "default_for_sizes": default_for_sizes,
                    "environment_variables": environment_variables,
                    "schedule": schedule,
                    "sizes": sizes,
                    "warm_pool_schedule": warm_pool_schedule,
                    "warm_pool_enabled": warm_pool_enabled,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateResponse,
        )

    async def delete(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectDeleteResponse:
        """
        Archive a project, remove its default VM-size assignments, and disable its build schedule. This does not permanently delete the project record.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectDeleteResponse: Delete a project

        Example:
            ```python
            project = await client.projects.delete(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._delete(
            path_template("/v1/projects/{projectId}", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDeleteResponse,
        )

    async def duplicate(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectDuplicateResponse:
        """
        Create a new project with the same configuration, environment variables, and schedule as an existing project. Snapshots are not copied.

        Args:
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectDuplicateResponse: Duplicate a project

        Example:
            ```python
            project = await client.projects.duplicate(
                project_id="projectId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{projectId}/duplicate", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDuplicateResponse,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.update_defaults = to_raw_response_wrapper(
            projects.update_defaults,
        )
        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.create = to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            projects.retrieve,
        )
        self.update = to_raw_response_wrapper(
            projects.update,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )
        self.duplicate = to_raw_response_wrapper(
            projects.duplicate,
        )

    @cached_property
    def environment_variables(self) -> EnvironmentVariablesResourceWithRawResponse:
        return EnvironmentVariablesResourceWithRawResponse(self._projects.environment_variables)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self._projects.snapshots)

    @cached_property
    def builds(self) -> BuildsResourceWithRawResponse:
        return BuildsResourceWithRawResponse(self._projects.builds)

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        return SchedulesResourceWithRawResponse(self._projects.schedules)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.update_defaults = async_to_raw_response_wrapper(
            projects.update_defaults,
        )
        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            projects.update,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )
        self.duplicate = async_to_raw_response_wrapper(
            projects.duplicate,
        )

    @cached_property
    def environment_variables(self) -> AsyncEnvironmentVariablesResourceWithRawResponse:
        return AsyncEnvironmentVariablesResourceWithRawResponse(self._projects.environment_variables)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self._projects.snapshots)

    @cached_property
    def builds(self) -> AsyncBuildsResourceWithRawResponse:
        return AsyncBuildsResourceWithRawResponse(self._projects.builds)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        return AsyncSchedulesResourceWithRawResponse(self._projects.schedules)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.update_defaults = to_streamed_response_wrapper(
            projects.update_defaults,
        )
        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            projects.update,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )
        self.duplicate = to_streamed_response_wrapper(
            projects.duplicate,
        )

    @cached_property
    def environment_variables(self) -> EnvironmentVariablesResourceWithStreamingResponse:
        return EnvironmentVariablesResourceWithStreamingResponse(self._projects.environment_variables)

    @cached_property
    def snapshots(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self._projects.snapshots)

    @cached_property
    def builds(self) -> BuildsResourceWithStreamingResponse:
        return BuildsResourceWithStreamingResponse(self._projects.builds)

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        return SchedulesResourceWithStreamingResponse(self._projects.schedules)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.update_defaults = async_to_streamed_response_wrapper(
            projects.update_defaults,
        )
        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            projects.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            projects.duplicate,
        )

    @cached_property
    def environment_variables(self) -> AsyncEnvironmentVariablesResourceWithStreamingResponse:
        return AsyncEnvironmentVariablesResourceWithStreamingResponse(self._projects.environment_variables)

    @cached_property
    def snapshots(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self._projects.snapshots)

    @cached_property
    def builds(self) -> AsyncBuildsResourceWithStreamingResponse:
        return AsyncBuildsResourceWithStreamingResponse(self._projects.builds)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        return AsyncSchedulesResourceWithStreamingResponse(self._projects.schedules)
