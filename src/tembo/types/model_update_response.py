# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ModelUpdateResponse",
    "InferenceProviderAccess",
    "InferenceProviderAccessTemboManagedInference",
    "InferenceProviderAccessTemboManagedInference2",
    "InferenceProviderAccessTemboManagedInference3",
    "InferenceProviderAccessByok",
    "InferenceProviderAccessByok2",
    "InferenceProviderAccessByok3",
    "InferenceProviderAccessAwsBedrock",
    "InferenceProviderAccessAwsBedrock2",
    "InferenceProviderAccessAwsBedrock3",
    "InferenceProviderAccessGcpVertexAI",
    "InferenceProviderAccessGcpVertexAI2",
    "InferenceProviderAccessGcpVertexAI3",
    "InferenceProviderAccessOpenRouter",
    "InferenceProviderAccessOpenRouter2",
    "InferenceProviderAccessOpenRouter3",
]


class InferenceProviderAccessOpenRouter3(BaseModel):
    available: Literal[False]

    unavailable_code: Literal[
        "plan_required",
        "missing_credentials",
        "unsupported_provider",
        "chatgpt_not_connected",
        "supergrok_not_connected",
        "claude_subscription_not_connected",
    ] = FieldInfo(alias="unavailableCode")

    unavailable_reason: str = FieldInfo(alias="unavailableReason")


class InferenceProviderAccessOpenRouter2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


InferenceProviderAccessOpenRouter: TypeAlias = Union[
    InferenceProviderAccessOpenRouter2, InferenceProviderAccessOpenRouter3
]


class InferenceProviderAccessGcpVertexAI3(BaseModel):
    available: Literal[False]

    unavailable_code: Literal[
        "plan_required",
        "missing_credentials",
        "unsupported_provider",
        "chatgpt_not_connected",
        "supergrok_not_connected",
        "claude_subscription_not_connected",
    ] = FieldInfo(alias="unavailableCode")

    unavailable_reason: str = FieldInfo(alias="unavailableReason")


class InferenceProviderAccessGcpVertexAI2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


InferenceProviderAccessGcpVertexAI: TypeAlias = Union[
    InferenceProviderAccessGcpVertexAI2, InferenceProviderAccessGcpVertexAI3
]


class InferenceProviderAccessAwsBedrock3(BaseModel):
    available: Literal[False]

    unavailable_code: Literal[
        "plan_required",
        "missing_credentials",
        "unsupported_provider",
        "chatgpt_not_connected",
        "supergrok_not_connected",
        "claude_subscription_not_connected",
    ] = FieldInfo(alias="unavailableCode")

    unavailable_reason: str = FieldInfo(alias="unavailableReason")


class InferenceProviderAccessAwsBedrock2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


InferenceProviderAccessAwsBedrock: TypeAlias = Union[
    InferenceProviderAccessAwsBedrock2, InferenceProviderAccessAwsBedrock3
]


class InferenceProviderAccessByok3(BaseModel):
    available: Literal[False]

    unavailable_code: Literal[
        "plan_required",
        "missing_credentials",
        "unsupported_provider",
        "chatgpt_not_connected",
        "supergrok_not_connected",
        "claude_subscription_not_connected",
    ] = FieldInfo(alias="unavailableCode")

    unavailable_reason: str = FieldInfo(alias="unavailableReason")


class InferenceProviderAccessByok2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


InferenceProviderAccessByok: TypeAlias = Union[InferenceProviderAccessByok2, InferenceProviderAccessByok3]


class InferenceProviderAccessTemboManagedInference3(BaseModel):
    available: Literal[False]

    unavailable_code: Literal[
        "plan_required",
        "missing_credentials",
        "unsupported_provider",
        "chatgpt_not_connected",
        "supergrok_not_connected",
        "claude_subscription_not_connected",
    ] = FieldInfo(alias="unavailableCode")

    unavailable_reason: str = FieldInfo(alias="unavailableReason")


class InferenceProviderAccessTemboManagedInference2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


InferenceProviderAccessTemboManagedInference: TypeAlias = Union[
    InferenceProviderAccessTemboManagedInference2, InferenceProviderAccessTemboManagedInference3
]


class InferenceProviderAccess(BaseModel):
    tembo_managed_inference: InferenceProviderAccessTemboManagedInference = FieldInfo(alias="TemboManagedInference")

    byok: InferenceProviderAccessByok = FieldInfo(alias="BYOK")

    aws_bedrock: InferenceProviderAccessAwsBedrock = FieldInfo(alias="AWSBedrock")

    gcp_vertex_ai: InferenceProviderAccessGcpVertexAI = FieldInfo(alias="GCPVertexAI")

    open_router: InferenceProviderAccessOpenRouter = FieldInfo(alias="OpenRouter")


class ModelUpdateResponse(BaseModel):
    name: Literal[
        "claude-opus-5-5",
        "claude-fable-5-1",
        "claude-fable-5",
        "claude-opus-5",
        "claude-sonnet-5-5",
        "claude-haiku-5-5",
        "claude-opus-4-8",
        "claude-opus-4-7",
        "claude-opus-4-6",
        "claude-opus-4-5",
        "claude-4-5-haiku",
        "gpt-6.1-sol",
        "gpt-6-astra",
        "gpt-6-sol",
        "gpt-6-luna",
        "gpt-5.6-sol",
        "gpt-5.6-terra",
        "gpt-5.6-luna",
        "gpt-5.5-pro",
        "gpt-5.5",
        "gpt-5.4",
        "gpt-5.4-mini",
        "gpt-5.4-nano",
        "gpt-5.3-codex",
        "gpt-5.3-codex-spark",
        "gpt-5.2-codex",
        "gpt-5.2",
        "glm-5p3",
        "glm-5p3-flash",
        "composer-1.5",
        "composer-2",
        "composer-2-fast",
        "composer-2.5",
        "gemini-3.1-pro",
        "gemini-3.5-flash",
        "grok-4.7",
        "grok",
        "kimi-k3",
        "minimax-m2p7",
        "minimax-m3",
        "deepseek-v4-pro",
        "deepseek-v4p1-flash",
    ]

    label: str

    provider: str

    enabled: bool

    available: bool

    unavailable_reason: Optional[str] = FieldInfo(alias="unavailableReason", default=None)

    supported_inference_providers: Optional[
        List[Literal["TemboManagedInference", "BYOK", "AWSBedrock", "GCPVertexAI", "OpenRouter"]]
    ] = FieldInfo(alias="supportedInferenceProviders", default=None)

    available_inference_providers: List[
        Literal["TemboManagedInference", "BYOK", "AWSBedrock", "GCPVertexAI", "OpenRouter"]
    ] = FieldInfo(alias="availableInferenceProviders")

    configured_inference_provider: Optional[
        Literal["TemboManagedInference", "BYOK", "AWSBedrock", "GCPVertexAI", "OpenRouter"]
    ] = FieldInfo(alias="configuredInferenceProvider", default=None)

    inference_provider: Literal["TemboManagedInference", "BYOK", "AWSBedrock", "GCPVertexAI", "OpenRouter"] = FieldInfo(
        alias="inferenceProvider"
    )

    inference_provider_access: InferenceProviderAccess = FieldInfo(alias="inferenceProviderAccess")

    selected_inference_provider_available: bool = FieldInfo(alias="selectedInferenceProviderAvailable")

    selected_inference_provider_unavailable_reason: Optional[str] = FieldInfo(
        alias="selectedInferenceProviderUnavailableReason", default=None
    )

    chatgpt_available: bool = FieldInfo(alias="chatgptAvailable")

    chatgpt_supported: bool = FieldInfo(alias="chatgptSupported")

    workspace_chatgpt_available: bool = FieldInfo(alias="workspaceChatgptAvailable")

    claude_subscription_supported: bool = FieldInfo(alias="claudeSubscriptionSupported")

    workspace_claude_subscription_available: bool = FieldInfo(alias="workspaceClaudeSubscriptionAvailable")

    supergrok_available: bool = FieldInfo(alias="supergrokAvailable")

    agent_inference_available: bool = FieldInfo(alias="agentInferenceAvailable")
