# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Literal, overload
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform, required_args
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .providers import (
    ProvidersResource,
    AsyncProvidersResource,
    ProvidersResourceWithRawResponse,
    AsyncProvidersResourceWithRawResponse,
    ProvidersResourceWithStreamingResponse,
    AsyncProvidersResourceWithStreamingResponse,
)
from .triggers import (
    TriggersResource,
    AsyncTriggersResource,
    TriggersResourceWithRawResponse,
    AsyncTriggersResourceWithRawResponse,
    TriggersResourceWithStreamingResponse,
    AsyncTriggersResourceWithStreamingResponse,
)
from ...types.integration_list_response import IntegrationListResponse
from ...types import (
    integration_list_params,
    integration_create_params,
    integration_update_params,
    integration_authorize_params,
    integration_sync_params,
    integration_sync_all_params,
    integration_retrieve_sync_status_params,
    integration_list_sentry_environments_params,
    integration_list_slack_channels_params,
)
from ...types.integration_create_response import IntegrationCreateResponse
from ...types.integration_retrieve_response import IntegrationRetrieveResponse
from ...types.integration_update_response import IntegrationUpdateResponse
from ...types.integration_delete_response import IntegrationDeleteResponse
from ...types.integration_authorize_response import IntegrationAuthorizeResponse
from ...types.integration_test_response import IntegrationTestResponse
from ...types.integration_sync_response import IntegrationSyncResponse
from ...types.integration_sync_all_response import IntegrationSyncAllResponse
from ...types.integration_retrieve_sync_status_response import IntegrationRetrieveSyncStatusResponse
from ...types.integration_retrieve_rate_limit_response import IntegrationRetrieveRateLimitResponse
from ...types.integration_list_sentry_environments_response import IntegrationListSentryEnvironmentsResponse
from ...types.integration_list_slack_channels_response import IntegrationListSlackChannelsResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def providers(self) -> ProvidersResource:
        return ProvidersResource(self._client)

    @cached_property
    def triggers(self) -> TriggersResource:
        return TriggersResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        enabled: bool | Omit = omit,
        has_enabled_repositories: bool | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        type: SequenceNotStr[str] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        exclude_organization_name: str | Omit = omit,
        include_total: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListResponse:
        """
        List integrations visible to the current organization or authenticated admin.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            enabled: Filter by whether integrations are enabled.
            has_enabled_repositories: Filter by whether integrations have enabled repositories.
            ids: Filter by integration IDs, supplied as a comma-separated list.
            search: Search integration provider types and external IDs.
            type: Filter provider types, supplied as a comma-separated list.
            created_after: Only integrations created after this ISO 8601 timestamp.
            exclude_organization_name: Exclude integrations belonging to the named organization within the caller access scope.
            include_total: Include totalCount for matching integrations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListResponse: List integrations

        Example:
            ```python
            integration = client.integrations.list(
                limit=50,
                include_total=False,
            )
            ```
        """
        return self._get(
            "/v1/integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "enabled": enabled,
                        "has_enabled_repositories": has_enabled_repositories,
                        "ids": ids,
                        "search": search,
                        "type": type,
                        "created_after": created_after,
                        "exclude_organization_name": exclude_organization_name,
                        "include_total": include_total,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            cast_to=IntegrationListResponse,
        )

    @overload
    def create(
        self,
        *,
        environment: str,
        role_arn: str,
        type: Literal["aws"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    def create(
        self,
        *,
        project_id: str,
        service_account_json: str,
        type: Literal["bigquery"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    def create(
        self,
        *,
        access_token: str,
        type: Literal["gitlab"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    def create(
        self,
        *,
        gateway: str,
        instance_name: str,
        password: str,
        protocol: Literal["fortinet", "anyconnect", "gp", "nc"],
        type: Literal["openconnect"],
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    def create(
        self,
        *,
        ca_certificate: str | Omit = omit,
        connection_string: str,
        instance_name: str,
        type: Literal["postgres"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        organization_id: str,
        organization_name: str | Omit = omit,
        type: Literal["snyk"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    def create(
        self,
        *,
        instance_name: str,
        oauth_client_id: str,
        oauth_client_secret: str,
        tags: SequenceNotStr[str],
        tailnet: str | Omit = omit,
        type: Literal["tailscale"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @required_args(
        ["environment", "role_arn", "type"],
        ["project_id", "service_account_json", "type"],
        ["access_token", "type"],
        ["gateway", "instance_name", "password", "protocol", "type", "username"],
        ["connection_string", "instance_name", "type"],
        ["client_id", "client_secret", "organization_id", "type"],
        ["instance_name", "oauth_client_id", "oauth_client_secret", "tags", "type"],
    )
    def create(
        self,
        *,
        environment: str | Omit = omit,
        role_arn: str | Omit = omit,
        type: Union[
            Literal["aws"],
            Literal["bigquery"],
            Literal["gitlab"],
            Literal["openconnect"],
            Literal["postgres"],
            Literal["snyk"],
            Literal["tailscale"],
        ],
        project_id: str | Omit = omit,
        service_account_json: str | Omit = omit,
        access_token: str | Omit = omit,
        gateway: str | Omit = omit,
        instance_name: str | Omit = omit,
        password: str | Omit = omit,
        protocol: Literal["fortinet", "anyconnect", "gp", "nc"] | Omit = omit,
        username: str | Omit = omit,
        ca_certificate: str | Omit = omit,
        connection_string: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        organization_id: str | Omit = omit,
        organization_name: str | Omit = omit,
        oauth_client_id: str | Omit = omit,
        oauth_client_secret: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tailnet: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse:
        """
        Connect AWS, BigQuery, GitLab, PostgreSQL, Snyk, OpenConnect VPN, or Tailscale using provider credentials. For browser-authorized providers, use listIntegrationProviders and authorizeIntegration instead.

        Args:
            environment: Display label for the AWS environment.
            role_arn: AWS IAM role ARN to assume for account access.
            type: Create an AWS account integration.
            project_id: Google Cloud project ID for BigQuery.
            service_account_json: Google Cloud service-account JSON credentials for BigQuery.
            access_token: GitLab access token used to connect the integration.
            gateway: VPN gateway hostname or URL for OpenConnect.
            instance_name: Display name for the VPN connection.
            password: VPN login password.
            protocol: OpenConnect VPN protocol supported by the gateway.
            username: VPN login username.
            ca_certificate: Optional CA certificate for the PostgreSQL TLS connection.
            connection_string: PostgreSQL connection URI, including credentials. Stored as secret configuration.
            client_id: Snyk service-account client ID.
            client_secret: Snyk service-account client secret.
            organization_id: Snyk organization ID, not a Tembo organization ID. Discover choices with discoverSnykOrganizations.
            organization_name: Optional display name for the Snyk organization.
            oauth_client_id: Tailscale OAuth client ID authorized to create tagged devices.
            oauth_client_secret: Tailscale OAuth client secret.
            tags: Tags to assign to connected devices, such as tag:tembo. Must be authorized for the OAuth client.
            tailnet: Tailnet name. The default - uses the OAuth client tailnet.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationCreateResponse: Create an integration

        Example:
            ```python
            integration = client.integrations.create(
                environment="x",
                role_arn="x",
                type="aws",
            )
            ```
        """
        return self._post(
            "/v1/integrations",
            body=maybe_transform(
                {
                    "environment": environment,
                    "role_arn": role_arn,
                    "type": type,
                    "project_id": project_id,
                    "service_account_json": service_account_json,
                    "access_token": access_token,
                    "gateway": gateway,
                    "instance_name": instance_name,
                    "password": password,
                    "protocol": protocol,
                    "username": username,
                    "ca_certificate": ca_certificate,
                    "connection_string": connection_string,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "organization_id": organization_id,
                    "organization_name": organization_name,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "tags": tags,
                    "tailnet": tailnet,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateResponse,
        )

    def retrieve(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRetrieveResponse:
        """
        Retrieve an integration and its configuration.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationRetrieveResponse: Retrieve an integration

        Example:
            ```python
            integration = client.integrations.retrieve(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            path_template("/v1/integrations/{integrationId}", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationRetrieveResponse,
        )

    @overload
    def update(
        self,
        integration_id: str,
        *,
        settings: integration_update_params.VariantSettings,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @overload
    def update(
        self,
        integration_id: str,
        *,
        aws: integration_update_params.Variant2Aws,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @overload
    def update(
        self,
        integration_id: str,
        *,
        postgres: integration_update_params.Variant3Postgres,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @overload
    def update(
        self,
        integration_id: str,
        *,
        atlassian_service_account: Optional[integration_update_params.Variant4AtlassianServiceAccount],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @required_args(["settings"], ["aws"], ["postgres"], ["atlassian_service_account"])
    def update(
        self,
        integration_id: str,
        *,
        settings: integration_update_params.VariantSettings | Omit = omit,
        aws: integration_update_params.Variant2Aws | Omit = omit,
        postgres: integration_update_params.Variant3Postgres | Omit = omit,
        atlassian_service_account: Optional[integration_update_params.Variant4AtlassianServiceAccount] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse:
        """
        Update integration settings such as the default repository, Slack channel restrictions, automatic solving, or Sentry environments; replace AWS or PostgreSQL configuration; set or remove Atlassian service-account credentials.

        Args:
            integration_id: Path parameter.
            settings: Update integration settings, preserving unspecified settings.
            aws: Replace AWS environment and assumed-role configuration.
            postgres: Replace PostgreSQL connection configuration.
            atlassian_service_account: Set Atlassian service-account OAuth credentials for triggers, or null to remove them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationUpdateResponse: Update an integration

        Example:
            ```python
            integration = client.integrations.update(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                settings={},
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._patch(
            path_template("/v1/integrations/{integrationId}", **{"integrationId": integration_id}),
            body=maybe_transform(
                {
                    "settings": settings,
                    "aws": aws,
                    "postgres": postgres,
                    "atlassian_service_account": atlassian_service_account,
                },
                integration_update_params.IntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationUpdateResponse,
        )

    def delete(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationDeleteResponse:
        """
        Uninstall an integration from its provider when supported, then delete it from Tembo.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationDeleteResponse: Delete an integration

        Example:
            ```python
            integration = client.integrations.delete(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._delete(
            path_template("/v1/integrations/{integrationId}", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationDeleteResponse,
        )

    def authorize(
        self,
        integration_id: str,
        *,
        return_url: str | Omit = omit,
        capability: Literal["confluenceTriggers"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationAuthorizeResponse:
        """
        Return the provider authorization URL for an integration.

        Args:
            integration_id: Path parameter.
            return_url: URL to return to after provider authorization. Must use HTTPS or localhost HTTP.
            capability: Request authorization for Confluence automation triggers instead of the default integration capability.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationAuthorizeResponse: Authorize an integration

        Example:
            ```python
            integration = client.integrations.authorize(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            path_template("/v1/integrations/{integrationId}/authorize", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"return_url": return_url, "capability": capability},
                    integration_authorize_params.IntegrationAuthorizeParams,
                ),
            ),
            cast_to=IntegrationAuthorizeResponse,
        )

    def test(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationTestResponse:
        """
        Test the saved provider connection.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationTestResponse: Test an integration

        Example:
            ```python
            integration = client.integrations.test(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            path_template("/v1/integrations/{integrationId}/test", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationTestResponse,
        )

    def sync(
        self,
        integration_id: str,
        *,
        mode: Literal["immediate", "queued"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationSyncResponse:
        """
        Queue or immediately perform an integration sync.

        Args:
            integration_id: Path parameter.
            mode: queued schedules a background integration sync; immediate performs the sync in this request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationSyncResponse: Sync an integration

        Example:
            ```python
            integration = client.integrations.sync(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                mode="queued",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            path_template("/v1/integrations/{integrationId}/sync", **{"integrationId": integration_id}),
            body=maybe_transform(
                {"mode": mode},
                integration_sync_params.IntegrationSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSyncResponse,
        )

    def sync_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationSyncAllResponse:
        """
        Queue integration and pull-request sync jobs for integrations with enabled repositories.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationSyncAllResponse: Sync eligible integrations

        Example:
            ```python
            integration = client.integrations.sync_all()
            ```
        """
        return self._post(
            "/v1/integrations/sync",
            body=maybe_transform(
                {},
                integration_sync_all_params.IntegrationSyncAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSyncAllResponse,
        )

    def retrieve_sync_status(
        self,
        *,
        integration_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRetrieveSyncStatusResponse:
        """
        Count active sync jobs for an integration or eligible integrations.

        Args:
            integration_id: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationRetrieveSyncStatusResponse: Retrieve integration sync status

        Example:
            ```python
            integration = client.integrations.retrieve_sync_status()
            ```
        """
        return self._get(
            "/v1/integrations/sync/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id},
                    integration_retrieve_sync_status_params.IntegrationRetrieveSyncStatusParams,
                ),
            ),
            cast_to=IntegrationRetrieveSyncStatusResponse,
        )

    def retrieve_rate_limit(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRetrieveRateLimitResponse:
        """
        Retrieve the GitHub installation rate-limit state.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationRetrieveRateLimitResponse: Retrieve an integration rate limit

        Example:
            ```python
            integration = client.integrations.retrieve_rate_limit(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            path_template("/v1/integrations/{integrationId}/rate-limit", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationRetrieveRateLimitResponse,
        )

    def list_sentry_environments(
        self,
        integration_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListSentryEnvironmentsResponse:
        """
        List environments visible to a Sentry integration.

        Args:
            integration_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListSentryEnvironmentsResponse: List Sentry environments

        Example:
            ```python
            integration = client.integrations.list_sentry_environments(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            path_template("/v1/integrations/{integrationId}/sentry-environments", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit},
                    integration_list_sentry_environments_params.IntegrationListSentryEnvironmentsParams,
                ),
            ),
            cast_to=IntegrationListSentryEnvironmentsResponse,
        )

    def list_slack_channels(
        self,
        integration_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListSlackChannelsResponse:
        """
        List channels visible to a Slack integration.

        Args:
            integration_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search Slack channel names.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListSlackChannelsResponse: List Slack channels

        Example:
            ```python
            integration = client.integrations.list_slack_channels(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            path_template("/v1/integrations/{integrationId}/slack-channels", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search},
                    integration_list_slack_channels_params.IntegrationListSlackChannelsParams,
                ),
            ),
            cast_to=IntegrationListSlackChannelsResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def providers(self) -> AsyncProvidersResource:
        return AsyncProvidersResource(self._client)

    @cached_property
    def triggers(self) -> AsyncTriggersResource:
        return AsyncTriggersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        enabled: bool | Omit = omit,
        has_enabled_repositories: bool | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        type: SequenceNotStr[str] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        exclude_organization_name: str | Omit = omit,
        include_total: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListResponse:
        """
        List integrations visible to the current organization or authenticated admin.

        Args:
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            enabled: Filter by whether integrations are enabled.
            has_enabled_repositories: Filter by whether integrations have enabled repositories.
            ids: Filter by integration IDs, supplied as a comma-separated list.
            search: Search integration provider types and external IDs.
            type: Filter provider types, supplied as a comma-separated list.
            created_after: Only integrations created after this ISO 8601 timestamp.
            exclude_organization_name: Exclude integrations belonging to the named organization within the caller access scope.
            include_total: Include totalCount for matching integrations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListResponse: List integrations

        Example:
            ```python
            integration = await client.integrations.list(
                limit=50,
                include_total=False,
            )
            ```
        """
        return await self._get(
            "/v1/integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "enabled": enabled,
                        "has_enabled_repositories": has_enabled_repositories,
                        "ids": ids,
                        "search": search,
                        "type": type,
                        "created_after": created_after,
                        "exclude_organization_name": exclude_organization_name,
                        "include_total": include_total,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            cast_to=IntegrationListResponse,
        )

    @overload
    async def create(
        self,
        *,
        environment: str,
        role_arn: str,
        type: Literal["aws"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        project_id: str,
        service_account_json: str,
        type: Literal["bigquery"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        access_token: str,
        type: Literal["gitlab"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        gateway: str,
        instance_name: str,
        password: str,
        protocol: Literal["fortinet", "anyconnect", "gp", "nc"],
        type: Literal["openconnect"],
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        ca_certificate: str | Omit = omit,
        connection_string: str,
        instance_name: str,
        type: Literal["postgres"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        organization_id: str,
        organization_name: str | Omit = omit,
        type: Literal["snyk"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        instance_name: str,
        oauth_client_id: str,
        oauth_client_secret: str,
        tags: SequenceNotStr[str],
        tailnet: str | Omit = omit,
        type: Literal["tailscale"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse: ...

    @required_args(
        ["environment", "role_arn", "type"],
        ["project_id", "service_account_json", "type"],
        ["access_token", "type"],
        ["gateway", "instance_name", "password", "protocol", "type", "username"],
        ["connection_string", "instance_name", "type"],
        ["client_id", "client_secret", "organization_id", "type"],
        ["instance_name", "oauth_client_id", "oauth_client_secret", "tags", "type"],
    )
    async def create(
        self,
        *,
        environment: str | Omit = omit,
        role_arn: str | Omit = omit,
        type: Union[
            Literal["aws"],
            Literal["bigquery"],
            Literal["gitlab"],
            Literal["openconnect"],
            Literal["postgres"],
            Literal["snyk"],
            Literal["tailscale"],
        ],
        project_id: str | Omit = omit,
        service_account_json: str | Omit = omit,
        access_token: str | Omit = omit,
        gateway: str | Omit = omit,
        instance_name: str | Omit = omit,
        password: str | Omit = omit,
        protocol: Literal["fortinet", "anyconnect", "gp", "nc"] | Omit = omit,
        username: str | Omit = omit,
        ca_certificate: str | Omit = omit,
        connection_string: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        organization_id: str | Omit = omit,
        organization_name: str | Omit = omit,
        oauth_client_id: str | Omit = omit,
        oauth_client_secret: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tailnet: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse:
        """
        Connect AWS, BigQuery, GitLab, PostgreSQL, Snyk, OpenConnect VPN, or Tailscale using provider credentials. For browser-authorized providers, use listIntegrationProviders and authorizeIntegration instead.

        Args:
            environment: Display label for the AWS environment.
            role_arn: AWS IAM role ARN to assume for account access.
            type: Create an AWS account integration.
            project_id: Google Cloud project ID for BigQuery.
            service_account_json: Google Cloud service-account JSON credentials for BigQuery.
            access_token: GitLab access token used to connect the integration.
            gateway: VPN gateway hostname or URL for OpenConnect.
            instance_name: Display name for the VPN connection.
            password: VPN login password.
            protocol: OpenConnect VPN protocol supported by the gateway.
            username: VPN login username.
            ca_certificate: Optional CA certificate for the PostgreSQL TLS connection.
            connection_string: PostgreSQL connection URI, including credentials. Stored as secret configuration.
            client_id: Snyk service-account client ID.
            client_secret: Snyk service-account client secret.
            organization_id: Snyk organization ID, not a Tembo organization ID. Discover choices with discoverSnykOrganizations.
            organization_name: Optional display name for the Snyk organization.
            oauth_client_id: Tailscale OAuth client ID authorized to create tagged devices.
            oauth_client_secret: Tailscale OAuth client secret.
            tags: Tags to assign to connected devices, such as tag:tembo. Must be authorized for the OAuth client.
            tailnet: Tailnet name. The default - uses the OAuth client tailnet.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationCreateResponse: Create an integration

        Example:
            ```python
            integration = await client.integrations.create(
                environment="x",
                role_arn="x",
                type="aws",
            )
            ```
        """
        return await self._post(
            "/v1/integrations",
            body=await async_maybe_transform(
                {
                    "environment": environment,
                    "role_arn": role_arn,
                    "type": type,
                    "project_id": project_id,
                    "service_account_json": service_account_json,
                    "access_token": access_token,
                    "gateway": gateway,
                    "instance_name": instance_name,
                    "password": password,
                    "protocol": protocol,
                    "username": username,
                    "ca_certificate": ca_certificate,
                    "connection_string": connection_string,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "organization_id": organization_id,
                    "organization_name": organization_name,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "tags": tags,
                    "tailnet": tailnet,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateResponse,
        )

    async def retrieve(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRetrieveResponse:
        """
        Retrieve an integration and its configuration.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationRetrieveResponse: Retrieve an integration

        Example:
            ```python
            integration = await client.integrations.retrieve(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            path_template("/v1/integrations/{integrationId}", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationRetrieveResponse,
        )

    @overload
    async def update(
        self,
        integration_id: str,
        *,
        settings: integration_update_params.VariantSettings,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @overload
    async def update(
        self,
        integration_id: str,
        *,
        aws: integration_update_params.Variant2Aws,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @overload
    async def update(
        self,
        integration_id: str,
        *,
        postgres: integration_update_params.Variant3Postgres,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @overload
    async def update(
        self,
        integration_id: str,
        *,
        atlassian_service_account: Optional[integration_update_params.Variant4AtlassianServiceAccount],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse: ...

    @required_args(["settings"], ["aws"], ["postgres"], ["atlassian_service_account"])
    async def update(
        self,
        integration_id: str,
        *,
        settings: integration_update_params.VariantSettings | Omit = omit,
        aws: integration_update_params.Variant2Aws | Omit = omit,
        postgres: integration_update_params.Variant3Postgres | Omit = omit,
        atlassian_service_account: Optional[integration_update_params.Variant4AtlassianServiceAccount] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse:
        """
        Update integration settings such as the default repository, Slack channel restrictions, automatic solving, or Sentry environments; replace AWS or PostgreSQL configuration; set or remove Atlassian service-account credentials.

        Args:
            integration_id: Path parameter.
            settings: Update integration settings, preserving unspecified settings.
            aws: Replace AWS environment and assumed-role configuration.
            postgres: Replace PostgreSQL connection configuration.
            atlassian_service_account: Set Atlassian service-account OAuth credentials for triggers, or null to remove them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationUpdateResponse: Update an integration

        Example:
            ```python
            integration = await client.integrations.update(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                settings={},
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._patch(
            path_template("/v1/integrations/{integrationId}", **{"integrationId": integration_id}),
            body=await async_maybe_transform(
                {
                    "settings": settings,
                    "aws": aws,
                    "postgres": postgres,
                    "atlassian_service_account": atlassian_service_account,
                },
                integration_update_params.IntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationUpdateResponse,
        )

    async def delete(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationDeleteResponse:
        """
        Uninstall an integration from its provider when supported, then delete it from Tembo.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationDeleteResponse: Delete an integration

        Example:
            ```python
            integration = await client.integrations.delete(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._delete(
            path_template("/v1/integrations/{integrationId}", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationDeleteResponse,
        )

    async def authorize(
        self,
        integration_id: str,
        *,
        return_url: str | Omit = omit,
        capability: Literal["confluenceTriggers"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationAuthorizeResponse:
        """
        Return the provider authorization URL for an integration.

        Args:
            integration_id: Path parameter.
            return_url: URL to return to after provider authorization. Must use HTTPS or localhost HTTP.
            capability: Request authorization for Confluence automation triggers instead of the default integration capability.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationAuthorizeResponse: Authorize an integration

        Example:
            ```python
            integration = await client.integrations.authorize(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            path_template("/v1/integrations/{integrationId}/authorize", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"return_url": return_url, "capability": capability},
                    integration_authorize_params.IntegrationAuthorizeParams,
                ),
            ),
            cast_to=IntegrationAuthorizeResponse,
        )

    async def test(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationTestResponse:
        """
        Test the saved provider connection.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationTestResponse: Test an integration

        Example:
            ```python
            integration = await client.integrations.test(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            path_template("/v1/integrations/{integrationId}/test", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationTestResponse,
        )

    async def sync(
        self,
        integration_id: str,
        *,
        mode: Literal["immediate", "queued"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationSyncResponse:
        """
        Queue or immediately perform an integration sync.

        Args:
            integration_id: Path parameter.
            mode: queued schedules a background integration sync; immediate performs the sync in this request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationSyncResponse: Sync an integration

        Example:
            ```python
            integration = await client.integrations.sync(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                mode="queued",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            path_template("/v1/integrations/{integrationId}/sync", **{"integrationId": integration_id}),
            body=await async_maybe_transform(
                {"mode": mode},
                integration_sync_params.IntegrationSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSyncResponse,
        )

    async def sync_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationSyncAllResponse:
        """
        Queue integration and pull-request sync jobs for integrations with enabled repositories.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationSyncAllResponse: Sync eligible integrations

        Example:
            ```python
            integration = await client.integrations.sync_all()
            ```
        """
        return await self._post(
            "/v1/integrations/sync",
            body=await async_maybe_transform(
                {},
                integration_sync_all_params.IntegrationSyncAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSyncAllResponse,
        )

    async def retrieve_sync_status(
        self,
        *,
        integration_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRetrieveSyncStatusResponse:
        """
        Count active sync jobs for an integration or eligible integrations.

        Args:
            integration_id: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationRetrieveSyncStatusResponse: Retrieve integration sync status

        Example:
            ```python
            integration = await client.integrations.retrieve_sync_status()
            ```
        """
        return await self._get(
            "/v1/integrations/sync/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id},
                    integration_retrieve_sync_status_params.IntegrationRetrieveSyncStatusParams,
                ),
            ),
            cast_to=IntegrationRetrieveSyncStatusResponse,
        )

    async def retrieve_rate_limit(
        self,
        integration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationRetrieveRateLimitResponse:
        """
        Retrieve the GitHub installation rate-limit state.

        Args:
            integration_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationRetrieveRateLimitResponse: Retrieve an integration rate limit

        Example:
            ```python
            integration = await client.integrations.retrieve_rate_limit(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            path_template("/v1/integrations/{integrationId}/rate-limit", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationRetrieveRateLimitResponse,
        )

    async def list_sentry_environments(
        self,
        integration_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListSentryEnvironmentsResponse:
        """
        List environments visible to a Sentry integration.

        Args:
            integration_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListSentryEnvironmentsResponse: List Sentry environments

        Example:
            ```python
            integration = await client.integrations.list_sentry_environments(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            path_template("/v1/integrations/{integrationId}/sentry-environments", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit},
                    integration_list_sentry_environments_params.IntegrationListSentryEnvironmentsParams,
                ),
            ),
            cast_to=IntegrationListSentryEnvironmentsResponse,
        )

    async def list_slack_channels(
        self,
        integration_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListSlackChannelsResponse:
        """
        List channels visible to a Slack integration.

        Args:
            integration_id: Path parameter.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search Slack channel names.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListSlackChannelsResponse: List Slack channels

        Example:
            ```python
            integration = await client.integrations.list_slack_channels(
                integration_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=50,
            )
            ```
        """
        if integration_id is None or (isinstance(integration_id, str) and not integration_id):
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            path_template("/v1/integrations/{integrationId}/slack-channels", **{"integrationId": integration_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor, "limit": limit, "search": search},
                    integration_list_slack_channels_params.IntegrationListSlackChannelsParams,
                ),
            ),
            cast_to=IntegrationListSlackChannelsResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.list = to_raw_response_wrapper(
            integrations.list,
        )
        self.create = to_raw_response_wrapper(
            integrations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            integrations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            integrations.update,
        )
        self.delete = to_raw_response_wrapper(
            integrations.delete,
        )
        self.authorize = to_raw_response_wrapper(
            integrations.authorize,
        )
        self.test = to_raw_response_wrapper(
            integrations.test,
        )
        self.sync = to_raw_response_wrapper(
            integrations.sync,
        )
        self.sync_all = to_raw_response_wrapper(
            integrations.sync_all,
        )
        self.retrieve_sync_status = to_raw_response_wrapper(
            integrations.retrieve_sync_status,
        )
        self.retrieve_rate_limit = to_raw_response_wrapper(
            integrations.retrieve_rate_limit,
        )
        self.list_sentry_environments = to_raw_response_wrapper(
            integrations.list_sentry_environments,
        )
        self.list_slack_channels = to_raw_response_wrapper(
            integrations.list_slack_channels,
        )

    @cached_property
    def providers(self) -> ProvidersResourceWithRawResponse:
        return ProvidersResourceWithRawResponse(self._integrations.providers)

    @cached_property
    def triggers(self) -> TriggersResourceWithRawResponse:
        return TriggersResourceWithRawResponse(self._integrations.triggers)


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.list = async_to_raw_response_wrapper(
            integrations.list,
        )
        self.create = async_to_raw_response_wrapper(
            integrations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            integrations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            integrations.update,
        )
        self.delete = async_to_raw_response_wrapper(
            integrations.delete,
        )
        self.authorize = async_to_raw_response_wrapper(
            integrations.authorize,
        )
        self.test = async_to_raw_response_wrapper(
            integrations.test,
        )
        self.sync = async_to_raw_response_wrapper(
            integrations.sync,
        )
        self.sync_all = async_to_raw_response_wrapper(
            integrations.sync_all,
        )
        self.retrieve_sync_status = async_to_raw_response_wrapper(
            integrations.retrieve_sync_status,
        )
        self.retrieve_rate_limit = async_to_raw_response_wrapper(
            integrations.retrieve_rate_limit,
        )
        self.list_sentry_environments = async_to_raw_response_wrapper(
            integrations.list_sentry_environments,
        )
        self.list_slack_channels = async_to_raw_response_wrapper(
            integrations.list_slack_channels,
        )

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithRawResponse:
        return AsyncProvidersResourceWithRawResponse(self._integrations.providers)

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithRawResponse:
        return AsyncTriggersResourceWithRawResponse(self._integrations.triggers)


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.list = to_streamed_response_wrapper(
            integrations.list,
        )
        self.create = to_streamed_response_wrapper(
            integrations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            integrations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            integrations.update,
        )
        self.delete = to_streamed_response_wrapper(
            integrations.delete,
        )
        self.authorize = to_streamed_response_wrapper(
            integrations.authorize,
        )
        self.test = to_streamed_response_wrapper(
            integrations.test,
        )
        self.sync = to_streamed_response_wrapper(
            integrations.sync,
        )
        self.sync_all = to_streamed_response_wrapper(
            integrations.sync_all,
        )
        self.retrieve_sync_status = to_streamed_response_wrapper(
            integrations.retrieve_sync_status,
        )
        self.retrieve_rate_limit = to_streamed_response_wrapper(
            integrations.retrieve_rate_limit,
        )
        self.list_sentry_environments = to_streamed_response_wrapper(
            integrations.list_sentry_environments,
        )
        self.list_slack_channels = to_streamed_response_wrapper(
            integrations.list_slack_channels,
        )

    @cached_property
    def providers(self) -> ProvidersResourceWithStreamingResponse:
        return ProvidersResourceWithStreamingResponse(self._integrations.providers)

    @cached_property
    def triggers(self) -> TriggersResourceWithStreamingResponse:
        return TriggersResourceWithStreamingResponse(self._integrations.triggers)


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.list = async_to_streamed_response_wrapper(
            integrations.list,
        )
        self.create = async_to_streamed_response_wrapper(
            integrations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            integrations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            integrations.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            integrations.delete,
        )
        self.authorize = async_to_streamed_response_wrapper(
            integrations.authorize,
        )
        self.test = async_to_streamed_response_wrapper(
            integrations.test,
        )
        self.sync = async_to_streamed_response_wrapper(
            integrations.sync,
        )
        self.sync_all = async_to_streamed_response_wrapper(
            integrations.sync_all,
        )
        self.retrieve_sync_status = async_to_streamed_response_wrapper(
            integrations.retrieve_sync_status,
        )
        self.retrieve_rate_limit = async_to_streamed_response_wrapper(
            integrations.retrieve_rate_limit,
        )
        self.list_sentry_environments = async_to_streamed_response_wrapper(
            integrations.list_sentry_environments,
        )
        self.list_slack_channels = async_to_streamed_response_wrapper(
            integrations.list_slack_channels,
        )

    @cached_property
    def providers(self) -> AsyncProvidersResourceWithStreamingResponse:
        return AsyncProvidersResourceWithStreamingResponse(self._integrations.providers)

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithStreamingResponse:
        return AsyncTriggersResourceWithStreamingResponse(self._integrations.triggers)
