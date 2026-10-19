# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BuildRetrieveResponse", "Progress"]


class Progress(BaseModel):
    message: Optional[str] = None

    percent: Optional[float] = None

    phase: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class BuildRetrieveResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)

    failure: Optional[str] = None

    include_deps: bool = FieldInfo(alias="includeDeps")

    include_skills: bool = FieldInfo(alias="includeSkills")

    name: Optional[str] = None

    progress: Optional[Progress] = None

    project_id: str = FieldInfo(alias="projectId")

    repository_ids: Optional[List[str]] = FieldInfo(alias="repositoryIds", default=None)

    sandbox_size: Literal["nano", "micro", "medium", "large", "xl", "xxl", "ultra"] = FieldInfo(alias="sandboxSize")

    setup_script: Optional[str] = FieldInfo(alias="setupScript", default=None)

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Literal["pending", "running", "failed", "completed", "cancelled"]

    trigger: Literal["manual", "scheduled", "rebuild"]
