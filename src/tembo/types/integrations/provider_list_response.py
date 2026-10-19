# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProviderListResponse", "InstalledCounts", "Item"]


class Item(BaseModel):
    authorize_url: str = FieldInfo(alias="authorizeUrl")

    category: str

    coming_soon: bool = FieldInfo(alias="comingSoon")

    description: str

    display_name: str = FieldInfo(alias="displayName")

    installed: bool

    integration_type: Literal[
        "github",
        "gitlab",
        "bitbucket",
        "atlassian",
        "linear",
        "slack",
        "sentry",
        "aws",
        "agent",
        "notion",
        "postgres",
        "bigquery",
        "azure",
        "ms-teams",
        "snyk",
        "hubspot",
        "openconnect",
        "tailscale",
    ] = FieldInfo(alias="integrationType")

    is_o_auth: bool = FieldInfo(alias="isOAuth")

    name: str

    oidc_issuer_host: Optional[str] = FieldInfo(alias="oidcIssuerHost", default=None)

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)

    template_url: Optional[str] = FieldInfo(alias="templateUrl", default=None)


class InstalledCounts(BaseModel):
    github: Optional[int] = None

    gitlab: Optional[int] = None

    bitbucket: Optional[int] = None

    atlassian: Optional[int] = None

    linear: Optional[int] = None

    slack: Optional[int] = None

    sentry: Optional[int] = None

    aws: Optional[int] = None

    agent: Optional[int] = None

    notion: Optional[int] = None

    postgres: Optional[int] = None

    bigquery: Optional[int] = None

    azure: Optional[int] = None

    ms_teams: Optional[int] = FieldInfo(alias="ms-teams", default=None)

    snyk: Optional[int] = None

    hubspot: Optional[int] = None

    openconnect: Optional[int] = None

    tailscale: Optional[int] = None


class ProviderListResponse(BaseModel):
    installed_counts: InstalledCounts = FieldInfo(alias="installedCounts")

    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
