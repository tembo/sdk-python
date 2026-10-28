# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = [
    "ProjectCreateParams",
    "Schedule",
    "ResourceSettings",
    "ResourceSettings2",
    "ResourceSettings2Allocation",
    "ResourceSettings3",
    "ResourceSettings3Allocation",
]


class ProjectCreateParams(TypedDict, total=False):
    description: Optional[str]
    """Short project description, or null to clear it."""

    name: Required[str]
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

    onboarding_default: Annotated[bool, PropertyInfo(alias="onboardingDefault")]
    """Make this project the onboarding default for the organization."""

    run_now: Annotated[bool, PropertyInfo(alias="runNow")]
    """Queue initial snapshot builds immediately when a build host is available. Defaults to false."""

    schedule: Schedule
    """Recurring schedule for rebuilding the project environment."""

    sizes: List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]]
    """Workspace VM sizes to build for this project."""

    resource_settings: Annotated[ResourceSettings, PropertyInfo(alias="resourceSettings")]


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


class Schedule(TypedDict, total=False):
    cron: Required[str]
    """Cron expression for recurring project snapshot builds."""

    timezone: str
    """Timezone for the cron schedule. Defaults to UTC."""
