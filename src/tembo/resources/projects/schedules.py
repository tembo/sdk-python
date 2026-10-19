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
from ...types.projects.schedule_list_response import ScheduleListResponse
from ...types.projects import schedule_list_params, schedule_create_params, schedule_update_params
from ...types.projects.schedule_create_response import ScheduleCreateResponse
from ...types.projects.schedule_retrieve_response import ScheduleRetrieveResponse
from ...types.projects.schedule_update_response import ScheduleUpdateResponse
from ...types.projects.schedule_delete_response import ScheduleDeleteResponse

__all__ = ["SchedulesResource", "AsyncSchedulesResource"]


class SchedulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchedulesResourceWithRawResponse:
        return SchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesResourceWithStreamingResponse:
        return SchedulesResourceWithStreamingResponse(self)

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
    ) -> ScheduleListResponse:
        """
        List schedules linked to a project.

        Args:
            project_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleListResponse: List project schedules

        Example:
            ```python
            schedule = client.projects.schedules.list(
                project_id="projectId",
                limit=50,
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{projectId}/schedules", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, schedule_list_params.ScheduleListParams),
            ),
            cast_to=ScheduleListResponse,
        )

    def create(
        self,
        project_id: str,
        *,
        cron: str,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Create a recurring project build schedule.

        Args:
            project_id: Path parameter.
            cron: Cron expression for recurring project snapshot builds.
            timezone: Timezone for the cron schedule. Defaults to UTC.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleCreateResponse: Create a project schedule

        Example:
            ```python
            schedule = client.projects.schedules.create(
                project_id="projectId",
                cron="x",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{projectId}/schedules", **{"projectId": project_id}),
            body=maybe_transform(
                {
                    "cron": cron,
                    "timezone": timezone,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    def retrieve(
        self,
        schedule_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieve one project build schedule.

        Args:
            schedule_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleRetrieveResponse: Retrieve a project schedule

        Example:
            ```python
            schedule = client.projects.schedules.retrieve(
                project_id="projectId",
                schedule_id="scheduleId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._get(
            path_template(
                "/v1/projects/{projectId}/schedules/{scheduleId}",
                **{"projectId": project_id, "scheduleId": schedule_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleRetrieveResponse,
        )

    def update(
        self,
        schedule_id: str,
        *,
        project_id: str,
        cron: str | Omit = omit,
        enabled: bool | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleUpdateResponse:
        """
        Update timing or enabled state for a project schedule.

        Args:
            schedule_id: Path parameter.
            project_id: Path parameter.
            cron: Replace the recurring project build cron expression.
            enabled: Enable or pause scheduled project builds.
            timezone: Timezone for the cron schedule, or null to clear it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleUpdateResponse: Update a project schedule

        Example:
            ```python
            schedule = client.projects.schedules.update(
                project_id="projectId",
                schedule_id="scheduleId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._patch(
            path_template(
                "/v1/projects/{projectId}/schedules/{scheduleId}",
                **{"projectId": project_id, "scheduleId": schedule_id},
            ),
            body=maybe_transform(
                {
                    "cron": cron,
                    "enabled": enabled,
                    "timezone": timezone,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleUpdateResponse,
        )

    def delete(
        self,
        schedule_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """
        Disable a project build schedule.

        Args:
            schedule_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleDeleteResponse: Delete a project schedule

        Example:
            ```python
            schedule = client.projects.schedules.delete(
                project_id="projectId",
                schedule_id="scheduleId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._delete(
            path_template(
                "/v1/projects/{projectId}/schedules/{scheduleId}",
                **{"projectId": project_id, "scheduleId": schedule_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )


class AsyncSchedulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchedulesResourceWithRawResponse:
        return AsyncSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesResourceWithStreamingResponse:
        return AsyncSchedulesResourceWithStreamingResponse(self)

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
    ) -> ScheduleListResponse:
        """
        List schedules linked to a project.

        Args:
            project_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleListResponse: List project schedules

        Example:
            ```python
            schedule = await client.projects.schedules.list(
                project_id="projectId",
                limit=50,
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{projectId}/schedules", **{"projectId": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, schedule_list_params.ScheduleListParams
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    async def create(
        self,
        project_id: str,
        *,
        cron: str,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Create a recurring project build schedule.

        Args:
            project_id: Path parameter.
            cron: Cron expression for recurring project snapshot builds.
            timezone: Timezone for the cron schedule. Defaults to UTC.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleCreateResponse: Create a project schedule

        Example:
            ```python
            schedule = await client.projects.schedules.create(
                project_id="projectId",
                cron="x",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{projectId}/schedules", **{"projectId": project_id}),
            body=await async_maybe_transform(
                {
                    "cron": cron,
                    "timezone": timezone,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    async def retrieve(
        self,
        schedule_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieve one project build schedule.

        Args:
            schedule_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleRetrieveResponse: Retrieve a project schedule

        Example:
            ```python
            schedule = await client.projects.schedules.retrieve(
                project_id="projectId",
                schedule_id="scheduleId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._get(
            path_template(
                "/v1/projects/{projectId}/schedules/{scheduleId}",
                **{"projectId": project_id, "scheduleId": schedule_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleRetrieveResponse,
        )

    async def update(
        self,
        schedule_id: str,
        *,
        project_id: str,
        cron: str | Omit = omit,
        enabled: bool | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleUpdateResponse:
        """
        Update timing or enabled state for a project schedule.

        Args:
            schedule_id: Path parameter.
            project_id: Path parameter.
            cron: Replace the recurring project build cron expression.
            enabled: Enable or pause scheduled project builds.
            timezone: Timezone for the cron schedule, or null to clear it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleUpdateResponse: Update a project schedule

        Example:
            ```python
            schedule = await client.projects.schedules.update(
                project_id="projectId",
                schedule_id="scheduleId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._patch(
            path_template(
                "/v1/projects/{projectId}/schedules/{scheduleId}",
                **{"projectId": project_id, "scheduleId": schedule_id},
            ),
            body=await async_maybe_transform(
                {
                    "cron": cron,
                    "enabled": enabled,
                    "timezone": timezone,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleUpdateResponse,
        )

    async def delete(
        self,
        schedule_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """
        Disable a project build schedule.

        Args:
            schedule_id: Path parameter.
            project_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleDeleteResponse: Delete a project schedule

        Example:
            ```python
            schedule = await client.projects.schedules.delete(
                project_id="projectId",
                schedule_id="scheduleId",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._delete(
            path_template(
                "/v1/projects/{projectId}/schedules/{scheduleId}",
                **{"projectId": project_id, "scheduleId": schedule_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )


class SchedulesResourceWithRawResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.list = to_raw_response_wrapper(
            schedules.list,
        )
        self.create = to_raw_response_wrapper(
            schedules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            schedules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            schedules.update,
        )
        self.delete = to_raw_response_wrapper(
            schedules.delete,
        )


class AsyncSchedulesResourceWithRawResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.list = async_to_raw_response_wrapper(
            schedules.list,
        )
        self.create = async_to_raw_response_wrapper(
            schedules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            schedules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            schedules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            schedules.delete,
        )


class SchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.list = to_streamed_response_wrapper(
            schedules.list,
        )
        self.create = to_streamed_response_wrapper(
            schedules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            schedules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            schedules.update,
        )
        self.delete = to_streamed_response_wrapper(
            schedules.delete,
        )


class AsyncSchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.list = async_to_streamed_response_wrapper(
            schedules.list,
        )
        self.create = async_to_streamed_response_wrapper(
            schedules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            schedules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            schedules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            schedules.delete,
        )
