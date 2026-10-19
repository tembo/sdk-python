# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["ProjectUpdateParams", "Schedule"]


class ProjectUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Short project description, or null to clear it."""

    include_deps: Annotated[bool, PropertyInfo(alias="includeDeps")]
    """Include project dependencies when building the environment. Defaults to true on creation."""

    include_skills: Annotated[bool, PropertyInfo(alias="includeSkills")]
    """Include skills in the project environment. Defaults to true on creation."""

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

    warm_pool_enabled: Annotated[bool, PropertyInfo(alias="warmPoolEnabled")]
    """Enable or disable prewarmed VMs for this project."""


class Schedule(TypedDict, total=False):
    cron: str
    """Replace the recurring project build cron expression."""

    enabled: bool
    """Enable or pause scheduled project builds."""

    timezone: Optional[str]
    """Timezone for the cron schedule, or null to clear it."""
