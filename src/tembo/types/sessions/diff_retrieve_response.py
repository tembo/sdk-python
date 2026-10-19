# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DiffRetrieveResponse"]


class DiffRetrieveResponse(BaseModel):
    additions: int

    baseline_sha: Optional[str] = FieldInfo(alias="baselineSha", default=None)

    branch: Optional[str] = None

    captured_at: datetime = FieldInfo(alias="capturedAt")

    changed_files: int = FieldInfo(alias="changedFiles")

    code_repository_id: Optional[str] = FieldInfo(alias="codeRepositoryId", default=None)

    deletions: int

    has_changes: bool = FieldInfo(alias="hasChanges")

    head_sha: Optional[str] = FieldInfo(alias="headSha", default=None)

    id: str

    remote_key: Optional[str] = FieldInfo(alias="remoteKey", default=None)

    root: str

    session_id: str = FieldInfo(alias="sessionId")

    untracked_files: int = FieldInfo(alias="untrackedFiles")

    data: str
