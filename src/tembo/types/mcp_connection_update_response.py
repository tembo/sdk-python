# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpConnectionUpdateResponse"]


class McpConnectionUpdateResponse(BaseModel):
    connected_at: Optional[datetime] = FieldInfo(alias="connectedAt", default=None)

    id: str

    name: str

    server_url: Optional[str] = FieldInfo(alias="serverUrl", default=None)

    type: Literal["remote", "stdio"]

    visibility: Literal["shared", "personal"]
    """shared makes the connection available to the organization; personal restricts it to its owner."""

    args: Optional[List[str]] = None
    """Command-line arguments for the stdio server. Stored here, not executed by this API."""

    auth_type: Optional[Literal["oauth", "client_credentials", "static_headers"]] = FieldInfo(
        alias="authType", default=None
    )
    """Authentication method: OAuth user authorization (oauth), Client Credentials (M2M) using client_credentials, or static request headers (static_headers)."""

    command: Optional[str] = None

    created_at: datetime = FieldInfo(alias="createdAt")

    env_keys: List[str] = FieldInfo(alias="envKeys")

    header_keys: List[str] = FieldInfo(alias="headerKeys")

    updated_at: datetime = FieldInfo(alias="updatedAt")
