# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SnapshotListResponse", "Item"]


class Item(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    is_active: bool = FieldInfo(alias="isActive")

    name: Optional[str] = None

    pinned_at: Optional[datetime] = FieldInfo(alias="pinnedAt", default=None)

    updated_at: datetime = FieldInfo(alias="updatedAt")

    automatic_sizing: bool = FieldInfo(alias="automaticSizing")

    build_duration_ms: Optional[float] = FieldInfo(alias="buildDurationMs", default=None)

    built_at: Optional[datetime] = FieldInfo(alias="builtAt", default=None)

    cpu: Optional[int] = None

    disk_size_gb: Optional[float] = FieldInfo(alias="diskSizeGb", default=None)

    has_setup_script: Optional[bool] = FieldInfo(alias="hasSetupScript", default=None)

    includes_repos: Optional[bool] = FieldInfo(alias="includesRepos", default=None)

    is_kvm: Optional[bool] = FieldInfo(alias="isKvm", default=None)

    memory_mb: Optional[int] = FieldInfo(alias="memoryMb", default=None)

    project_id: str = FieldInfo(alias="projectId")

    rebuild_of_snapshot_id: Optional[str] = FieldInfo(alias="rebuildOfSnapshotId", default=None)

    repository_ids: Optional[List[str]] = FieldInfo(alias="repositoryIds", default=None)

    setup_script: Optional[str] = FieldInfo(alias="setupScript", default=None)

    size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]] = None

    size_bytes: Optional[str] = FieldInfo(alias="sizeBytes", default=None)

    trigger: Optional[Literal["manual", "scheduled", "rebuild", "manager_reconcile", "admin"]] = None


class SnapshotListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
