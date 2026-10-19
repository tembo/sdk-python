# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SettingValidateCredentialsParams", "Variant", "Variant2", "Variant3", "Variant4", "Variant5", "Variant6"]


class Variant6(TypedDict, total=False):
    provider: Required[Literal["gcp-vertex-ai"]]
    """Validate Google Cloud Vertex AI credentials without saving them."""

    service_account_json: Required[Annotated[str, PropertyInfo(alias="serviceAccountJson")]]
    """The GCP service account JSON."""

    project: Required[str]
    """The GCP project ID."""

    location: Required[str]
    """The Vertex AI location."""


class Variant5(TypedDict, total=False):
    provider: Required[Literal["aws-bedrock"]]
    """Validate AWS Bedrock credentials without saving them."""

    access_key_id: Required[Annotated[str, PropertyInfo(alias="accessKeyId")]]
    """The AWS access key ID."""

    secret_access_key: Required[Annotated[str, PropertyInfo(alias="secretAccessKey")]]
    """The AWS secret access key."""

    region: Required[str]
    """The AWS region."""


class Variant4(TypedDict, total=False):
    provider: Required[Literal["openrouter"]]
    """Validate OpenRouter API credentials without saving them."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """The OpenRouter API key."""


class Variant3(TypedDict, total=False):
    provider: Required[Literal["xai"]]
    """Validate xAI API credentials without saving them."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """The xAI API key."""


class Variant2(TypedDict, total=False):
    provider: Required[Literal["openai"]]
    """Validate OpenAI API credentials without saving them."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """The OpenAI API key."""


class Variant(TypedDict, total=False):
    provider: Required[Literal["anthropic"]]
    """Validate Anthropic API credentials without saving them."""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
    """The Anthropic API key."""


SettingValidateCredentialsParams: TypeAlias = Union[Variant, Variant2, Variant3, Variant4, Variant5, Variant6]
