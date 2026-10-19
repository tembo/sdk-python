# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TriggerRetrieveResponse",
    "Filters",
    "FiltersProperties",
    "FiltersProperties2",
    "FiltersProperties3",
    "FiltersProperties4",
    "FiltersProperties4Items",
]


class FiltersProperties4Items(BaseModel):
    enum: Optional[List[str]] = None

    type: Literal["string"]


class FiltersProperties4(BaseModel):
    description: Optional[str] = None

    items: FiltersProperties4Items

    type: Literal["array"]


class FiltersProperties3(BaseModel):
    description: Optional[str] = None

    enum: Optional[List[str]] = None

    type: Literal["string"]


class FiltersProperties2(BaseModel):
    description: Optional[str] = None

    type: Literal["boolean"]

    default: Optional[bool] = None


FiltersProperties: TypeAlias = Union[FiltersProperties2, FiltersProperties3, FiltersProperties4]


class Filters(BaseModel):
    properties: Dict[str, FiltersProperties]


class TriggerRetrieveResponse(BaseModel):
    description: str

    display_name: str = FieldInfo(alias="displayName")

    filters: Optional[Filters] = None

    has_filter_options: bool = FieldInfo(alias="hasFilterOptions")

    name: str

    integration_id: str = FieldInfo(alias="integrationId")

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

    default_filters: Dict[str, Union[bool, str, List[str]]] = FieldInfo(alias="defaultFilters")
