# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TriggerListResponse",
    "Item",
    "ItemTrigger",
    "ItemTriggerFilters",
    "ItemTriggerFiltersProperties",
    "ItemTriggerFiltersProperties2",
    "ItemTriggerFiltersProperties3",
    "ItemTriggerFiltersProperties4",
    "ItemTriggerFiltersProperties4Items",
]


class ItemTriggerFiltersProperties4Items(BaseModel):
    enum: Optional[List[str]] = None

    type: Literal["string"]


class ItemTriggerFiltersProperties4(BaseModel):
    description: Optional[str] = None

    items: ItemTriggerFiltersProperties4Items

    type: Literal["array"]


class ItemTriggerFiltersProperties3(BaseModel):
    description: Optional[str] = None

    enum: Optional[List[str]] = None

    type: Literal["string"]


class ItemTriggerFiltersProperties2(BaseModel):
    description: Optional[str] = None

    type: Literal["boolean"]

    default: Optional[bool] = None


ItemTriggerFiltersProperties: TypeAlias = Union[
    ItemTriggerFiltersProperties2, ItemTriggerFiltersProperties3, ItemTriggerFiltersProperties4
]


class ItemTriggerFilters(BaseModel):
    properties: Dict[str, ItemTriggerFiltersProperties]


class ItemTrigger(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    filters: Optional[ItemTriggerFilters] = None

    has_filter_options: bool = FieldInfo(alias="hasFilterOptions")

    name: str


class Item(BaseModel):
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

    triggers: List[ItemTrigger]


class TriggerListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
