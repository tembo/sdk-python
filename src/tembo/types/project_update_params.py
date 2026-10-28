# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = [
    "ProjectUpdateParams",
    "ResourceSettings",
    "ResourceSettings2",
    "ResourceSettings2Allocation",
    "ResourceSettings3",
    "ResourceSettings3Allocation",
    "Schedule",
    "WarmPoolSchedule",
]


class ProjectUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Short project description, or null to clear it."""

    name: str
    """Project display name."""

    setup_script: Annotated[Optional[str], PropertyInfo(alias="setupScript")]
    """Setup script to run while building the environment, or null to clear it."""

    code_repository_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="codeRepositoryIds")]
    """Repository IDs included in the project environment. On update, replaces the repository selection."""

    agent_instructions: Annotated[Optional[str], PropertyInfo(alias="agentInstructions")]
    """Instructions supplied to agents using this project, or null to clear them."""

    color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"]
    """Project display color."""

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
    """Project display icon."""

    include_deps: Annotated[bool, PropertyInfo(alias="includeDeps")]
    """Deprecated and ignored. Project builds always install dependencies."""

    include_skills: Annotated[bool, PropertyInfo(alias="includeSkills")]
    """Deprecated and ignored. Project builds always include skills."""

    resource_settings: Annotated[ResourceSettings, PropertyInfo(alias="resourceSettings")]

    default_for_sizes: Annotated[
        List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]], PropertyInfo(alias="defaultForSizes")
    ]
    """VM sizes for which this project is the organization default. An empty array removes its default assignments."""

    environment_variables: Annotated[Dict[str, str], PropertyInfo(alias="environmentVariables")]
    """Replace the complete environment-variable map. Use createProjectEnvironmentVariables to add or replace individual keys instead."""

    schedule: Schedule
    """Change the project build schedule, including enabling or pausing it."""

    sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]]
    """Replace the workspace VM sizes built for this project."""

    warm_pool_schedule: Annotated[Optional[WarmPoolSchedule], PropertyInfo(alias="warmPoolSchedule")]
    """Weekly availability for prewarmed VMs. Null means always on; days use 0=Sunday. Overnight windows end the following day."""

    warm_pool_enabled: Annotated[bool, PropertyInfo(alias="warmPoolEnabled")]
    """Enable or disable prewarmed VMs for this project."""


class WarmPoolSchedule(TypedDict, total=False):
    timezone: Required[str]

    days: Required[Iterable[int]]

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]

    end_time: Required[Annotated[str, PropertyInfo(alias="endTime")]]


class Schedule(TypedDict, total=False):
    cron: str
    """Replace the recurring project build cron expression."""

    enabled: bool
    """Enable or pause scheduled project builds."""

    timezone: Optional[str]
    """Timezone for the cron schedule, or null to clear it."""


class ResourceSettings3Allocation(TypedDict, total=False):
    cpu_min: Annotated[int, PropertyInfo(alias="cpuMin")]

    cpu_max: Annotated[int, PropertyInfo(alias="cpuMax")]

    memory_min_mb: Required[Annotated[int, PropertyInfo(alias="memoryMinMb")]]

    memory_max_mb: Required[Annotated[int, PropertyInfo(alias="memoryMaxMb")]]

    disk_size_gb: Required[Annotated[int, PropertyInfo(alias="diskSizeGb")]]


class ResourceSettings3(TypedDict, total=False):
    automatic_sizing: Required[Annotated[Literal[False], PropertyInfo(alias="automaticSizing")]]

    allocation: ResourceSettings3Allocation


class ResourceSettings2Allocation(TypedDict, total=False):
    cpu_min: Annotated[int, PropertyInfo(alias="cpuMin")]

    cpu_max: Annotated[int, PropertyInfo(alias="cpuMax")]

    memory_min_mb: Required[Annotated[int, PropertyInfo(alias="memoryMinMb")]]

    memory_max_mb: Required[Annotated[int, PropertyInfo(alias="memoryMaxMb")]]

    disk_size_gb: Required[Annotated[int, PropertyInfo(alias="diskSizeGb")]]


class ResourceSettings2(TypedDict, total=False):
    automatic_sizing: Required[Annotated[Literal[True], PropertyInfo(alias="automaticSizing")]]

    allocation: ResourceSettings2Allocation


ResourceSettings: TypeAlias = Union[ResourceSettings2, ResourceSettings3]
