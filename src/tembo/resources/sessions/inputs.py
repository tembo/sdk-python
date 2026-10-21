# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict
from ..._types import SequenceNotStr

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.sessions.input_list_response import InputListResponse
from ...types.sessions.input_update_response import InputUpdateResponse
from ...types.sessions import input_update_params

__all__ = ["InputsResource", "AsyncInputsResource"]


class InputsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InputsResourceWithRawResponse:
        return InputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InputsResourceWithStreamingResponse:
        return InputsResourceWithStreamingResponse(self)

    def list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InputListResponse:
        """
        List pending questions for the active session agent.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InputListResponse: List session inputs

        Example:
            ```python
            input = client.sessions.inputs.list(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/v1/sessions/{sessionId}/inputs", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputListResponse,
        )

    def update(
        self,
        input_id: str,
        *,
        session_id: str,
        answers: Dict[str, SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InputUpdateResponse:
        """
        Answer a pending session question.

        Args:
            input_id: Path parameter.
            session_id: Path parameter.
            answers: Answers keyed by question ID. Send an empty object to skip the questions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InputUpdateResponse: Update a session input

        Example:
            ```python
            input = client.sessions.inputs.update(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                input_id="inputId",
                answers={},
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if input_id is None or (isinstance(input_id, str) and not input_id):
            raise ValueError(f"Expected a non-empty value for `input_id` but received {input_id!r}")
        return self._patch(
            path_template(
                "/v1/sessions/{sessionId}/inputs/{inputId}", **{"sessionId": session_id, "inputId": input_id}
            ),
            body=maybe_transform(
                {"answers": answers},
                input_update_params.InputUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputUpdateResponse,
        )


class AsyncInputsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInputsResourceWithRawResponse:
        return AsyncInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInputsResourceWithStreamingResponse:
        return AsyncInputsResourceWithStreamingResponse(self)

    async def list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InputListResponse:
        """
        List pending questions for the active session agent.

        Args:
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InputListResponse: List session inputs

        Example:
            ```python
            input = await client.sessions.inputs.list(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/v1/sessions/{sessionId}/inputs", **{"sessionId": session_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputListResponse,
        )

    async def update(
        self,
        input_id: str,
        *,
        session_id: str,
        answers: Dict[str, SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InputUpdateResponse:
        """
        Answer a pending session question.

        Args:
            input_id: Path parameter.
            session_id: Path parameter.
            answers: Answers keyed by question ID. Send an empty object to skip the questions.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InputUpdateResponse: Update a session input

        Example:
            ```python
            input = await client.sessions.inputs.update(
                session_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                input_id="inputId",
                answers={},
            )
            ```
        """
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if input_id is None or (isinstance(input_id, str) and not input_id):
            raise ValueError(f"Expected a non-empty value for `input_id` but received {input_id!r}")
        return await self._patch(
            path_template(
                "/v1/sessions/{sessionId}/inputs/{inputId}", **{"sessionId": session_id, "inputId": input_id}
            ),
            body=await async_maybe_transform(
                {"answers": answers},
                input_update_params.InputUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InputUpdateResponse,
        )


class InputsResourceWithRawResponse:
    def __init__(self, inputs: InputsResource) -> None:
        self._inputs = inputs

        self.list = to_raw_response_wrapper(
            inputs.list,
        )
        self.update = to_raw_response_wrapper(
            inputs.update,
        )


class AsyncInputsResourceWithRawResponse:
    def __init__(self, inputs: AsyncInputsResource) -> None:
        self._inputs = inputs

        self.list = async_to_raw_response_wrapper(
            inputs.list,
        )
        self.update = async_to_raw_response_wrapper(
            inputs.update,
        )


class InputsResourceWithStreamingResponse:
    def __init__(self, inputs: InputsResource) -> None:
        self._inputs = inputs

        self.list = to_streamed_response_wrapper(
            inputs.list,
        )
        self.update = to_streamed_response_wrapper(
            inputs.update,
        )


class AsyncInputsResourceWithStreamingResponse:
    def __init__(self, inputs: AsyncInputsResource) -> None:
        self._inputs = inputs

        self.list = async_to_streamed_response_wrapper(
            inputs.list,
        )
        self.update = async_to_streamed_response_wrapper(
            inputs.update,
        )
