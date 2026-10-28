# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProjectListResponse",
    "Item",
    "ItemActiveSnapshot",
    "ItemResourceSettings",
    "ItemResourceSettings2",
    "ItemResourceSettings2Allocation",
    "ItemResourceSettings3",
    "ItemResourceSettings3Allocation",
    "ItemWarmPoolSchedule",
]


class ItemWarmPoolSchedule(BaseModel):
    timezone: str

    days: List[int]

    start_time: str = FieldInfo(alias="startTime")

    end_time: str = FieldInfo(alias="endTime")


class ItemResourceSettings3Allocation(BaseModel):
    cpu_min: Optional[int] = FieldInfo(alias="cpuMin", default=None)

    cpu_max: Optional[int] = FieldInfo(alias="cpuMax", default=None)

    memory_min_mb: int = FieldInfo(alias="memoryMinMb")

    memory_max_mb: int = FieldInfo(alias="memoryMaxMb")

    disk_size_gb: int = FieldInfo(alias="diskSizeGb")


class ItemResourceSettings3(BaseModel):
    automatic_sizing: Literal[False] = FieldInfo(alias="automaticSizing")

    allocation: Optional[ItemResourceSettings3Allocation] = None


class ItemResourceSettings2Allocation(BaseModel):
    cpu_min: Optional[int] = FieldInfo(alias="cpuMin", default=None)

    cpu_max: Optional[int] = FieldInfo(alias="cpuMax", default=None)

    memory_min_mb: int = FieldInfo(alias="memoryMinMb")

    memory_max_mb: int = FieldInfo(alias="memoryMaxMb")

    disk_size_gb: int = FieldInfo(alias="diskSizeGb")


class ItemResourceSettings2(BaseModel):
    automatic_sizing: Literal[True] = FieldInfo(alias="automaticSizing")

    allocation: Optional[ItemResourceSettings2Allocation] = None


ItemResourceSettings: TypeAlias = Union[ItemResourceSettings2, ItemResourceSettings3]


class ItemActiveSnapshot(BaseModel):
    id: str

    size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]

    built_at: datetime = FieldInfo(alias="builtAt")


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    id: str

    name: str

    setup_script: Optional[str] = FieldInfo(alias="setupScript", default=None)

    updated_at: datetime = FieldInfo(alias="updatedAt")

    active_snapshots: List[ItemActiveSnapshot] = FieldInfo(alias="activeSnapshots")

    resource_settings: Optional[ItemResourceSettings] = FieldInfo(alias="resourceSettings", default=None)

    agent_instructions: Optional[str] = FieldInfo(alias="agentInstructions", default=None)

    code_repository_ids: Optional[List[str]] = FieldInfo(alias="codeRepositoryIds", default=None)

    color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"]

    default_for_sizes: List[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]] = FieldInfo(
        alias="defaultForSizes"
    )

    icon: Literal[
        "folder",
        "code",
        "terminal",
        "book",
        "brain",
        "bug",
        "building",
        "cloud",
        "globe",
        "idea",
        "tools",
        "magic",
        "processor",
        "sandbox",
        "server",
        "tasks",
        "tactics",
        "images",
        "database",
        "api",
        "mobile",
        "package",
    ]

    onboarding_default: bool = FieldInfo(alias="onboardingDefault")
    """True for the project created during onboarding until it is first edited"""

    sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]]

    warm_pool_enabled: bool = FieldInfo(alias="warmPoolEnabled")

    warm_pool_schedule: Optional[ItemWarmPoolSchedule] = FieldInfo(alias="warmPoolSchedule", default=None)


class ProjectListResponse(BaseModel):
    has_built_snapshot: bool = FieldInfo(alias="hasBuiltSnapshot")

    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
