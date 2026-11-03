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
    name: str

    label: str

    provider: str

    inference_source: Optional[str] = FieldInfo(alias="inferenceSource", default=None)
    """Selected subscription, API provider, or CLI API billing source for this runtime and model."""

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

    ultracode_models: List[str] = FieldInfo(alias="ultracodeModels")
    """Models that support ultracode workflow orchestration."""


class Item(BaseModel):
    name: Literal["claudeCode", "codex", "opencode", "cursor", "amp", "fx", "pi"]

    display_name: str = FieldInfo(alias="displayName")

    default_model_name: str = FieldInfo(alias="defaultModelName")

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
