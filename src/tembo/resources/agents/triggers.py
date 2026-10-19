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
from ...types.agents.trigger_list_response import TriggerListResponse
from ...types.agents import trigger_list_params, trigger_create_params, trigger_update_params
from ...types.agents.trigger_create_response import TriggerCreateResponse
from ...types.agents.trigger_filters_param import TriggerFiltersParam
from ...types.agents.trigger_retrieve_response import TriggerRetrieveResponse
from ...types.agents.trigger_update_response import TriggerUpdateResponse
from ...types.agents.trigger_delete_response import TriggerDeleteResponse

__all__ = ["TriggersResource", "AsyncTriggersResource"]


class TriggersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TriggersResourceWithRawResponse:
        return TriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggersResourceWithStreamingResponse:
        return TriggersResourceWithStreamingResponse(self)

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
    ) -> TriggerListResponse:
        """
        List the integration events configured to start runs of an agent.

        Args:
            agent_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerListResponse: List agent triggers

        Example:
            ```python
            trigger = client.agents.triggers.list(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agentId}/triggers", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, trigger_list_params.TriggerListParams),
            ),
            cast_to=TriggerListResponse,
        )

    def create(
        self,
        agent_id: str,
        *,
        name: str,
        integration_type: str | Omit = omit,
        integration_id: str | Omit = omit,
        filters: TriggerFiltersParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerCreateResponse:
        """
        Configure an integration event to start agent runs. Available filters depend on the integration and event name.

        Args:
            agent_id: Path parameter.
            name: Integration event name. Use listIntegrationTriggers to discover supported triggers.
            integration_type: Provider type for the trigger, such as github or slack.
            integration_id: Connected integration that supplies trigger events.
            filters: Event-specific trigger filters. Use retrieveIntegrationTrigger and listIntegrationTriggerFilterOptions to discover supported fields and values.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerCreateResponse: Create an agent trigger

        Example:
            ```python
            trigger = client.agents.triggers.create(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/agents/{agentId}/triggers", **{"agentId": agent_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "integration_type": integration_type,
                    "integration_id": integration_id,
                    "filters": filters,
                },
                trigger_create_params.TriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerCreateResponse,
        )

    def retrieve(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Retrieve an agent trigger and its integration event filters.

        Args:
            trigger_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerRetrieveResponse: Retrieve an agent trigger

        Example:
            ```python
            trigger = client.agents.triggers.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if trigger_id is None or (isinstance(trigger_id, str) and not trigger_id):
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._get(
            path_template(
                "/v1/agents/{agentId}/triggers/{triggerId}", **{"agentId": agent_id, "triggerId": trigger_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    def update(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        name: str,
        integration_id: str | Omit = omit,
        filters: TriggerFiltersParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerUpdateResponse:
        """
        Change an agent trigger event, integration, or filters. Use updateAgent with enabled to enable or pause the agent and its triggers.

        Args:
            trigger_id: Path parameter.
            agent_id: Path parameter.
            name: Integration event name. Use listIntegrationTriggers to discover supported triggers.
            integration_id: Connected integration that supplies trigger events.
            filters: Event-specific trigger filters. Use retrieveIntegrationTrigger and listIntegrationTriggerFilterOptions to discover supported fields and values.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerUpdateResponse: Update an agent trigger

        Example:
            ```python
            trigger = client.agents.triggers.update(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if trigger_id is None or (isinstance(trigger_id, str) and not trigger_id):
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._patch(
            path_template(
                "/v1/agents/{agentId}/triggers/{triggerId}", **{"agentId": agent_id, "triggerId": trigger_id}
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "integration_id": integration_id,
                    "filters": filters,
                },
                trigger_update_params.TriggerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerUpdateResponse,
        )

    def delete(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerDeleteResponse:
        """
        Delete an integration event trigger for an agent.

        Args:
            trigger_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerDeleteResponse: Delete an agent trigger

        Example:
            ```python
            trigger = client.agents.triggers.delete(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if trigger_id is None or (isinstance(trigger_id, str) and not trigger_id):
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._delete(
            path_template(
                "/v1/agents/{agentId}/triggers/{triggerId}", **{"agentId": agent_id, "triggerId": trigger_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerDeleteResponse,
        )


class AsyncTriggersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTriggersResourceWithRawResponse:
        return AsyncTriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggersResourceWithStreamingResponse:
        return AsyncTriggersResourceWithStreamingResponse(self)

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
    ) -> TriggerListResponse:
        """
        List the integration events configured to start runs of an agent.

        Args:
            agent_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerListResponse: List agent triggers

        Example:
            ```python
            trigger = await client.agents.triggers.list(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agentId}/triggers", **{"agentId": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, trigger_list_params.TriggerListParams
                ),
            ),
            cast_to=TriggerListResponse,
        )

    async def create(
        self,
        agent_id: str,
        *,
        name: str,
        integration_type: str | Omit = omit,
        integration_id: str | Omit = omit,
        filters: TriggerFiltersParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerCreateResponse:
        """
        Configure an integration event to start agent runs. Available filters depend on the integration and event name.

        Args:
            agent_id: Path parameter.
            name: Integration event name. Use listIntegrationTriggers to discover supported triggers.
            integration_type: Provider type for the trigger, such as github or slack.
            integration_id: Connected integration that supplies trigger events.
            filters: Event-specific trigger filters. Use retrieveIntegrationTrigger and listIntegrationTriggerFilterOptions to discover supported fields and values.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerCreateResponse: Create an agent trigger

        Example:
            ```python
            trigger = await client.agents.triggers.create(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/agents/{agentId}/triggers", **{"agentId": agent_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "integration_type": integration_type,
                    "integration_id": integration_id,
                    "filters": filters,
                },
                trigger_create_params.TriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerCreateResponse,
        )

    async def retrieve(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Retrieve an agent trigger and its integration event filters.

        Args:
            trigger_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerRetrieveResponse: Retrieve an agent trigger

        Example:
            ```python
            trigger = await client.agents.triggers.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if trigger_id is None or (isinstance(trigger_id, str) and not trigger_id):
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._get(
            path_template(
                "/v1/agents/{agentId}/triggers/{triggerId}", **{"agentId": agent_id, "triggerId": trigger_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    async def update(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        name: str,
        integration_id: str | Omit = omit,
        filters: TriggerFiltersParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerUpdateResponse:
        """
        Change an agent trigger event, integration, or filters. Use updateAgent with enabled to enable or pause the agent and its triggers.

        Args:
            trigger_id: Path parameter.
            agent_id: Path parameter.
            name: Integration event name. Use listIntegrationTriggers to discover supported triggers.
            integration_id: Connected integration that supplies trigger events.
            filters: Event-specific trigger filters. Use retrieveIntegrationTrigger and listIntegrationTriggerFilterOptions to discover supported fields and values.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerUpdateResponse: Update an agent trigger

        Example:
            ```python
            trigger = await client.agents.triggers.update(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if trigger_id is None or (isinstance(trigger_id, str) and not trigger_id):
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._patch(
            path_template(
                "/v1/agents/{agentId}/triggers/{triggerId}", **{"agentId": agent_id, "triggerId": trigger_id}
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "integration_id": integration_id,
                    "filters": filters,
                },
                trigger_update_params.TriggerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerUpdateResponse,
        )

    async def delete(
        self,
        trigger_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerDeleteResponse:
        """
        Delete an integration event trigger for an agent.

        Args:
            trigger_id: Path parameter.
            agent_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerDeleteResponse: Delete an agent trigger

        Example:
            ```python
            trigger = await client.agents.triggers.delete(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if trigger_id is None or (isinstance(trigger_id, str) and not trigger_id):
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._delete(
            path_template(
                "/v1/agents/{agentId}/triggers/{triggerId}", **{"agentId": agent_id, "triggerId": trigger_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerDeleteResponse,
        )


class TriggersResourceWithRawResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.list = to_raw_response_wrapper(
            triggers.list,
        )
        self.create = to_raw_response_wrapper(
            triggers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            triggers.update,
        )
        self.delete = to_raw_response_wrapper(
            triggers.delete,
        )


class AsyncTriggersResourceWithRawResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.list = async_to_raw_response_wrapper(
            triggers.list,
        )
        self.create = async_to_raw_response_wrapper(
            triggers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            triggers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            triggers.delete,
        )


class TriggersResourceWithStreamingResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.list = to_streamed_response_wrapper(
            triggers.list,
        )
        self.create = to_streamed_response_wrapper(
            triggers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            triggers.update,
        )
        self.delete = to_streamed_response_wrapper(
            triggers.delete,
        )


class AsyncTriggersResourceWithStreamingResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.list = async_to_streamed_response_wrapper(
            triggers.list,
        )
        self.create = async_to_streamed_response_wrapper(
            triggers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            triggers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            triggers.delete,
        )
