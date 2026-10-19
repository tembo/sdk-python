# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["ProjectCreateParams", "Schedule"]


class ProjectCreateParams(TypedDict, total=False):
    description: Optional[str]
    """Short project description, or null to clear it."""

    include_deps: Annotated[bool, PropertyInfo(alias="includeDeps")]
    """Include project dependencies when building the environment. Defaults to true on creation."""

    include_skills: Annotated[bool, PropertyInfo(alias="includeSkills")]
    """Include skills in the project environment. Defaults to true on creation."""

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

    onboarding_default: Annotated[bool, PropertyInfo(alias="onboardingDefault")]
    """Make this project the onboarding default for the organization."""

    run_now: Annotated[bool, PropertyInfo(alias="runNow")]
    """Queue initial snapshot builds immediately when a build host is available. Defaults to false."""

    schedule: Schedule
    """Recurring schedule for rebuilding the project environment."""

    sizes: Required[List[Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"]]]
    """Workspace VM sizes to build for this project."""


class Schedule(TypedDict, total=False):
    cron: Required[str]
    """Cron expression for recurring project snapshot builds."""

    timezone: str
    """Timezone for the cron schedule. Defaults to UTC."""
