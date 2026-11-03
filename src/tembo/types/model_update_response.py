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
    name: str

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
