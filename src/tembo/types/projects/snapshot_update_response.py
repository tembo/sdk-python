# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SnapshotUpdateResponse"]


class SnapshotUpdateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    is_active: bool = FieldInfo(alias="isActive")

    name: Optional[str] = None

    pinned_at: Optional[datetime] = FieldInfo(alias="pinnedAt", default=None)

    updated_at: datetime = FieldInfo(alias="updatedAt")

    build_duration_ms: Optional[float] = FieldInfo(alias="buildDurationMs", default=None)

    built_at: Optional[datetime] = FieldInfo(alias="builtAt", default=None)

    cpu: Optional[int] = None

    has_setup_script: Optional[bool] = FieldInfo(alias="hasSetupScript", default=None)

    includes_deps: Optional[bool] = FieldInfo(alias="includesDeps", default=None)

    includes_repos: Optional[bool] = FieldInfo(alias="includesRepos", default=None)

    includes_skills: Optional[bool] = FieldInfo(alias="includesSkills", default=None)

    is_kvm: Optional[bool] = FieldInfo(alias="isKvm", default=None)

    memory_mb: Optional[int] = FieldInfo(alias="memoryMb", default=None)

    project_id: str = FieldInfo(alias="projectId")

    rebuild_of_snapshot_id: Optional[str] = FieldInfo(alias="rebuildOfSnapshotId", default=None)

    repository_ids: Optional[List[str]] = FieldInfo(alias="repositoryIds", default=None)

    setup_script: Optional[str] = FieldInfo(alias="setupScript", default=None)

    size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]] = None

    size_bytes: Optional[str] = FieldInfo(alias="sizeBytes", default=None)

    trigger: Optional[Literal["manual", "scheduled", "rebuild", "manager_reconcile", "admin"]] = None
