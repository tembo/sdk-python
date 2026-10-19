# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectUpdateResponse", "ActiveSnapshot"]


class ActiveSnapshot(BaseModel):
    id: str

    size: Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]

    built_at: datetime = FieldInfo(alias="builtAt")


class ProjectUpdateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    id: str

    include_deps: bool = FieldInfo(alias="includeDeps")

    include_skills: bool = FieldInfo(alias="includeSkills")

    name: str

    setup_script: Optional[str] = FieldInfo(alias="setupScript", default=None)

    updated_at: datetime = FieldInfo(alias="updatedAt")

    active_snapshots: List[ActiveSnapshot] = FieldInfo(alias="activeSnapshots")

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
