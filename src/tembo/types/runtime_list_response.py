# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "RuntimeListResponse",
    "Item",
    "ItemRunCapabilities",
    "ItemAvailability",
    "ItemAvailability2",
    "ItemAvailability3",
    "ItemCompatibleModel",
    "ItemCompatibleModelAvailability",
    "ItemCompatibleModelAvailability2",
    "ItemCompatibleModelAvailability3",
]


class ItemCompatibleModelAvailability3(BaseModel):
    status: Literal["unavailable"]

    code: Literal[
        "model_disabled",
        "plan_required",
        "missing_credentials",
        "unsupported_provider",
        "chatgpt_not_connected",
        "supergrok_not_connected",
        "claude_subscription_not_connected",
    ]

    reason: str


class ItemCompatibleModelAvailability2(BaseModel):
    status: Literal["available"]


ItemCompatibleModelAvailability: TypeAlias = Union[ItemCompatibleModelAvailability2, ItemCompatibleModelAvailability3]


class ItemCompatibleModel(BaseModel):
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

    is_default: bool = FieldInfo(alias="isDefault")

    is_platform_default: bool = FieldInfo(alias="isPlatformDefault")

    reasoning_levels: List[str] = FieldInfo(alias="reasoningLevels")

    availability: ItemCompatibleModelAvailability


class ItemAvailability3(BaseModel):
    status: Literal["unavailable"]

    code: Literal["plan_required", "missing_credentials"]

    reason: str


class ItemAvailability2(BaseModel):
    status: Literal["available"]


ItemAvailability: TypeAlias = Union[ItemAvailability2, ItemAvailability3]


class ItemRunCapabilities(BaseModel):
    modes: List[Literal["normal", "planning"]]

    speeds: List[Literal["normal", "fast", "ultrafast"]]

    supports_goals: bool = FieldInfo(alias="supportsGoals")


class Item(BaseModel):
    name: Literal["claudeCode", "codex", "opencode", "cursor", "amp", "fx", "pi"]

    display_name: str = FieldInfo(alias="displayName")

    default_model_name: Literal[
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
    ] = FieldInfo(alias="defaultModelName")

    requires_api_key: bool = FieldInfo(alias="requiresApiKey")

    has_api_key: bool = FieldInfo(alias="hasApiKey")

    run_capabilities: ItemRunCapabilities = FieldInfo(alias="runCapabilities")

    availability: ItemAvailability

    compatible_models: List[ItemCompatibleModel] = FieldInfo(alias="compatibleModels")


class RuntimeListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[Literal["claudeCode", "codex", "opencode", "cursor", "amp", "fx", "pi"]] = FieldInfo(
        alias="nextCursor", default=None
    )
