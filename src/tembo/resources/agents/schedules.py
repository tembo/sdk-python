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
from ...types.agents.schedule_list_response import ScheduleListResponse
from ...types.agents import schedule_list_params, schedule_create_params, schedule_update_params
from ...types.agents.schedule_create_response import ScheduleCreateResponse
from ...types.agents.schedule_retrieve_response import ScheduleRetrieveResponse
from ...types.agents.schedule_update_response import ScheduleUpdateResponse
from ...types.agents.schedule_delete_response import ScheduleDeleteResponse

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
    ) -> ScheduleListResponse:
        """
        List the schedules configured for an agent.

        Args:
            agent_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleListResponse: List agent schedules

        Example:
            ```python
            schedule = client.agents.schedules.list(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agentId}/schedules", **{"agentId": agent_id}),
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
        agent_id: str,
        *,
        cron: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Create a recurring schedule that starts agent runs using a cron expression.

        Args:
            agent_id: Path parameter.
            cron: Cron expression for recurring agent runs. Agent enabled and archived state controls whether the schedule runs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleCreateResponse: Create an agent schedule

        Example:
            ```python
            schedule = client.agents.schedules.create(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                cron="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/agents/{agentId}/schedules", **{"agentId": agent_id}),
            body=maybe_transform(
                {"cron": cron},
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
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieve an agent schedule, including its enabled state and next execution time.

        Args:
            schedule_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleRetrieveResponse: Retrieve an agent schedule

        Example:
            ```python
            schedule = client.agents.schedules.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._get(
            path_template(
                "/v1/agents/{agentId}/schedules/{scheduleId}", **{"agentId": agent_id, "scheduleId": schedule_id}
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
        agent_id: str,
        cron: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleUpdateResponse:
        """
        Change an agent schedule cron expression. Use updateAgent with enabled to enable or pause the agent and its schedules.

        Args:
            schedule_id: Path parameter.
            agent_id: Path parameter.
            cron: Cron expression for recurring agent runs. Agent enabled and archived state controls whether the schedule runs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleUpdateResponse: Update an agent schedule

        Example:
            ```python
            schedule = client.agents.schedules.update(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                cron="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._patch(
            path_template(
                "/v1/agents/{agentId}/schedules/{scheduleId}", **{"agentId": agent_id, "scheduleId": schedule_id}
            ),
            body=maybe_transform(
                {"cron": cron},
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
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """
        Delete a recurring agent schedule.

        Args:
            schedule_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleDeleteResponse: Delete an agent schedule

        Example:
            ```python
            schedule = client.agents.schedules.delete(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._delete(
            path_template(
                "/v1/agents/{agentId}/schedules/{scheduleId}", **{"agentId": agent_id, "scheduleId": schedule_id}
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
    ) -> ScheduleListResponse:
        """
        List the schedules configured for an agent.

        Args:
            agent_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleListResponse: List agent schedules

        Example:
            ```python
            schedule = await client.agents.schedules.list(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agentId}/schedules", **{"agentId": agent_id}),
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
        agent_id: str,
        *,
        cron: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Create a recurring schedule that starts agent runs using a cron expression.

        Args:
            agent_id: Path parameter.
            cron: Cron expression for recurring agent runs. Agent enabled and archived state controls whether the schedule runs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleCreateResponse: Create an agent schedule

        Example:
            ```python
            schedule = await client.agents.schedules.create(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                cron="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/agents/{agentId}/schedules", **{"agentId": agent_id}),
            body=await async_maybe_transform(
                {"cron": cron},
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
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieve an agent schedule, including its enabled state and next execution time.

        Args:
            schedule_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleRetrieveResponse: Retrieve an agent schedule

        Example:
            ```python
            schedule = await client.agents.schedules.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._get(
            path_template(
                "/v1/agents/{agentId}/schedules/{scheduleId}", **{"agentId": agent_id, "scheduleId": schedule_id}
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
        agent_id: str,
        cron: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleUpdateResponse:
        """
        Change an agent schedule cron expression. Use updateAgent with enabled to enable or pause the agent and its schedules.

        Args:
            schedule_id: Path parameter.
            agent_id: Path parameter.
            cron: Cron expression for recurring agent runs. Agent enabled and archived state controls whether the schedule runs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleUpdateResponse: Update an agent schedule

        Example:
            ```python
            schedule = await client.agents.schedules.update(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                cron="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._patch(
            path_template(
                "/v1/agents/{agentId}/schedules/{scheduleId}", **{"agentId": agent_id, "scheduleId": schedule_id}
            ),
            body=await async_maybe_transform(
                {"cron": cron},
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
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleDeleteResponse:
        """
        Delete a recurring agent schedule.

        Args:
            schedule_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScheduleDeleteResponse: Delete an agent schedule

        Example:
            ```python
            schedule = await client.agents.schedules.delete(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                schedule_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if schedule_id is None or (isinstance(schedule_id, str) and not schedule_id):
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._delete(
            path_template(
                "/v1/agents/{agentId}/schedules/{scheduleId}", **{"agentId": agent_id, "scheduleId": schedule_id}
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
