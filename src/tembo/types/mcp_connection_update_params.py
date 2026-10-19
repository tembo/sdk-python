# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["McpConnectionUpdateParams", "Variant", "Variant2"]


class Variant2(TypedDict, total=False):
    command: str
    """Replace the stored stdio server executable. This API never executes it."""

    name: str
    """Display name for the MCP connection."""

    type: Required[Literal["stdio"]]
    """Connection type must remain stdio; transport type cannot be changed by update."""

    args: Optional[SequenceNotStr[str]]
    """Command-line arguments for the stdio server. Stored here, not executed by this API."""

    env: Optional[Dict[str, Optional[str]]]
    """Merge write-only environment variables by key. A null value removes a key; null for the entire env field clears all variables."""


class Variant(TypedDict, total=False):
    name: str
    """Display name for the MCP connection."""

    server_url: Annotated[str, PropertyInfo(alias="serverUrl")]
    """HTTP or HTTPS MCP server endpoint. Changing it requires an explicit authType, clears old credentials, and requires authorization to reconnect."""

    type: Required[Literal["remote"]]
    """Connection type must remain remote; transport type cannot be changed by update."""

    auth_type: Annotated[Literal["oauth", "client_credentials", "static_headers"], PropertyInfo(alias="authType")]
    """Authentication method: OAuth user authorization (oauth), Client Credentials (M2M) using client_credentials, or static request headers (static_headers)."""

    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """OAuth client ID when replacing authentication. Requires authType; required for client_credentials or pre_registered OAuth."""

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]
    """Write-only client secret when replacing authentication. Requires authType; required for client_credentials."""

    headers: Optional[Dict[str, Optional[str]]]
    """Requires authType. Merges by key only when keeping static_headers authentication and the same server URL; otherwise replaces stored headers. Null values remove keys; static_headers requires at least one header. Values are write-only."""

    oauth_registration: Annotated[Literal["automatic", "pre_registered"], PropertyInfo(alias="oauthRegistration")]
    """Register an OAuth client automatically or use pre-registered clientId and optional clientSecret."""

    scope: str
    """OAuth scopes when replacing authentication. Requires authType."""


McpConnectionUpdateParams: TypeAlias = Union[Variant, Variant2]
