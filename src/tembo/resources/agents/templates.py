# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

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
from ...types.agents.template_list_response import TemplateListResponse
from ...types.agents import template_list_params
from ...types.agents.template_retrieve_response import TemplateRetrieveResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Literal[
            "addTestCoverage",
            "addTestCoverageFromJira",
            "autoAgentsMdMaintainer",
            "autoDocsMaintainer",
            "publicApiReleaseMaintainer",
            "commitOfTheDay",
            "customerHealthMonitoringAgent",
            "deadCodeCleanup",
            "dependencySweepAgent",
            "autoFixCi",
            "autoFixSentryError",
            "dailySlackChangelog",
            "duplicateTicketDetector",
            "fixBugsReportedInSlack",
            "enrichGithubIssue",
            "enrichJiraIssue",
            "enrichLinearIssue",
            "hubspotCallTaskCoach",
            "hubspotEmailTaskDrafter",
            "hubspotTicketToLinearBug",
            "prDescription",
            "prReview",
            "pagePerformanceReport",
            "prioritizeSentry",
            "productFaqAgent",
            "productFinanceAgent",
            "queryPerformanceReport",
            "securityFixFromJira",
            "securityScan",
            "skillProgressionMap",
            "slackChannelListener",
            "slopCop",
            "testAudit",
            "staleCodeComments",
            "stalePullRequestNotifier",
            "summarizeChangesDaily",
            "triageNewJiraBug",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        List reusable agent templates and their configuration requirements.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TemplateListResponse: List agent templates

        Example:
            ```python
            template = client.agents.templates.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/agents/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor, "limit": limit}, template_list_params.TemplateListParams),
            ),
            cast_to=TemplateListResponse,
        )

    def retrieve(
        self,
        template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRetrieveResponse:
        """
        Retrieve a reusable agent template by name, including its instructions and required parameters.

        Args:
            template_name: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TemplateRetrieveResponse: Retrieve an agent template

        Example:
            ```python
            template = client.agents.templates.retrieve(
                template_name="templateName",
            )
            ```
        """
        if template_name is None or (isinstance(template_name, str) and not template_name):
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return self._get(
            path_template("/v1/agents/templates/{templateName}", **{"templateName": template_name}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRetrieveResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: Literal[
            "addTestCoverage",
            "addTestCoverageFromJira",
            "autoAgentsMdMaintainer",
            "autoDocsMaintainer",
            "publicApiReleaseMaintainer",
            "commitOfTheDay",
            "customerHealthMonitoringAgent",
            "deadCodeCleanup",
            "dependencySweepAgent",
            "autoFixCi",
            "autoFixSentryError",
            "dailySlackChangelog",
            "duplicateTicketDetector",
            "fixBugsReportedInSlack",
            "enrichGithubIssue",
            "enrichJiraIssue",
            "enrichLinearIssue",
            "hubspotCallTaskCoach",
            "hubspotEmailTaskDrafter",
            "hubspotTicketToLinearBug",
            "prDescription",
            "prReview",
            "pagePerformanceReport",
            "prioritizeSentry",
            "productFaqAgent",
            "productFinanceAgent",
            "queryPerformanceReport",
            "securityFixFromJira",
            "securityScan",
            "skillProgressionMap",
            "slackChannelListener",
            "slopCop",
            "testAudit",
            "staleCodeComments",
            "stalePullRequestNotifier",
            "summarizeChangesDaily",
            "triageNewJiraBug",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        List reusable agent templates and their configuration requirements.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TemplateListResponse: List agent templates

        Example:
            ```python
            template = await client.agents.templates.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/agents/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit}, template_list_params.TemplateListParams
                ),
            ),
            cast_to=TemplateListResponse,
        )

    async def retrieve(
        self,
        template_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRetrieveResponse:
        """
        Retrieve a reusable agent template by name, including its instructions and required parameters.

        Args:
            template_name: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TemplateRetrieveResponse: Retrieve an agent template

        Example:
            ```python
            template = await client.agents.templates.retrieve(
                template_name="templateName",
            )
            ```
        """
        if template_name is None or (isinstance(template_name, str) and not template_name):
            raise ValueError(f"Expected a non-empty value for `template_name` but received {template_name!r}")
        return await self._get(
            path_template("/v1/agents/templates/{templateName}", **{"templateName": template_name}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateRetrieveResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.retrieve = to_raw_response_wrapper(
            templates.retrieve,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            templates.retrieve,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            templates.retrieve,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            templates.retrieve,
        )
