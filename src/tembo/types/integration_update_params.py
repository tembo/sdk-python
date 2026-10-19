# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = [
    "IntegrationUpdateParams",
    "Variant",
    "VariantSettings",
    "Variant2",
    "Variant2Aws",
    "Variant3",
    "Variant3Postgres",
    "Variant4",
    "Variant4AtlassianServiceAccount",
]


class Variant4AtlassianServiceAccount(TypedDict, total=False):
    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]

    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]


class Variant4(TypedDict, total=False):
    atlassian_service_account: Required[
        Annotated[Optional[Variant4AtlassianServiceAccount], PropertyInfo(alias="atlassianServiceAccount")]
    ]
    """Set Atlassian service-account OAuth credentials for triggers, or null to remove them."""


class Variant3Postgres(TypedDict, total=False):
    ca_certificate: Annotated[str, PropertyInfo(alias="caCertificate")]
    """Optional CA certificate for the PostgreSQL TLS connection."""

    connection_string: Required[Annotated[str, PropertyInfo(alias="connectionString")]]
    """PostgreSQL connection URI, including credentials. Stored as secret configuration."""

    instance_name: Required[Annotated[str, PropertyInfo(alias="instanceName")]]
    """Display name for the PostgreSQL instance."""


class Variant3(TypedDict, total=False):
    postgres: Required[Variant3Postgres]
    """Replace PostgreSQL connection configuration."""


class Variant2Aws(TypedDict, total=False):
    environment: Required[str]
    """Display label for the AWS environment."""

    role_arn: Required[Annotated[str, PropertyInfo(alias="roleArn")]]
    """AWS IAM role ARN to assume for account access."""


class Variant2(TypedDict, total=False):
    aws: Required[Variant2Aws]
    """Replace AWS environment and assumed-role configuration."""


class VariantSettings(TypedDict, total=False):
    default_repository_id: Annotated[Optional[str], PropertyInfo(alias="defaultRepositoryId")]

    disallowed_slack_channel_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="disallowedSlackChannelIds")]

    instant_solve: Annotated[bool, PropertyInfo(alias="instantSolve")]

    sentry_environments: Annotated[SequenceNotStr[str], PropertyInfo(alias="sentryEnvironments")]


class Variant(TypedDict, total=False):
    settings: Required[VariantSettings]
    """Update integration settings, preserving unspecified settings."""


IntegrationUpdateParams: TypeAlias = Union[Variant, Variant2, Variant3, Variant4]
