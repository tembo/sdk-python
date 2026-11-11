# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List
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
from ...types.organizations.role_list_response import RoleListResponse
from ...types.organizations.role_create_response import RoleCreateResponse
from ...types.organizations import role_create_params, role_update_params, role_delete_params
from ...types.organizations.role_retrieve_response import RoleRetrieveResponse
from ...types.organizations.role_update_response import RoleUpdateResponse
from ...types.organizations.role_delete_response import RoleDeleteResponse

__all__ = ["RolesResource", "AsyncRolesResource"]


class RolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesResourceWithRawResponse:
        return RolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesResourceWithStreamingResponse:
        return RolesResourceWithStreamingResponse(self)

    def list(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """
        List organization roles

        Args:
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleListResponse: List organization roles

        Example:
            ```python
            role = client.organizations.roles.list(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/v1/organizations/{organizationId}/roles", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleListResponse,
        )

    def create(
        self,
        organization_id: str,
        *,
        name: str,
        description: str | Omit = omit,
        permissions: List[
            Literal[
                "organization:read",
                "organization:write",
                "organization:member:read",
                "organization:member:write",
                "organization:invitation:read",
                "organization:invitation:write",
                "organization:role:read",
                "organization:role:write",
                "organization:secret:read",
                "organization:secret:write",
                "organization:setting:read",
                "organization:setting:write",
                "organization:configuration:read",
                "organization:configuration:write",
                "organization:subscription:read",
                "organization:subscription:write",
                "organization:onboarding:read",
                "organization:onboarding:write",
                "organization:logo:read",
                "organization:logo:write",
                "organization:slack_connect:read",
                "organization:slack_connect:write",
                "billing:read",
                "billing:write",
                "billing:trial:read",
                "billing:trial:write",
                "billing:usage:read",
                "billing:usage:write",
                "billing:payment:read",
                "billing:payment:write",
                "billing:payment_method:read",
                "billing:payment_method:write",
                "billing:checkout:read",
                "billing:checkout:write",
                "billing:subscription_checkout:read",
                "billing:subscription_checkout:write",
                "billing:portal:read",
                "billing:portal:write",
                "billing:on_demand:read",
                "billing:on_demand:write",
                "billing:credit:read",
                "billing:credit:write",
                "billing:custom_price:read",
                "billing:custom_price:write",
                "billing:custom_plan:read",
                "billing:custom_plan:write",
                "billing:overage_report:read",
                "billing:overage_report:write",
                "api_key:read",
                "api_key:write",
                "user:read",
                "user:write",
                "user:setting:read",
                "user:setting:write",
                "user:environment_variable:read",
                "user:environment_variable:write",
                "user:subscription:read",
                "user:subscription:write",
                "user:connected_account:read",
                "user:connected_account:write",
                "user:organization:read",
                "user:organization:write",
                "user:profile_picture:read",
                "user:profile_picture:write",
                "user:deletion:read",
                "user:deletion:write",
                "agent:read",
                "agent:write",
                "agent:schedule:read",
                "agent:schedule:write",
                "agent:trigger:read",
                "agent:trigger:write",
                "agent:run:read",
                "agent:run:write",
                "agent:instruction_revision:read",
                "agent:instruction_revision:write",
                "agent:template:read",
                "agent:template:write",
                "session:read",
                "session:write",
                "session:message:read",
                "session:message:write",
                "session:artifact:read",
                "session:artifact:write",
                "session:source:read",
                "session:source:write",
                "session:command:read",
                "session:command:write",
                "session:input:read",
                "session:input:write",
                "session:queue:read",
                "session:queue:write",
                "session:event:read",
                "session:event:write",
                "session:file:read",
                "session:file:write",
                "session:diff:read",
                "session:diff:write",
                "session:workspace:read",
                "session:workspace:write",
                "session:workspace_file:read",
                "session:workspace_file:write",
                "session:workspace_diff:read",
                "session:workspace_diff:write",
                "session:workspace_preview:read",
                "session:workspace_preview:write",
                "pull_request:read",
                "pull_request:write",
                "pull_request:merge:read",
                "pull_request:merge:write",
                "pull_request:attachment:read",
                "pull_request:attachment:write",
                "pull_request:session:read",
                "pull_request:session:write",
                "pull_request:message:read",
                "pull_request:message:write",
                "pull_request:comment:read",
                "pull_request:comment:write",
                "pull_request:review:read",
                "pull_request:review:write",
                "pull_request:reaction:read",
                "pull_request:reaction:write",
                "pull_request:commit:read",
                "pull_request:commit:write",
                "pull_request:check:read",
                "pull_request:check:write",
                "pull_request:file:read",
                "pull_request:file:write",
                "pull_request:reviewer:read",
                "pull_request:reviewer:write",
                "pull_request:label:read",
                "pull_request:label:write",
                "pull_request:thread:read",
                "pull_request:thread:write",
                "pull_request:tour:read",
                "pull_request:tour:write",
                "pull_request:branch_status:read",
                "pull_request:branch_status:write",
                "pull_request:stack:read",
                "pull_request:stack:write",
                "repository:read",
                "repository:write",
                "repository:branch:read",
                "repository:branch:write",
                "repository:file:read",
                "repository:file:write",
                "repository:pull_request:read",
                "repository:pull_request:write",
                "repository:user:read",
                "repository:user:write",
                "repository:label:read",
                "repository:label:write",
                "integration:read",
                "integration:write",
                "integration:trigger:read",
                "integration:trigger:write",
                "integration:provider:read",
                "integration:provider:write",
                "integration:configuration:read",
                "integration:configuration:write",
                "integration:snyk_organization:read",
                "integration:snyk_organization:write",
                "integration:sentry_environment:read",
                "integration:sentry_environment:write",
                "integration:slack_channel:read",
                "integration:slack_channel:write",
                "integration:rate_limit:read",
                "integration:rate_limit:write",
                "mcp_connection:read",
                "mcp_connection:write",
                "mcp_connection:shared:read",
                "mcp_connection:shared:write",
                "model:read",
                "model:write",
                "project:read",
                "project:write",
                "project:environment_variable:read",
                "project:environment_variable:write",
                "project:snapshot:read",
                "project:snapshot:write",
                "project:build:read",
                "project:build:write",
                "project:build_detail:read",
                "project:build_detail:write",
                "project:schedule:read",
                "project:schedule:write",
                "project:default:read",
                "project:default:write",
                "project:system_snapshot:read",
                "project:system_snapshot:write",
                "project:organization_snapshot:read",
                "project:organization_snapshot:write",
                "sandbox:read",
                "sandbox:write",
                "sandbox:metric:read",
                "sandbox:metric:write",
                "sandbox:event:read",
                "sandbox:event:write",
                "sandbox:size:read",
                "sandbox:size:write",
                "sandbox:virtual_machine:read",
                "sandbox:virtual_machine:write",
                "device:read",
                "device:write",
                "skill:read",
                "skill:write",
                "skill:marketplace:read",
                "skill:marketplace:write",
                "insight:read",
                "insight:write",
                "insight:member:read",
                "insight:member:write",
                "insight:repository:read",
                "insight:repository:write",
                "insight:usage:read",
                "insight:usage:write",
                "file:read",
                "file:write",
                "pin:read",
                "pin:write",
                "folder:read",
                "folder:write",
                "queue:job:read",
                "queue:job:write",
                "queue:host_manager_job:read",
                "queue:host_manager_job:write",
                "queue:worker:read",
                "queue:worker:write",
                "queue:scheduled_job:read",
                "queue:scheduled_job:write",
                "queue:triggered_job:read",
                "queue:triggered_job:write",
                "runtime:read",
                "runtime:write",
                "session:source_credential:read",
                "session:source_credential:write",
                "device:all:write",
                "insight:user:read",
            ]
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleCreateResponse:
        """
        Create a organization role

        Args:
            organization_id: Path parameter.
            name: Body parameter.
            description: Body parameter.
            permissions: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleCreateResponse: Create a organization role

        Example:
            ```python
            role = client.organizations.roles.create(
                organization_id="organizationId",
                name="x",
                description="",
                permissions=["organization:read"],
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            path_template("/v1/organizations/{organizationId}/roles", **{"organizationId": organization_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "permissions": permissions,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleCreateResponse,
        )

    def retrieve(
        self,
        role_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleRetrieveResponse:
        """
        Retrieve an organization role

        Args:
            role_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleRetrieveResponse: Retrieve an organization role

        Example:
            ```python
            role = client.organizations.roles.retrieve(
                organization_id="organizationId",
                role_id="roleId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if role_id is None or (isinstance(role_id, str) and not role_id):
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._get(
            path_template(
                "/v1/organizations/{organizationId}/roles/{roleId}",
                **{"organizationId": organization_id, "roleId": role_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleRetrieveResponse,
        )

    def update(
        self,
        role_id: str,
        *,
        organization_id: str,
        name: str | Omit = omit,
        description: str | Omit = omit,
        permissions: List[
            Literal[
                "organization:read",
                "organization:write",
                "organization:member:read",
                "organization:member:write",
                "organization:invitation:read",
                "organization:invitation:write",
                "organization:role:read",
                "organization:role:write",
                "organization:secret:read",
                "organization:secret:write",
                "organization:setting:read",
                "organization:setting:write",
                "organization:configuration:read",
                "organization:configuration:write",
                "organization:subscription:read",
                "organization:subscription:write",
                "organization:onboarding:read",
                "organization:onboarding:write",
                "organization:logo:read",
                "organization:logo:write",
                "organization:slack_connect:read",
                "organization:slack_connect:write",
                "billing:read",
                "billing:write",
                "billing:trial:read",
                "billing:trial:write",
                "billing:usage:read",
                "billing:usage:write",
                "billing:payment:read",
                "billing:payment:write",
                "billing:payment_method:read",
                "billing:payment_method:write",
                "billing:checkout:read",
                "billing:checkout:write",
                "billing:subscription_checkout:read",
                "billing:subscription_checkout:write",
                "billing:portal:read",
                "billing:portal:write",
                "billing:on_demand:read",
                "billing:on_demand:write",
                "billing:credit:read",
                "billing:credit:write",
                "billing:custom_price:read",
                "billing:custom_price:write",
                "billing:custom_plan:read",
                "billing:custom_plan:write",
                "billing:overage_report:read",
                "billing:overage_report:write",
                "api_key:read",
                "api_key:write",
                "user:read",
                "user:write",
                "user:setting:read",
                "user:setting:write",
                "user:environment_variable:read",
                "user:environment_variable:write",
                "user:subscription:read",
                "user:subscription:write",
                "user:connected_account:read",
                "user:connected_account:write",
                "user:organization:read",
                "user:organization:write",
                "user:profile_picture:read",
                "user:profile_picture:write",
                "user:deletion:read",
                "user:deletion:write",
                "agent:read",
                "agent:write",
                "agent:schedule:read",
                "agent:schedule:write",
                "agent:trigger:read",
                "agent:trigger:write",
                "agent:run:read",
                "agent:run:write",
                "agent:instruction_revision:read",
                "agent:instruction_revision:write",
                "agent:template:read",
                "agent:template:write",
                "session:read",
                "session:write",
                "session:message:read",
                "session:message:write",
                "session:artifact:read",
                "session:artifact:write",
                "session:source:read",
                "session:source:write",
                "session:command:read",
                "session:command:write",
                "session:input:read",
                "session:input:write",
                "session:queue:read",
                "session:queue:write",
                "session:event:read",
                "session:event:write",
                "session:file:read",
                "session:file:write",
                "session:diff:read",
                "session:diff:write",
                "session:workspace:read",
                "session:workspace:write",
                "session:workspace_file:read",
                "session:workspace_file:write",
                "session:workspace_diff:read",
                "session:workspace_diff:write",
                "session:workspace_preview:read",
                "session:workspace_preview:write",
                "pull_request:read",
                "pull_request:write",
                "pull_request:merge:read",
                "pull_request:merge:write",
                "pull_request:attachment:read",
                "pull_request:attachment:write",
                "pull_request:session:read",
                "pull_request:session:write",
                "pull_request:message:read",
                "pull_request:message:write",
                "pull_request:comment:read",
                "pull_request:comment:write",
                "pull_request:review:read",
                "pull_request:review:write",
                "pull_request:reaction:read",
                "pull_request:reaction:write",
                "pull_request:commit:read",
                "pull_request:commit:write",
                "pull_request:check:read",
                "pull_request:check:write",
                "pull_request:file:read",
                "pull_request:file:write",
                "pull_request:reviewer:read",
                "pull_request:reviewer:write",
                "pull_request:label:read",
                "pull_request:label:write",
                "pull_request:thread:read",
                "pull_request:thread:write",
                "pull_request:tour:read",
                "pull_request:tour:write",
                "pull_request:branch_status:read",
                "pull_request:branch_status:write",
                "pull_request:stack:read",
                "pull_request:stack:write",
                "repository:read",
                "repository:write",
                "repository:branch:read",
                "repository:branch:write",
                "repository:file:read",
                "repository:file:write",
                "repository:pull_request:read",
                "repository:pull_request:write",
                "repository:user:read",
                "repository:user:write",
                "repository:label:read",
                "repository:label:write",
                "integration:read",
                "integration:write",
                "integration:trigger:read",
                "integration:trigger:write",
                "integration:provider:read",
                "integration:provider:write",
                "integration:configuration:read",
                "integration:configuration:write",
                "integration:snyk_organization:read",
                "integration:snyk_organization:write",
                "integration:sentry_environment:read",
                "integration:sentry_environment:write",
                "integration:slack_channel:read",
                "integration:slack_channel:write",
                "integration:rate_limit:read",
                "integration:rate_limit:write",
                "mcp_connection:read",
                "mcp_connection:write",
                "mcp_connection:shared:read",
                "mcp_connection:shared:write",
                "model:read",
                "model:write",
                "project:read",
                "project:write",
                "project:environment_variable:read",
                "project:environment_variable:write",
                "project:snapshot:read",
                "project:snapshot:write",
                "project:build:read",
                "project:build:write",
                "project:build_detail:read",
                "project:build_detail:write",
                "project:schedule:read",
                "project:schedule:write",
                "project:default:read",
                "project:default:write",
                "project:system_snapshot:read",
                "project:system_snapshot:write",
                "project:organization_snapshot:read",
                "project:organization_snapshot:write",
                "sandbox:read",
                "sandbox:write",
                "sandbox:metric:read",
                "sandbox:metric:write",
                "sandbox:event:read",
                "sandbox:event:write",
                "sandbox:size:read",
                "sandbox:size:write",
                "sandbox:virtual_machine:read",
                "sandbox:virtual_machine:write",
                "device:read",
                "device:write",
                "skill:read",
                "skill:write",
                "skill:marketplace:read",
                "skill:marketplace:write",
                "insight:read",
                "insight:write",
                "insight:member:read",
                "insight:member:write",
                "insight:repository:read",
                "insight:repository:write",
                "insight:usage:read",
                "insight:usage:write",
                "file:read",
                "file:write",
                "pin:read",
                "pin:write",
                "folder:read",
                "folder:write",
                "queue:job:read",
                "queue:job:write",
                "queue:host_manager_job:read",
                "queue:host_manager_job:write",
                "queue:worker:read",
                "queue:worker:write",
                "queue:scheduled_job:read",
                "queue:scheduled_job:write",
                "queue:triggered_job:read",
                "queue:triggered_job:write",
                "runtime:read",
                "runtime:write",
                "session:source_credential:read",
                "session:source_credential:write",
                "device:all:write",
                "insight:user:read",
            ]
        ]
        | Omit = omit,
        is_default: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleUpdateResponse:
        """
        Update a organization role

        Args:
            role_id: Path parameter.
            organization_id: Path parameter.
            name: Body parameter.
            description: Body parameter.
            permissions: Body parameter.
            is_default: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleUpdateResponse: Update a organization role

        Example:
            ```python
            role = client.organizations.roles.update(
                organization_id="organizationId",
                role_id="roleId",
                description="",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if role_id is None or (isinstance(role_id, str) and not role_id):
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._patch(
            path_template(
                "/v1/organizations/{organizationId}/roles/{roleId}",
                **{"organizationId": organization_id, "roleId": role_id},
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "permissions": permissions,
                    "is_default": is_default,
                },
                role_update_params.RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleUpdateResponse,
        )

    def delete(
        self,
        role_id: str,
        *,
        organization_id: str,
        replacement_role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleDeleteResponse:
        """
        Archive a role with an explicit replacement

        Args:
            role_id: Path parameter.
            organization_id: Path parameter.
            replacement_role_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleDeleteResponse: Archive a role with an explicit replacement

        Example:
            ```python
            role = client.organizations.roles.delete(
                organization_id="organizationId",
                role_id="roleId",
                replacement_role_id="x",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if role_id is None or (isinstance(role_id, str) and not role_id):
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._delete(
            path_template(
                "/v1/organizations/{organizationId}/roles/{roleId}",
                **{"organizationId": organization_id, "roleId": role_id},
            ),
            body=maybe_transform(
                {"replacement_role_id": replacement_role_id},
                role_delete_params.RoleDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleDeleteResponse,
        )


class AsyncRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolesResourceWithRawResponse:
        return AsyncRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolesResourceWithStreamingResponse:
        return AsyncRolesResourceWithStreamingResponse(self)

    async def list(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleListResponse:
        """
        List organization roles

        Args:
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleListResponse: List organization roles

        Example:
            ```python
            role = await client.organizations.roles.list(
                organization_id="organizationId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/v1/organizations/{organizationId}/roles", **{"organizationId": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleListResponse,
        )

    async def create(
        self,
        organization_id: str,
        *,
        name: str,
        description: str | Omit = omit,
        permissions: List[
            Literal[
                "organization:read",
                "organization:write",
                "organization:member:read",
                "organization:member:write",
                "organization:invitation:read",
                "organization:invitation:write",
                "organization:role:read",
                "organization:role:write",
                "organization:secret:read",
                "organization:secret:write",
                "organization:setting:read",
                "organization:setting:write",
                "organization:configuration:read",
                "organization:configuration:write",
                "organization:subscription:read",
                "organization:subscription:write",
                "organization:onboarding:read",
                "organization:onboarding:write",
                "organization:logo:read",
                "organization:logo:write",
                "organization:slack_connect:read",
                "organization:slack_connect:write",
                "billing:read",
                "billing:write",
                "billing:trial:read",
                "billing:trial:write",
                "billing:usage:read",
                "billing:usage:write",
                "billing:payment:read",
                "billing:payment:write",
                "billing:payment_method:read",
                "billing:payment_method:write",
                "billing:checkout:read",
                "billing:checkout:write",
                "billing:subscription_checkout:read",
                "billing:subscription_checkout:write",
                "billing:portal:read",
                "billing:portal:write",
                "billing:on_demand:read",
                "billing:on_demand:write",
                "billing:credit:read",
                "billing:credit:write",
                "billing:custom_price:read",
                "billing:custom_price:write",
                "billing:custom_plan:read",
                "billing:custom_plan:write",
                "billing:overage_report:read",
                "billing:overage_report:write",
                "api_key:read",
                "api_key:write",
                "user:read",
                "user:write",
                "user:setting:read",
                "user:setting:write",
                "user:environment_variable:read",
                "user:environment_variable:write",
                "user:subscription:read",
                "user:subscription:write",
                "user:connected_account:read",
                "user:connected_account:write",
                "user:organization:read",
                "user:organization:write",
                "user:profile_picture:read",
                "user:profile_picture:write",
                "user:deletion:read",
                "user:deletion:write",
                "agent:read",
                "agent:write",
                "agent:schedule:read",
                "agent:schedule:write",
                "agent:trigger:read",
                "agent:trigger:write",
                "agent:run:read",
                "agent:run:write",
                "agent:instruction_revision:read",
                "agent:instruction_revision:write",
                "agent:template:read",
                "agent:template:write",
                "session:read",
                "session:write",
                "session:message:read",
                "session:message:write",
                "session:artifact:read",
                "session:artifact:write",
                "session:source:read",
                "session:source:write",
                "session:command:read",
                "session:command:write",
                "session:input:read",
                "session:input:write",
                "session:queue:read",
                "session:queue:write",
                "session:event:read",
                "session:event:write",
                "session:file:read",
                "session:file:write",
                "session:diff:read",
                "session:diff:write",
                "session:workspace:read",
                "session:workspace:write",
                "session:workspace_file:read",
                "session:workspace_file:write",
                "session:workspace_diff:read",
                "session:workspace_diff:write",
                "session:workspace_preview:read",
                "session:workspace_preview:write",
                "pull_request:read",
                "pull_request:write",
                "pull_request:merge:read",
                "pull_request:merge:write",
                "pull_request:attachment:read",
                "pull_request:attachment:write",
                "pull_request:session:read",
                "pull_request:session:write",
                "pull_request:message:read",
                "pull_request:message:write",
                "pull_request:comment:read",
                "pull_request:comment:write",
                "pull_request:review:read",
                "pull_request:review:write",
                "pull_request:reaction:read",
                "pull_request:reaction:write",
                "pull_request:commit:read",
                "pull_request:commit:write",
                "pull_request:check:read",
                "pull_request:check:write",
                "pull_request:file:read",
                "pull_request:file:write",
                "pull_request:reviewer:read",
                "pull_request:reviewer:write",
                "pull_request:label:read",
                "pull_request:label:write",
                "pull_request:thread:read",
                "pull_request:thread:write",
                "pull_request:tour:read",
                "pull_request:tour:write",
                "pull_request:branch_status:read",
                "pull_request:branch_status:write",
                "pull_request:stack:read",
                "pull_request:stack:write",
                "repository:read",
                "repository:write",
                "repository:branch:read",
                "repository:branch:write",
                "repository:file:read",
                "repository:file:write",
                "repository:pull_request:read",
                "repository:pull_request:write",
                "repository:user:read",
                "repository:user:write",
                "repository:label:read",
                "repository:label:write",
                "integration:read",
                "integration:write",
                "integration:trigger:read",
                "integration:trigger:write",
                "integration:provider:read",
                "integration:provider:write",
                "integration:configuration:read",
                "integration:configuration:write",
                "integration:snyk_organization:read",
                "integration:snyk_organization:write",
                "integration:sentry_environment:read",
                "integration:sentry_environment:write",
                "integration:slack_channel:read",
                "integration:slack_channel:write",
                "integration:rate_limit:read",
                "integration:rate_limit:write",
                "mcp_connection:read",
                "mcp_connection:write",
                "mcp_connection:shared:read",
                "mcp_connection:shared:write",
                "model:read",
                "model:write",
                "project:read",
                "project:write",
                "project:environment_variable:read",
                "project:environment_variable:write",
                "project:snapshot:read",
                "project:snapshot:write",
                "project:build:read",
                "project:build:write",
                "project:build_detail:read",
                "project:build_detail:write",
                "project:schedule:read",
                "project:schedule:write",
                "project:default:read",
                "project:default:write",
                "project:system_snapshot:read",
                "project:system_snapshot:write",
                "project:organization_snapshot:read",
                "project:organization_snapshot:write",
                "sandbox:read",
                "sandbox:write",
                "sandbox:metric:read",
                "sandbox:metric:write",
                "sandbox:event:read",
                "sandbox:event:write",
                "sandbox:size:read",
                "sandbox:size:write",
                "sandbox:virtual_machine:read",
                "sandbox:virtual_machine:write",
                "device:read",
                "device:write",
                "skill:read",
                "skill:write",
                "skill:marketplace:read",
                "skill:marketplace:write",
                "insight:read",
                "insight:write",
                "insight:member:read",
                "insight:member:write",
                "insight:repository:read",
                "insight:repository:write",
                "insight:usage:read",
                "insight:usage:write",
                "file:read",
                "file:write",
                "pin:read",
                "pin:write",
                "folder:read",
                "folder:write",
                "queue:job:read",
                "queue:job:write",
                "queue:host_manager_job:read",
                "queue:host_manager_job:write",
                "queue:worker:read",
                "queue:worker:write",
                "queue:scheduled_job:read",
                "queue:scheduled_job:write",
                "queue:triggered_job:read",
                "queue:triggered_job:write",
                "runtime:read",
                "runtime:write",
                "session:source_credential:read",
                "session:source_credential:write",
                "device:all:write",
                "insight:user:read",
            ]
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleCreateResponse:
        """
        Create a organization role

        Args:
            organization_id: Path parameter.
            name: Body parameter.
            description: Body parameter.
            permissions: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleCreateResponse: Create a organization role

        Example:
            ```python
            role = await client.organizations.roles.create(
                organization_id="organizationId",
                name="x",
                description="",
                permissions=["organization:read"],
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            path_template("/v1/organizations/{organizationId}/roles", **{"organizationId": organization_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "permissions": permissions,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleCreateResponse,
        )

    async def retrieve(
        self,
        role_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleRetrieveResponse:
        """
        Retrieve an organization role

        Args:
            role_id: Path parameter.
            organization_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleRetrieveResponse: Retrieve an organization role

        Example:
            ```python
            role = await client.organizations.roles.retrieve(
                organization_id="organizationId",
                role_id="roleId",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if role_id is None or (isinstance(role_id, str) and not role_id):
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._get(
            path_template(
                "/v1/organizations/{organizationId}/roles/{roleId}",
                **{"organizationId": organization_id, "roleId": role_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleRetrieveResponse,
        )

    async def update(
        self,
        role_id: str,
        *,
        organization_id: str,
        name: str | Omit = omit,
        description: str | Omit = omit,
        permissions: List[
            Literal[
                "organization:read",
                "organization:write",
                "organization:member:read",
                "organization:member:write",
                "organization:invitation:read",
                "organization:invitation:write",
                "organization:role:read",
                "organization:role:write",
                "organization:secret:read",
                "organization:secret:write",
                "organization:setting:read",
                "organization:setting:write",
                "organization:configuration:read",
                "organization:configuration:write",
                "organization:subscription:read",
                "organization:subscription:write",
                "organization:onboarding:read",
                "organization:onboarding:write",
                "organization:logo:read",
                "organization:logo:write",
                "organization:slack_connect:read",
                "organization:slack_connect:write",
                "billing:read",
                "billing:write",
                "billing:trial:read",
                "billing:trial:write",
                "billing:usage:read",
                "billing:usage:write",
                "billing:payment:read",
                "billing:payment:write",
                "billing:payment_method:read",
                "billing:payment_method:write",
                "billing:checkout:read",
                "billing:checkout:write",
                "billing:subscription_checkout:read",
                "billing:subscription_checkout:write",
                "billing:portal:read",
                "billing:portal:write",
                "billing:on_demand:read",
                "billing:on_demand:write",
                "billing:credit:read",
                "billing:credit:write",
                "billing:custom_price:read",
                "billing:custom_price:write",
                "billing:custom_plan:read",
                "billing:custom_plan:write",
                "billing:overage_report:read",
                "billing:overage_report:write",
                "api_key:read",
                "api_key:write",
                "user:read",
                "user:write",
                "user:setting:read",
                "user:setting:write",
                "user:environment_variable:read",
                "user:environment_variable:write",
                "user:subscription:read",
                "user:subscription:write",
                "user:connected_account:read",
                "user:connected_account:write",
                "user:organization:read",
                "user:organization:write",
                "user:profile_picture:read",
                "user:profile_picture:write",
                "user:deletion:read",
                "user:deletion:write",
                "agent:read",
                "agent:write",
                "agent:schedule:read",
                "agent:schedule:write",
                "agent:trigger:read",
                "agent:trigger:write",
                "agent:run:read",
                "agent:run:write",
                "agent:instruction_revision:read",
                "agent:instruction_revision:write",
                "agent:template:read",
                "agent:template:write",
                "session:read",
                "session:write",
                "session:message:read",
                "session:message:write",
                "session:artifact:read",
                "session:artifact:write",
                "session:source:read",
                "session:source:write",
                "session:command:read",
                "session:command:write",
                "session:input:read",
                "session:input:write",
                "session:queue:read",
                "session:queue:write",
                "session:event:read",
                "session:event:write",
                "session:file:read",
                "session:file:write",
                "session:diff:read",
                "session:diff:write",
                "session:workspace:read",
                "session:workspace:write",
                "session:workspace_file:read",
                "session:workspace_file:write",
                "session:workspace_diff:read",
                "session:workspace_diff:write",
                "session:workspace_preview:read",
                "session:workspace_preview:write",
                "pull_request:read",
                "pull_request:write",
                "pull_request:merge:read",
                "pull_request:merge:write",
                "pull_request:attachment:read",
                "pull_request:attachment:write",
                "pull_request:session:read",
                "pull_request:session:write",
                "pull_request:message:read",
                "pull_request:message:write",
                "pull_request:comment:read",
                "pull_request:comment:write",
                "pull_request:review:read",
                "pull_request:review:write",
                "pull_request:reaction:read",
                "pull_request:reaction:write",
                "pull_request:commit:read",
                "pull_request:commit:write",
                "pull_request:check:read",
                "pull_request:check:write",
                "pull_request:file:read",
                "pull_request:file:write",
                "pull_request:reviewer:read",
                "pull_request:reviewer:write",
                "pull_request:label:read",
                "pull_request:label:write",
                "pull_request:thread:read",
                "pull_request:thread:write",
                "pull_request:tour:read",
                "pull_request:tour:write",
                "pull_request:branch_status:read",
                "pull_request:branch_status:write",
                "pull_request:stack:read",
                "pull_request:stack:write",
                "repository:read",
                "repository:write",
                "repository:branch:read",
                "repository:branch:write",
                "repository:file:read",
                "repository:file:write",
                "repository:pull_request:read",
                "repository:pull_request:write",
                "repository:user:read",
                "repository:user:write",
                "repository:label:read",
                "repository:label:write",
                "integration:read",
                "integration:write",
                "integration:trigger:read",
                "integration:trigger:write",
                "integration:provider:read",
                "integration:provider:write",
                "integration:configuration:read",
                "integration:configuration:write",
                "integration:snyk_organization:read",
                "integration:snyk_organization:write",
                "integration:sentry_environment:read",
                "integration:sentry_environment:write",
                "integration:slack_channel:read",
                "integration:slack_channel:write",
                "integration:rate_limit:read",
                "integration:rate_limit:write",
                "mcp_connection:read",
                "mcp_connection:write",
                "mcp_connection:shared:read",
                "mcp_connection:shared:write",
                "model:read",
                "model:write",
                "project:read",
                "project:write",
                "project:environment_variable:read",
                "project:environment_variable:write",
                "project:snapshot:read",
                "project:snapshot:write",
                "project:build:read",
                "project:build:write",
                "project:build_detail:read",
                "project:build_detail:write",
                "project:schedule:read",
                "project:schedule:write",
                "project:default:read",
                "project:default:write",
                "project:system_snapshot:read",
                "project:system_snapshot:write",
                "project:organization_snapshot:read",
                "project:organization_snapshot:write",
                "sandbox:read",
                "sandbox:write",
                "sandbox:metric:read",
                "sandbox:metric:write",
                "sandbox:event:read",
                "sandbox:event:write",
                "sandbox:size:read",
                "sandbox:size:write",
                "sandbox:virtual_machine:read",
                "sandbox:virtual_machine:write",
                "device:read",
                "device:write",
                "skill:read",
                "skill:write",
                "skill:marketplace:read",
                "skill:marketplace:write",
                "insight:read",
                "insight:write",
                "insight:member:read",
                "insight:member:write",
                "insight:repository:read",
                "insight:repository:write",
                "insight:usage:read",
                "insight:usage:write",
                "file:read",
                "file:write",
                "pin:read",
                "pin:write",
                "folder:read",
                "folder:write",
                "queue:job:read",
                "queue:job:write",
                "queue:host_manager_job:read",
                "queue:host_manager_job:write",
                "queue:worker:read",
                "queue:worker:write",
                "queue:scheduled_job:read",
                "queue:scheduled_job:write",
                "queue:triggered_job:read",
                "queue:triggered_job:write",
                "runtime:read",
                "runtime:write",
                "session:source_credential:read",
                "session:source_credential:write",
                "device:all:write",
                "insight:user:read",
            ]
        ]
        | Omit = omit,
        is_default: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleUpdateResponse:
        """
        Update a organization role

        Args:
            role_id: Path parameter.
            organization_id: Path parameter.
            name: Body parameter.
            description: Body parameter.
            permissions: Body parameter.
            is_default: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleUpdateResponse: Update a organization role

        Example:
            ```python
            role = await client.organizations.roles.update(
                organization_id="organizationId",
                role_id="roleId",
                description="",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if role_id is None or (isinstance(role_id, str) and not role_id):
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._patch(
            path_template(
                "/v1/organizations/{organizationId}/roles/{roleId}",
                **{"organizationId": organization_id, "roleId": role_id},
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "permissions": permissions,
                    "is_default": is_default,
                },
                role_update_params.RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleUpdateResponse,
        )

    async def delete(
        self,
        role_id: str,
        *,
        organization_id: str,
        replacement_role_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleDeleteResponse:
        """
        Archive a role with an explicit replacement

        Args:
            role_id: Path parameter.
            organization_id: Path parameter.
            replacement_role_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RoleDeleteResponse: Archive a role with an explicit replacement

        Example:
            ```python
            role = await client.organizations.roles.delete(
                organization_id="organizationId",
                role_id="roleId",
                replacement_role_id="x",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if role_id is None or (isinstance(role_id, str) and not role_id):
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._delete(
            path_template(
                "/v1/organizations/{organizationId}/roles/{roleId}",
                **{"organizationId": organization_id, "roleId": role_id},
            ),
            body=await async_maybe_transform(
                {"replacement_role_id": replacement_role_id},
                role_delete_params.RoleDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleDeleteResponse,
        )


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.list = to_raw_response_wrapper(
            roles.list,
        )
        self.create = to_raw_response_wrapper(
            roles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            roles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            roles.update,
        )
        self.delete = to_raw_response_wrapper(
            roles.delete,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.create = async_to_raw_response_wrapper(
            roles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            roles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            roles.update,
        )
        self.delete = async_to_raw_response_wrapper(
            roles.delete,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.create = to_streamed_response_wrapper(
            roles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            roles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            roles.update,
        )
        self.delete = to_streamed_response_wrapper(
            roles.delete,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.create = async_to_streamed_response_wrapper(
            roles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            roles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            roles.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            roles.delete,
        )
