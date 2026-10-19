# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["IntegrationCreateParams", "Variant", "Variant2", "Variant3", "Variant4", "Variant5", "Variant6", "Variant7"]


class Variant7(TypedDict, total=False):
    instance_name: Required[Annotated[str, PropertyInfo(alias="instanceName")]]
    """Display name for the Tailscale connection."""

    oauth_client_id: Required[Annotated[str, PropertyInfo(alias="oauthClientId")]]
    """Tailscale OAuth client ID authorized to create tagged devices."""

    oauth_client_secret: Required[Annotated[str, PropertyInfo(alias="oauthClientSecret")]]
    """Tailscale OAuth client secret."""

    tags: Required[SequenceNotStr[str]]
    """Tags to assign to connected devices, such as tag:tembo. Must be authorized for the OAuth client."""

    tailnet: str
    """Tailnet name. The default - uses the OAuth client tailnet."""

    type: Required[Literal["tailscale"]]
    """Create a Tailscale private-network integration."""


class Variant6(TypedDict, total=False):
    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]
    """Snyk service-account client ID."""

    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]
    """Snyk service-account client secret."""

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """Snyk organization ID, not a Tembo organization ID. Discover choices with discoverSnykOrganizations."""

    organization_name: Annotated[str, PropertyInfo(alias="organizationName")]
    """Optional display name for the Snyk organization."""

    type: Required[Literal["snyk"]]
    """Create a Snyk integration."""


class Variant5(TypedDict, total=False):
    ca_certificate: Annotated[str, PropertyInfo(alias="caCertificate")]
    """Optional CA certificate for the PostgreSQL TLS connection."""

    connection_string: Required[Annotated[str, PropertyInfo(alias="connectionString")]]
    """PostgreSQL connection URI, including credentials. Stored as secret configuration."""

    instance_name: Required[Annotated[str, PropertyInfo(alias="instanceName")]]
    """Display name for the PostgreSQL instance."""

    type: Required[Literal["postgres"]]
    """Create a PostgreSQL integration."""


class Variant4(TypedDict, total=False):
    gateway: Required[str]
    """VPN gateway hostname or URL for OpenConnect."""

    instance_name: Required[Annotated[str, PropertyInfo(alias="instanceName")]]
    """Display name for the VPN connection."""

    password: Required[str]
    """VPN login password."""

    protocol: Required[Literal["fortinet", "anyconnect", "gp", "nc"]]
    """OpenConnect VPN protocol supported by the gateway."""

    type: Required[Literal["openconnect"]]
    """Create an OpenConnect VPN integration."""

    username: Required[str]
    """VPN login username."""


class Variant3(TypedDict, total=False):
    access_token: Required[Annotated[str, PropertyInfo(alias="accessToken")]]
    """GitLab access token used to connect the integration."""

    type: Required[Literal["gitlab"]]
    """Create a GitLab integration."""


class Variant2(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """Google Cloud project ID for BigQuery."""

    service_account_json: Required[Annotated[str, PropertyInfo(alias="serviceAccountJson")]]
    """Google Cloud service-account JSON credentials for BigQuery."""

    type: Required[Literal["bigquery"]]
    """Create a BigQuery integration."""


class Variant(TypedDict, total=False):
    environment: Required[str]
    """Display label for the AWS environment."""

    role_arn: Required[Annotated[str, PropertyInfo(alias="roleArn")]]
    """AWS IAM role ARN to assume for account access."""

    type: Required[Literal["aws"]]
    """Create an AWS account integration."""


IntegrationCreateParams: TypeAlias = Union[Variant, Variant2, Variant3, Variant4, Variant5, Variant6, Variant7]
