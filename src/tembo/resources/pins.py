# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

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
from ..types.pin_list_response import PinListResponse
from ..types import pin_list_params, pin_create_params, pin_update_params
from ..types.pin_create_response import PinCreateResponse
from ..types.pin_update_response import PinUpdateResponse
from ..types.pin_delete_response import PinDeleteResponse

__all__ = ["PinsResource", "AsyncPinsResource"]


class PinsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PinsResourceWithRawResponse:
        return PinsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PinsResourceWithStreamingResponse:
        return PinsResourceWithStreamingResponse(self)

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
    ) -> PinListResponse:
        """
        List your pinned resources in pin order.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of pins returned per page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinListResponse: List pins

        Example:
            ```python
            pin = client.pins.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/pins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, pin_list_params.PinListParams),
            ),
            cast_to=PinListResponse,
        )

    def create(
        self,
        *,
        type: Literal["session", "pull_request", "project"],
        id: str,
        placement: pin_create_params.Placement | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinCreateResponse:
        """
        Pin a session, pull request, or project you have permission to access.

        Args:
            type: Kind of resource to pin or unpin: session, pull_request, or project.
            id: ID of the session, pull request, or project, not a separate pin ID.
            placement: Position of a new pin relative to another pin. Omit to add it first. Ignored if the resource is already pinned; use updatePin to reorder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinCreateResponse: Create a pin

        Example:
            ```python
            pin = client.pins.create(
                type="session",
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return self._post(
            "/v1/pins",
            body=maybe_transform(
                {
                    "type": type,
                    "id": id,
                    "placement": placement,
                },
                pin_create_params.PinCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinCreateResponse,
        )

    def update(
        self,
        resource_id: str,
        *,
        resource_type: Literal["session", "pull_request", "project"],
        placement: pin_update_params.Placement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinUpdateResponse:
        """
        Reorder a pinned session, pull request, or project before or after another pin for the authenticated user. Use createPin to pin a resource and deletePin to unpin it.

        Args:
            resource_id: ID of the pinned session, pull request, or project, not a separate pin ID.
            resource_type: Kind of resource to pin or unpin: session, pull_request, or project.
            placement: Reorder an existing pin before or after another pin. Use createPin to pin a resource and deletePin to unpin it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinUpdateResponse: Update a pin

        Example:
            ```python
            pin = client.pins.update(
                resource_type="session",
                resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                placement={"target": {"type": "session", "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}, "position": "before"},
            )
            ```
        """
        if resource_type is None or (isinstance(resource_type, str) and not resource_type):
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if resource_id is None or (isinstance(resource_id, str) and not resource_id):
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._patch(
            path_template(
                "/v1/pins/{resourceType}/{resourceId}", **{"resourceType": resource_type, "resourceId": resource_id}
            ),
            body=maybe_transform(
                {"placement": placement},
                pin_update_params.PinUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinUpdateResponse,
        )

    def delete(
        self,
        resource_id: str,
        *,
        resource_type: Literal["session", "pull_request", "project"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinDeleteResponse:
        """
        Unpin a session, pull request, or project for the authenticated user without deleting or archiving the resource.

        Args:
            resource_id: ID of the pinned session, pull request, or project, not a separate pin ID.
            resource_type: Kind of resource to pin or unpin: session, pull_request, or project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinDeleteResponse: Delete a pin

        Example:
            ```python
            pin = client.pins.delete(
                resource_type="session",
                resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if resource_type is None or (isinstance(resource_type, str) and not resource_type):
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if resource_id is None or (isinstance(resource_id, str) and not resource_id):
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._delete(
            path_template(
                "/v1/pins/{resourceType}/{resourceId}", **{"resourceType": resource_type, "resourceId": resource_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinDeleteResponse,
        )


class AsyncPinsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPinsResourceWithRawResponse:
        return AsyncPinsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPinsResourceWithStreamingResponse:
        return AsyncPinsResourceWithStreamingResponse(self)

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
    ) -> PinListResponse:
        """
        List your pinned resources in pin order.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of pins returned per page.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinListResponse: List pins

        Example:
            ```python
            pin = await client.pins.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/pins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cursor": cursor, "limit": limit}, pin_list_params.PinListParams),
            ),
            cast_to=PinListResponse,
        )

    async def create(
        self,
        *,
        type: Literal["session", "pull_request", "project"],
        id: str,
        placement: pin_create_params.Placement | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinCreateResponse:
        """
        Pin a session, pull request, or project you have permission to access.

        Args:
            type: Kind of resource to pin or unpin: session, pull_request, or project.
            id: ID of the session, pull request, or project, not a separate pin ID.
            placement: Position of a new pin relative to another pin. Omit to add it first. Ignored if the resource is already pinned; use updatePin to reorder.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinCreateResponse: Create a pin

        Example:
            ```python
            pin = await client.pins.create(
                type="session",
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return await self._post(
            "/v1/pins",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "id": id,
                    "placement": placement,
                },
                pin_create_params.PinCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinCreateResponse,
        )

    async def update(
        self,
        resource_id: str,
        *,
        resource_type: Literal["session", "pull_request", "project"],
        placement: pin_update_params.Placement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinUpdateResponse:
        """
        Reorder a pinned session, pull request, or project before or after another pin for the authenticated user. Use createPin to pin a resource and deletePin to unpin it.

        Args:
            resource_id: ID of the pinned session, pull request, or project, not a separate pin ID.
            resource_type: Kind of resource to pin or unpin: session, pull_request, or project.
            placement: Reorder an existing pin before or after another pin. Use createPin to pin a resource and deletePin to unpin it.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinUpdateResponse: Update a pin

        Example:
            ```python
            pin = await client.pins.update(
                resource_type="session",
                resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                placement={"target": {"type": "session", "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}, "position": "before"},
            )
            ```
        """
        if resource_type is None or (isinstance(resource_type, str) and not resource_type):
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if resource_id is None or (isinstance(resource_id, str) and not resource_id):
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._patch(
            path_template(
                "/v1/pins/{resourceType}/{resourceId}", **{"resourceType": resource_type, "resourceId": resource_id}
            ),
            body=await async_maybe_transform(
                {"placement": placement},
                pin_update_params.PinUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinUpdateResponse,
        )

    async def delete(
        self,
        resource_id: str,
        *,
        resource_type: Literal["session", "pull_request", "project"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PinDeleteResponse:
        """
        Unpin a session, pull request, or project for the authenticated user without deleting or archiving the resource.

        Args:
            resource_id: ID of the pinned session, pull request, or project, not a separate pin ID.
            resource_type: Kind of resource to pin or unpin: session, pull_request, or project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PinDeleteResponse: Delete a pin

        Example:
            ```python
            pin = await client.pins.delete(
                resource_type="session",
                resource_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if resource_type is None or (isinstance(resource_type, str) and not resource_type):
            raise ValueError(f"Expected a non-empty value for `resource_type` but received {resource_type!r}")
        if resource_id is None or (isinstance(resource_id, str) and not resource_id):
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._delete(
            path_template(
                "/v1/pins/{resourceType}/{resourceId}", **{"resourceType": resource_type, "resourceId": resource_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinDeleteResponse,
        )


class PinsResourceWithRawResponse:
    def __init__(self, pins: PinsResource) -> None:
        self._pins = pins

        self.list = to_raw_response_wrapper(
            pins.list,
        )
        self.create = to_raw_response_wrapper(
            pins.create,
        )
        self.update = to_raw_response_wrapper(
            pins.update,
        )
        self.delete = to_raw_response_wrapper(
            pins.delete,
        )


class AsyncPinsResourceWithRawResponse:
    def __init__(self, pins: AsyncPinsResource) -> None:
        self._pins = pins

        self.list = async_to_raw_response_wrapper(
            pins.list,
        )
        self.create = async_to_raw_response_wrapper(
            pins.create,
        )
        self.update = async_to_raw_response_wrapper(
            pins.update,
        )
        self.delete = async_to_raw_response_wrapper(
            pins.delete,
        )


class PinsResourceWithStreamingResponse:
    def __init__(self, pins: PinsResource) -> None:
        self._pins = pins

        self.list = to_streamed_response_wrapper(
            pins.list,
        )
        self.create = to_streamed_response_wrapper(
            pins.create,
        )
        self.update = to_streamed_response_wrapper(
            pins.update,
        )
        self.delete = to_streamed_response_wrapper(
            pins.delete,
        )


class AsyncPinsResourceWithStreamingResponse:
    def __init__(self, pins: AsyncPinsResource) -> None:
        self._pins = pins

        self.list = async_to_streamed_response_wrapper(
            pins.list,
        )
        self.create = async_to_streamed_response_wrapper(
            pins.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pins.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            pins.delete,
        )
