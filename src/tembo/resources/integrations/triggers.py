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
from ...types.integrations.trigger_list_response import TriggerListResponse
from ...types.integrations import trigger_list_params, trigger_list_filter_options_params
from ...types.integrations.trigger_retrieve_response import TriggerRetrieveResponse
from ...types.integrations.trigger_list_filter_options_response import TriggerListFilterOptionsResponse

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
        List visible automation triggers grouped by provider.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerListResponse: List integration triggers

        Example:
            ```python
            trigger = client.integrations.triggers.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/integrations/triggers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, trigger_list_params.TriggerListParams),
            ),
            cast_to=TriggerListResponse,
        )

    def retrieve(
        self,
        trigger_name: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Retrieve a trigger definition and its default filter values for an integration in the current organization.

        Args:
            trigger_name: Path parameter.
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerRetrieveResponse: Retrieve an integration trigger

        Example:
            ```python
            trigger = client.integrations.triggers.retrieve(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_name="triggerName",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if trigger_name is None or (isinstance(trigger_name, str) and not trigger_name):
            raise ValueError(f"Expected a non-empty value for `trigger_name` but received {trigger_name!r}")
        return self._get(
            path_template(
                "/v1/integrations/{integrationId}/triggers/{triggerName}",
                **{"integrationId": integration_id, "triggerName": trigger_name},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    def list_filter_options(
        self,
        field: str,
        *,
        integration_id: str,
        trigger_name: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListFilterOptionsResponse:
        """
        List one cursor-page of selectable values for an integration trigger filter field, with optional search.

        Args:
            field: Path parameter.
            integration_id: Path parameter.
            trigger_name: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search selectable values for this integration trigger filter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerListFilterOptionsResponse: List integration trigger filter options

        Example:
            ```python
            trigger = client.integrations.triggers.list_filter_options(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_name="triggerName",
                field="field",
                limit=50,
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if trigger_name is None or (isinstance(trigger_name, str) and not trigger_name):
            raise ValueError(f"Expected a non-empty value for `trigger_name` but received {trigger_name!r}")
        if field is None or (isinstance(field, str) and not field):
            raise ValueError(f"Expected a non-empty value for `field` but received {field!r}")
        return self._get(
            path_template(
                "/v1/integrations/{integrationId}/triggers/{triggerName}/filter-options/{field}",
                **{"integrationId": integration_id, "triggerName": trigger_name, "field": field},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search},
                    trigger_list_filter_options_params.TriggerListFilterOptionsParams,
                ),
            ),
            cast_to=TriggerListFilterOptionsResponse,
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
        List visible automation triggers grouped by provider.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerListResponse: List integration triggers

        Example:
            ```python
            trigger = await client.integrations.triggers.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/integrations/triggers",
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

    async def retrieve(
        self,
        trigger_name: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Retrieve a trigger definition and its default filter values for an integration in the current organization.

        Args:
            trigger_name: Path parameter.
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerRetrieveResponse: Retrieve an integration trigger

        Example:
            ```python
            trigger = await client.integrations.triggers.retrieve(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_name="triggerName",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if trigger_name is None or (isinstance(trigger_name, str) and not trigger_name):
            raise ValueError(f"Expected a non-empty value for `trigger_name` but received {trigger_name!r}")
        return await self._get(
            path_template(
                "/v1/integrations/{integrationId}/triggers/{triggerName}",
                **{"integrationId": integration_id, "triggerName": trigger_name},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    async def list_filter_options(
        self,
        field: str,
        *,
        integration_id: str,
        trigger_name: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListFilterOptionsResponse:
        """
        List one cursor-page of selectable values for an integration trigger filter field, with optional search.

        Args:
            field: Path parameter.
            integration_id: Path parameter.
            trigger_name: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search selectable values for this integration trigger filter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TriggerListFilterOptionsResponse: List integration trigger filter options

        Example:
            ```python
            trigger = await client.integrations.triggers.list_filter_options(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                trigger_name="triggerName",
                field="field",
                limit=50,
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if trigger_name is None or (isinstance(trigger_name, str) and not trigger_name):
            raise ValueError(f"Expected a non-empty value for `trigger_name` but received {trigger_name!r}")
        if field is None or (isinstance(field, str) and not field):
            raise ValueError(f"Expected a non-empty value for `field` but received {field!r}")
        return await self._get(
            path_template(
                "/v1/integrations/{integrationId}/triggers/{triggerName}/filter-options/{field}",
                **{"integrationId": integration_id, "triggerName": trigger_name, "field": field},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search},
                    trigger_list_filter_options_params.TriggerListFilterOptionsParams,
                ),
            ),
            cast_to=TriggerListFilterOptionsResponse,
        )


class TriggersResourceWithRawResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.list = to_raw_response_wrapper(
            triggers.list,
        )
        self.retrieve = to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.list_filter_options = to_raw_response_wrapper(
            triggers.list_filter_options,
        )


class AsyncTriggersResourceWithRawResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.list = async_to_raw_response_wrapper(
            triggers.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.list_filter_options = async_to_raw_response_wrapper(
            triggers.list_filter_options,
        )


class TriggersResourceWithStreamingResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.list = to_streamed_response_wrapper(
            triggers.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.list_filter_options = to_streamed_response_wrapper(
            triggers.list_filter_options,
        )


class AsyncTriggersResourceWithStreamingResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.list = async_to_streamed_response_wrapper(
            triggers.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.list_filter_options = async_to_streamed_response_wrapper(
            triggers.list_filter_options,
        )
