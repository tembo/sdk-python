# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
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
from ..types.model_list_response import ModelListResponse
from ..types import model_list_params, model_update_params
from ..types.model_update_response import ModelUpdateResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self)

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
    ) -> ModelListResponse:
        """
        List the models available to the current organization, including enablement and inference-provider access.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ModelListResponse: List models

        Example:
            ```python
            model = client.models.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/models",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, model_list_params.ModelListParams),
            ),
            cast_to=ModelListResponse,
        )

    def update(
        self,
        model_name: str,
        *,
        enabled: bool | Omit = omit,
        inference_provider: Optional[
            Literal["TemboManagedInference", "BYOK", "AWSBedrock", "GCPVertexAI", "OpenRouter"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelUpdateResponse:
        """
        Enable or disable an organization model, or select its inference provider.

        Args:
            model_name: Path parameter.
            enabled: Enable or disable this model for the organization.
            inference_provider: Select the inference provider used to run this model. Use listModels to discover available provider access.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ModelUpdateResponse: Update a model

        Example:
            ```python
            model = client.models.update(
                model_name="modelName",
            )
            ```
        """
        if model_name is None or (isinstance(model_name, str) and not model_name):
            raise ValueError(f"Expected a non-empty value for `model_name` but received {model_name!r}")
        return self._patch(
            path_template("/v1/models/{modelName}", **{"modelName": model_name}),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "inference_provider": inference_provider,
                },
                model_update_params.ModelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelUpdateResponse,
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self)

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
    ) -> ModelListResponse:
        """
        List the models available to the current organization, including enablement and inference-provider access.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ModelListResponse: List models

        Example:
            ```python
            model = await client.models.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/models",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, model_list_params.ModelListParams
                ),
            ),
            cast_to=ModelListResponse,
        )

    async def update(
        self,
        model_name: str,
        *,
        enabled: bool | Omit = omit,
        inference_provider: Optional[
            Literal["TemboManagedInference", "BYOK", "AWSBedrock", "GCPVertexAI", "OpenRouter"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelUpdateResponse:
        """
        Enable or disable an organization model, or select its inference provider.

        Args:
            model_name: Path parameter.
            enabled: Enable or disable this model for the organization.
            inference_provider: Select the inference provider used to run this model. Use listModels to discover available provider access.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ModelUpdateResponse: Update a model

        Example:
            ```python
            model = await client.models.update(
                model_name="modelName",
            )
            ```
        """
        if model_name is None or (isinstance(model_name, str) and not model_name):
            raise ValueError(f"Expected a non-empty value for `model_name` but received {model_name!r}")
        return await self._patch(
            path_template("/v1/models/{modelName}", **{"modelName": model_name}),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "inference_provider": inference_provider,
                },
                model_update_params.ModelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelUpdateResponse,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.list = to_raw_response_wrapper(
            models.list,
        )
        self.update = to_raw_response_wrapper(
            models.update,
        )


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.list = async_to_raw_response_wrapper(
            models.list,
        )
        self.update = async_to_raw_response_wrapper(
            models.update,
        )


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.list = to_streamed_response_wrapper(
            models.list,
        )
        self.update = to_streamed_response_wrapper(
            models.update,
        )


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.list = async_to_streamed_response_wrapper(
            models.list,
        )
        self.update = async_to_streamed_response_wrapper(
            models.update,
        )
