# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Optional, Union
from typing_extensions import Literal, overload
from .._types import SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform, required_args
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.mcp_connection_list_response import McpConnectionListResponse
from ..types import mcp_connection_list_params, mcp_connection_create_params, mcp_connection_update_params
from ..types.mcp_connection_create_response import McpConnectionCreateResponse
from ..types.mcp_connection_retrieve_response import McpConnectionRetrieveResponse
from ..types.mcp_connection_update_response import McpConnectionUpdateResponse
from ..types.mcp_connection_delete_response import McpConnectionDeleteResponse
from ..types.mcp_connection_authorize_response import McpConnectionAuthorizeResponse
from ..types.mcp_connection_test_response import McpConnectionTestResponse

__all__ = ["McpConnectionsResource", "AsyncMcpConnectionsResource"]


class McpConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpConnectionsResourceWithRawResponse:
        return McpConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpConnectionsResourceWithStreamingResponse:
        return McpConnectionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        connected: bool | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionListResponse:
        """
        List MCP connections for the current organization with cursor pagination and optional search by name or URL. Command arguments, headers, and environment configuration are omitted.

        Args:
            connected: Filter by whether the MCP connection has completed connection or authorization.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search MCP connection names or server URLs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionListResponse: List MCP connections

        Example:
            ```python
            mcp_connection = client.mcp_connections.list(
                limit=50,
            )
            ```
        """
        return self._get(
            "/v1/mcp-connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"connected": connected, "cursor": cursor, "limit": limit, "search": search},
                    mcp_connection_list_params.McpConnectionListParams,
                ),
            ),
            cast_to=McpConnectionListResponse,
        )

    @overload
    def create(
        self,
        *,
        name: str,
        args: SequenceNotStr[str] | Omit = omit,
        command: str,
        env: Dict[str, str] | Omit = omit,
        type: Literal["stdio"],
        visibility: Literal["shared", "personal"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionCreateResponse: ...

    @overload
    def create(
        self,
        *,
        name: str,
        server_url: str,
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        type: Literal["remote"] | Omit = omit,
        visibility: Literal["shared", "personal"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionCreateResponse: ...

    @required_args(["command", "name", "type"], ["name", "server_url"])
    def create(
        self,
        *,
        name: str,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        type: Union[Literal["stdio"], Literal["remote"]] | Omit = omit,
        visibility: Literal["shared", "personal"] | Omit = omit,
        server_url: str | Omit = omit,
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionCreateResponse:
        """
        Create a new stdio or Streamable HTTP MCP connection. Remote connections support OAuth, Client Credentials (M2M), or static headers and begin authorization when required; stdio commands are stored but never executed by this API.

        Args:
            name: Display name for the MCP connection.
            args: Command-line arguments for the stdio server. Stored here, not executed by this API.
            command: Executable for the stdio MCP server. This API stores the command but never executes it.
            env: Environment variables for the stdio command. Values are write-only.
            type: Use stdio for a command-based MCP server.
            visibility: shared makes the connection available to the organization; personal restricts it to its owner.
            server_url: HTTP or HTTPS MCP server endpoint. Changing it requires an explicit authType, clears old credentials, and requires authorization to reconnect.
            auth_type: Authentication method: OAuth user authorization (oauth), Client Credentials (M2M) using client_credentials, or static request headers (static_headers).
            client_id: OAuth client ID. Required for client_credentials or pre_registered OAuth.
            client_secret: Write-only OAuth client secret. Required for client_credentials; optional for pre_registered OAuth.
            headers: Request headers for static-header or automatic OAuth authentication. Values are write-only.
            oauth_registration: Register an OAuth client automatically or use pre-registered clientId and optional clientSecret.
            scope: OAuth scopes requested for client credentials or pre-registered OAuth.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionCreateResponse: Create an MCP connection

        Example:
            ```python
            mcp_connection = client.mcp_connections.create(
                name="x",
                args=[],
                command="x",
                type="stdio",
                visibility="shared",
            )
            ```
        """
        return self._post(
            "/v1/mcp-connections",
            body=maybe_transform(
                {
                    "name": name,
                    "args": args,
                    "command": command,
                    "env": env,
                    "type": type,
                    "visibility": visibility,
                    "server_url": server_url,
                    "auth_type": auth_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "headers": headers,
                    "oauth_registration": oauth_registration,
                    "scope": scope,
                },
                mcp_connection_create_params.McpConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionCreateResponse,
        )

    def retrieve(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionRetrieveResponse:
        """
        Retrieve MCP connection configuration and authentication details. Stored header values, environment values, OAuth tokens, and client secrets are never returned.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionRetrieveResponse: Retrieve an MCP connection

        Example:
            ```python
            mcp_connection = client.mcp_connections.retrieve(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return self._get(
            path_template("/v1/mcp-connections/{mcpConnectionId}", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionRetrieveResponse,
        )

    @overload
    def update(
        self,
        mcp_connection_id: str,
        *,
        name: str | Omit = omit,
        server_url: str | Omit = omit,
        type: Literal["remote"],
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Optional[Dict[str, Optional[str]]] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionUpdateResponse: ...

    @overload
    def update(
        self,
        mcp_connection_id: str,
        *,
        command: str | Omit = omit,
        name: str | Omit = omit,
        type: Literal["stdio"],
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        env: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionUpdateResponse: ...

    def update(
        self,
        mcp_connection_id: str,
        *,
        name: str | Omit = omit,
        server_url: str | Omit = omit,
        type: Union[Literal["remote"], Literal["stdio"]],
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Optional[Dict[str, Optional[str]]] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        command: str | Omit = omit,
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        env: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionUpdateResponse:
        """
        Update MCP configuration, including OAuth, Client Credentials (M2M), or static-header authentication. Supplied headers merge by key only for unchanged-server static_headers authentication; otherwise they are replaced. Environment values merge by key, null values remove individual keys, and a null environment clears all variables. Hidden credentials are preserved unless explicitly changed or authentication is replaced; changing a remote server URL clears credentials for the old server. Call authorize explicitly after changing the server or authentication to reconnect.

        Args:
            mcp_connection_id: Path parameter.
            name: Display name for the MCP connection.
            server_url: HTTP or HTTPS MCP server endpoint. Changing it requires an explicit authType, clears old credentials, and requires authorization to reconnect.
            type: Connection type must remain remote; transport type cannot be changed by update.
            auth_type: Authentication method: OAuth user authorization (oauth), Client Credentials (M2M) using client_credentials, or static request headers (static_headers).
            client_id: OAuth client ID when replacing authentication. Requires authType; required for client_credentials or pre_registered OAuth.
            client_secret: Write-only client secret when replacing authentication. Requires authType; required for client_credentials.
            headers: Requires authType. Merges by key only when keeping static_headers authentication and the same server URL; otherwise replaces stored headers. Null values remove keys; static_headers requires at least one header. Values are write-only.
            oauth_registration: Register an OAuth client automatically or use pre-registered clientId and optional clientSecret.
            scope: OAuth scopes when replacing authentication. Requires authType.
            command: Replace the stored stdio server executable. This API never executes it.
            args: Command-line arguments for the stdio server. Stored here, not executed by this API.
            env: Merge write-only environment variables by key. A null value removes a key; null for the entire env field clears all variables.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionUpdateResponse: Update an MCP connection

        Example:
            ```python
            mcp_connection = client.mcp_connections.update(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                type="remote",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return self._patch(
            path_template("/v1/mcp-connections/{mcpConnectionId}", **{"mcpConnectionId": mcp_connection_id}),
            body=maybe_transform(
                {
                    "name": name,
                    "server_url": server_url,
                    "type": type,
                    "auth_type": auth_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "headers": headers,
                    "oauth_registration": oauth_registration,
                    "scope": scope,
                    "command": command,
                    "args": args,
                    "env": env,
                },
                mcp_connection_update_params.McpConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionUpdateResponse,
        )

    def delete(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionDeleteResponse:
        """
        Delete an MCP connection in the current organization.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionDeleteResponse: Delete an MCP connection

        Example:
            ```python
            mcp_connection = client.mcp_connections.delete(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return self._delete(
            path_template("/v1/mcp-connections/{mcpConnectionId}", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionDeleteResponse,
        )

    def authorize(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionAuthorizeResponse:
        """
        Connect or authorize a remote Streamable HTTP MCP connection, returning an OAuth URL when user authorization is required. Stdio connections are rejected because this action cannot authorize them.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionAuthorizeResponse: Authorize an MCP connection

        Example:
            ```python
            mcp_connection = client.mcp_connections.authorize(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return self._post(
            path_template("/v1/mcp-connections/{mcpConnectionId}/authorize", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionAuthorizeResponse,
        )

    def test(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionTestResponse:
        """
        Test a remote MCP connection by connecting to its server. Stdio connections are rejected because the API does not execute arbitrary local commands.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionTestResponse: Test an MCP connection

        Example:
            ```python
            mcp_connection = client.mcp_connections.test(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return self._post(
            path_template("/v1/mcp-connections/{mcpConnectionId}/test", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionTestResponse,
        )


class AsyncMcpConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpConnectionsResourceWithRawResponse:
        return AsyncMcpConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpConnectionsResourceWithStreamingResponse:
        return AsyncMcpConnectionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        connected: bool | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionListResponse:
        """
        List MCP connections for the current organization with cursor pagination and optional search by name or URL. Command arguments, headers, and environment configuration are omitted.

        Args:
            connected: Filter by whether the MCP connection has completed connection or authorization.
            cursor: Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages.
            limit: Maximum number of items to return in one page. Use nextCursor from the response to fetch more items.
            search: Search MCP connection names or server URLs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionListResponse: List MCP connections

        Example:
            ```python
            mcp_connection = await client.mcp_connections.list(
                limit=50,
            )
            ```
        """
        return await self._get(
            "/v1/mcp-connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"connected": connected, "cursor": cursor, "limit": limit, "search": search},
                    mcp_connection_list_params.McpConnectionListParams,
                ),
            ),
            cast_to=McpConnectionListResponse,
        )

    @overload
    async def create(
        self,
        *,
        name: str,
        args: SequenceNotStr[str] | Omit = omit,
        command: str,
        env: Dict[str, str] | Omit = omit,
        type: Literal["stdio"],
        visibility: Literal["shared", "personal"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionCreateResponse: ...

    @overload
    async def create(
        self,
        *,
        name: str,
        server_url: str,
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        type: Literal["remote"] | Omit = omit,
        visibility: Literal["shared", "personal"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionCreateResponse: ...

    @required_args(["command", "name", "type"], ["name", "server_url"])
    async def create(
        self,
        *,
        name: str,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        type: Union[Literal["stdio"], Literal["remote"]] | Omit = omit,
        visibility: Literal["shared", "personal"] | Omit = omit,
        server_url: str | Omit = omit,
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionCreateResponse:
        """
        Create a new stdio or Streamable HTTP MCP connection. Remote connections support OAuth, Client Credentials (M2M), or static headers and begin authorization when required; stdio commands are stored but never executed by this API.

        Args:
            name: Display name for the MCP connection.
            args: Command-line arguments for the stdio server. Stored here, not executed by this API.
            command: Executable for the stdio MCP server. This API stores the command but never executes it.
            env: Environment variables for the stdio command. Values are write-only.
            type: Use stdio for a command-based MCP server.
            visibility: shared makes the connection available to the organization; personal restricts it to its owner.
            server_url: HTTP or HTTPS MCP server endpoint. Changing it requires an explicit authType, clears old credentials, and requires authorization to reconnect.
            auth_type: Authentication method: OAuth user authorization (oauth), Client Credentials (M2M) using client_credentials, or static request headers (static_headers).
            client_id: OAuth client ID. Required for client_credentials or pre_registered OAuth.
            client_secret: Write-only OAuth client secret. Required for client_credentials; optional for pre_registered OAuth.
            headers: Request headers for static-header or automatic OAuth authentication. Values are write-only.
            oauth_registration: Register an OAuth client automatically or use pre-registered clientId and optional clientSecret.
            scope: OAuth scopes requested for client credentials or pre-registered OAuth.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionCreateResponse: Create an MCP connection

        Example:
            ```python
            mcp_connection = await client.mcp_connections.create(
                name="x",
                args=[],
                command="x",
                type="stdio",
                visibility="shared",
            )
            ```
        """
        return await self._post(
            "/v1/mcp-connections",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "args": args,
                    "command": command,
                    "env": env,
                    "type": type,
                    "visibility": visibility,
                    "server_url": server_url,
                    "auth_type": auth_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "headers": headers,
                    "oauth_registration": oauth_registration,
                    "scope": scope,
                },
                mcp_connection_create_params.McpConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionCreateResponse,
        )

    async def retrieve(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionRetrieveResponse:
        """
        Retrieve MCP connection configuration and authentication details. Stored header values, environment values, OAuth tokens, and client secrets are never returned.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionRetrieveResponse: Retrieve an MCP connection

        Example:
            ```python
            mcp_connection = await client.mcp_connections.retrieve(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return await self._get(
            path_template("/v1/mcp-connections/{mcpConnectionId}", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionRetrieveResponse,
        )

    @overload
    async def update(
        self,
        mcp_connection_id: str,
        *,
        name: str | Omit = omit,
        server_url: str | Omit = omit,
        type: Literal["remote"],
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Optional[Dict[str, Optional[str]]] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionUpdateResponse: ...

    @overload
    async def update(
        self,
        mcp_connection_id: str,
        *,
        command: str | Omit = omit,
        name: str | Omit = omit,
        type: Literal["stdio"],
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        env: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionUpdateResponse: ...

    async def update(
        self,
        mcp_connection_id: str,
        *,
        name: str | Omit = omit,
        server_url: str | Omit = omit,
        type: Union[Literal["remote"], Literal["stdio"]],
        auth_type: Literal["oauth", "client_credentials", "static_headers"] | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        headers: Optional[Dict[str, Optional[str]]] | Omit = omit,
        oauth_registration: Literal["automatic", "pre_registered"] | Omit = omit,
        scope: str | Omit = omit,
        command: str | Omit = omit,
        args: Optional[SequenceNotStr[str]] | Omit = omit,
        env: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionUpdateResponse:
        """
        Update MCP configuration, including OAuth, Client Credentials (M2M), or static-header authentication. Supplied headers merge by key only for unchanged-server static_headers authentication; otherwise they are replaced. Environment values merge by key, null values remove individual keys, and a null environment clears all variables. Hidden credentials are preserved unless explicitly changed or authentication is replaced; changing a remote server URL clears credentials for the old server. Call authorize explicitly after changing the server or authentication to reconnect.

        Args:
            mcp_connection_id: Path parameter.
            name: Display name for the MCP connection.
            server_url: HTTP or HTTPS MCP server endpoint. Changing it requires an explicit authType, clears old credentials, and requires authorization to reconnect.
            type: Connection type must remain remote; transport type cannot be changed by update.
            auth_type: Authentication method: OAuth user authorization (oauth), Client Credentials (M2M) using client_credentials, or static request headers (static_headers).
            client_id: OAuth client ID when replacing authentication. Requires authType; required for client_credentials or pre_registered OAuth.
            client_secret: Write-only client secret when replacing authentication. Requires authType; required for client_credentials.
            headers: Requires authType. Merges by key only when keeping static_headers authentication and the same server URL; otherwise replaces stored headers. Null values remove keys; static_headers requires at least one header. Values are write-only.
            oauth_registration: Register an OAuth client automatically or use pre-registered clientId and optional clientSecret.
            scope: OAuth scopes when replacing authentication. Requires authType.
            command: Replace the stored stdio server executable. This API never executes it.
            args: Command-line arguments for the stdio server. Stored here, not executed by this API.
            env: Merge write-only environment variables by key. A null value removes a key; null for the entire env field clears all variables.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionUpdateResponse: Update an MCP connection

        Example:
            ```python
            mcp_connection = await client.mcp_connections.update(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                type="remote",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return await self._patch(
            path_template("/v1/mcp-connections/{mcpConnectionId}", **{"mcpConnectionId": mcp_connection_id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "server_url": server_url,
                    "type": type,
                    "auth_type": auth_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "headers": headers,
                    "oauth_registration": oauth_registration,
                    "scope": scope,
                    "command": command,
                    "args": args,
                    "env": env,
                },
                mcp_connection_update_params.McpConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionUpdateResponse,
        )

    async def delete(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionDeleteResponse:
        """
        Delete an MCP connection in the current organization.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionDeleteResponse: Delete an MCP connection

        Example:
            ```python
            mcp_connection = await client.mcp_connections.delete(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return await self._delete(
            path_template("/v1/mcp-connections/{mcpConnectionId}", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionDeleteResponse,
        )

    async def authorize(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionAuthorizeResponse:
        """
        Connect or authorize a remote Streamable HTTP MCP connection, returning an OAuth URL when user authorization is required. Stdio connections are rejected because this action cannot authorize them.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionAuthorizeResponse: Authorize an MCP connection

        Example:
            ```python
            mcp_connection = await client.mcp_connections.authorize(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return await self._post(
            path_template("/v1/mcp-connections/{mcpConnectionId}/authorize", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionAuthorizeResponse,
        )

    async def test(
        self,
        mcp_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectionTestResponse:
        """
        Test a remote MCP connection by connecting to its server. Stdio connections are rejected because the API does not execute arbitrary local commands.

        Args:
            mcp_connection_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpConnectionTestResponse: Test an MCP connection

        Example:
            ```python
            mcp_connection = await client.mcp_connections.test(
                mcp_connection_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if mcp_connection_id is None or (isinstance(mcp_connection_id, str) and not mcp_connection_id):
            raise ValueError(f"Expected a non-empty value for `mcp_connection_id` but received {mcp_connection_id!r}")
        return await self._post(
            path_template("/v1/mcp-connections/{mcpConnectionId}/test", **{"mcpConnectionId": mcp_connection_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpConnectionTestResponse,
        )


class McpConnectionsResourceWithRawResponse:
    def __init__(self, mcp_connections: McpConnectionsResource) -> None:
        self._mcp_connections = mcp_connections

        self.list = to_raw_response_wrapper(
            mcp_connections.list,
        )
        self.create = to_raw_response_wrapper(
            mcp_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mcp_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mcp_connections.update,
        )
        self.delete = to_raw_response_wrapper(
            mcp_connections.delete,
        )
        self.authorize = to_raw_response_wrapper(
            mcp_connections.authorize,
        )
        self.test = to_raw_response_wrapper(
            mcp_connections.test,
        )


class AsyncMcpConnectionsResourceWithRawResponse:
    def __init__(self, mcp_connections: AsyncMcpConnectionsResource) -> None:
        self._mcp_connections = mcp_connections

        self.list = async_to_raw_response_wrapper(
            mcp_connections.list,
        )
        self.create = async_to_raw_response_wrapper(
            mcp_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mcp_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mcp_connections.update,
        )
        self.delete = async_to_raw_response_wrapper(
            mcp_connections.delete,
        )
        self.authorize = async_to_raw_response_wrapper(
            mcp_connections.authorize,
        )
        self.test = async_to_raw_response_wrapper(
            mcp_connections.test,
        )


class McpConnectionsResourceWithStreamingResponse:
    def __init__(self, mcp_connections: McpConnectionsResource) -> None:
        self._mcp_connections = mcp_connections

        self.list = to_streamed_response_wrapper(
            mcp_connections.list,
        )
        self.create = to_streamed_response_wrapper(
            mcp_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mcp_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mcp_connections.update,
        )
        self.delete = to_streamed_response_wrapper(
            mcp_connections.delete,
        )
        self.authorize = to_streamed_response_wrapper(
            mcp_connections.authorize,
        )
        self.test = to_streamed_response_wrapper(
            mcp_connections.test,
        )


class AsyncMcpConnectionsResourceWithStreamingResponse:
    def __init__(self, mcp_connections: AsyncMcpConnectionsResource) -> None:
        self._mcp_connections = mcp_connections

        self.list = async_to_streamed_response_wrapper(
            mcp_connections.list,
        )
        self.create = async_to_streamed_response_wrapper(
            mcp_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mcp_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mcp_connections.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            mcp_connections.delete,
        )
        self.authorize = async_to_streamed_response_wrapper(
            mcp_connections.authorize,
        )
        self.test = async_to_streamed_response_wrapper(
            mcp_connections.test,
        )
