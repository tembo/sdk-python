# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["McpConnectionCreateParams", "Variant", "Variant2"]


class Variant2(TypedDict, total=False):
    name: Required[str]
    """Display name for the MCP connection."""

    server_url: Required[Annotated[str, PropertyInfo(alias="serverUrl")]]
    """HTTP or HTTPS MCP server endpoint. Changing it requires an explicit authType, clears old credentials, and requires authorization to reconnect."""

    auth_type: Annotated[Literal["oauth", "client_credentials", "static_headers"], PropertyInfo(alias="authType")]
    """Authentication method: OAuth user authorization (oauth), Client Credentials (M2M) using client_credentials, or static request headers (static_headers)."""

    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """OAuth client ID. Required for client_credentials or pre_registered OAuth."""

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]
    """Write-only OAuth client secret. Required for client_credentials; optional for pre_registered OAuth."""

    headers: Dict[str, str]
    """Request headers for static-header or automatic OAuth authentication. Values are write-only."""

    oauth_registration: Annotated[Literal["automatic", "pre_registered"], PropertyInfo(alias="oauthRegistration")]
    """Register an OAuth client automatically or use pre-registered clientId and optional clientSecret."""

    scope: str
    """OAuth scopes requested for client credentials or pre-registered OAuth."""

    type: Literal["remote"]
    """Use remote for a Streamable HTTP MCP server."""

    visibility: Literal["shared", "personal"]
    """shared makes the connection available to the organization; personal restricts it to its owner."""


class Variant(TypedDict, total=False):
    name: Required[str]
    """Display name for the MCP connection."""

    args: SequenceNotStr[str]
    """Command-line arguments for the stdio server. Stored here, not executed by this API."""

    command: Required[str]
    """Executable for the stdio MCP server. This API stores the command but never executes it."""

    env: Dict[str, str]
    """Environment variables for the stdio command. Values are write-only."""

    type: Required[Literal["stdio"]]
    """Use stdio for a command-based MCP server."""

    visibility: Literal["shared", "personal"]
    """shared makes the connection available to the organization; personal restricts it to its owner."""


McpConnectionCreateParams: TypeAlias = Union[Variant, Variant2]
