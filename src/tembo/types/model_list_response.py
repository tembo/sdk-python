# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ModelListResponse",
    "Item",
    "ItemInferenceProviderAccess",
    "ItemInferenceProviderAccessTemboManagedInference",
    "ItemInferenceProviderAccessTemboManagedInference2",
    "ItemInferenceProviderAccessTemboManagedInference3",
    "ItemInferenceProviderAccessByok",
    "ItemInferenceProviderAccessByok2",
    "ItemInferenceProviderAccessByok3",
    "ItemInferenceProviderAccessAwsBedrock",
    "ItemInferenceProviderAccessAwsBedrock2",
    "ItemInferenceProviderAccessAwsBedrock3",
    "ItemInferenceProviderAccessGcpVertexAI",
    "ItemInferenceProviderAccessGcpVertexAI2",
    "ItemInferenceProviderAccessGcpVertexAI3",
    "ItemInferenceProviderAccessOpenRouter",
    "ItemInferenceProviderAccessOpenRouter2",
    "ItemInferenceProviderAccessOpenRouter3",
]


class ItemInferenceProviderAccessOpenRouter3(BaseModel):
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


class ItemInferenceProviderAccessOpenRouter2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


ItemInferenceProviderAccessOpenRouter: TypeAlias = Union[
    ItemInferenceProviderAccessOpenRouter2, ItemInferenceProviderAccessOpenRouter3
]


class ItemInferenceProviderAccessGcpVertexAI3(BaseModel):
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


class ItemInferenceProviderAccessGcpVertexAI2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


ItemInferenceProviderAccessGcpVertexAI: TypeAlias = Union[
    ItemInferenceProviderAccessGcpVertexAI2, ItemInferenceProviderAccessGcpVertexAI3
]


class ItemInferenceProviderAccessAwsBedrock3(BaseModel):
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


class ItemInferenceProviderAccessAwsBedrock2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


ItemInferenceProviderAccessAwsBedrock: TypeAlias = Union[
    ItemInferenceProviderAccessAwsBedrock2, ItemInferenceProviderAccessAwsBedrock3
]


class ItemInferenceProviderAccessByok3(BaseModel):
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


class ItemInferenceProviderAccessByok2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


ItemInferenceProviderAccessByok: TypeAlias = Union[ItemInferenceProviderAccessByok2, ItemInferenceProviderAccessByok3]


class ItemInferenceProviderAccessTemboManagedInference3(BaseModel):
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


class ItemInferenceProviderAccessTemboManagedInference2(BaseModel):
    available: Literal[True]

    unavailable_code: None = FieldInfo(alias="unavailableCode", default=None)

    unavailable_reason: None = FieldInfo(alias="unavailableReason", default=None)


ItemInferenceProviderAccessTemboManagedInference: TypeAlias = Union[
    ItemInferenceProviderAccessTemboManagedInference2, ItemInferenceProviderAccessTemboManagedInference3
]


class ItemInferenceProviderAccess(BaseModel):
    tembo_managed_inference: ItemInferenceProviderAccessTemboManagedInference = FieldInfo(alias="TemboManagedInference")

    byok: ItemInferenceProviderAccessByok = FieldInfo(alias="BYOK")

    aws_bedrock: ItemInferenceProviderAccessAwsBedrock = FieldInfo(alias="AWSBedrock")

    gcp_vertex_ai: ItemInferenceProviderAccessGcpVertexAI = FieldInfo(alias="GCPVertexAI")

    open_router: ItemInferenceProviderAccessOpenRouter = FieldInfo(alias="OpenRouter")


class Item(BaseModel):
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

    inference_provider_access: ItemInferenceProviderAccess = FieldInfo(alias="inferenceProviderAccess")

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


class ModelListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[
        Literal[
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
    ] = FieldInfo(alias="nextCursor", default=None)
