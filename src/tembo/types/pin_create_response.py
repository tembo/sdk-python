# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PinCreateResponse",
    "PinCreateResponseResource",
    "PinCreateResponseResourceVM",
    "PinCreateResponseResourceSessionSource",
    "PinCreateResponseResourceSessionSourceSessionSourceCodeRepository",
    "PinCreateResponseResourceSessionSourceSessionSourceCodeRepositoryCodeRepository",
    "PinCreateResponseResourceSessionSourceSessionSourceCodeRepositoryCodeRepositoryIntegration",
    "PinCreateResponseResourcePullRequest",
    "PinCreateResponseResourcePullRequestDiffSummary",
    "PinCreateResponseResourceDiffSummary",
    "PinCreateResponseResourceState",
    "PinCreateResponse2",
    "PinCreateResponse2Resource",
    "PinCreateResponse2ResourceAuthor",
    "PinCreateResponse2ResourceCodeRepository",
    "PinCreateResponse2ResourceCodeRepositoryIntegration",
    "PinCreateResponse3",
    "PinCreateResponse3Resource",
]


class PinCreateResponse3Resource(BaseModel):
    id: str

    name: str

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

    color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"]


class PinCreateResponse3(BaseModel):
    type: Literal["project"]

    resource: PinCreateResponse3Resource


class PinCreateResponse2ResourceCodeRepositoryIntegration(BaseModel):
    type: Literal["github", "gitlab", "bitbucket"]


class PinCreateResponse2ResourceCodeRepository(BaseModel):
    name: str

    owner: Optional[str] = None

    integration: PinCreateResponse2ResourceCodeRepositoryIntegration


class PinCreateResponse2ResourceAuthor(BaseModel):
    login: Optional[str] = None

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)


class PinCreateResponse2Resource(BaseModel):
    id: str

    url: str

    title: Optional[str] = None

    status: Literal["open", "merged", "closed"]

    is_draft: bool = FieldInfo(alias="isDraft")

    author: Optional[PinCreateResponse2ResourceAuthor] = None

    code_repository: Optional[PinCreateResponse2ResourceCodeRepository] = FieldInfo(
        alias="codeRepository", default=None
    )


class PinCreateResponse2(BaseModel):
    type: Literal["pull_request"]

    resource: PinCreateResponse2Resource


class PinCreateResponseResourceState(BaseModel):
    current: Optional[Literal["inProgress", "queued", "completed", "failed", "cancelled"]] = None

    is_queued: bool = FieldInfo(alias="isQueued")

    is_cancelled: bool = FieldInfo(alias="isCancelled")

    is_completed: bool = FieldInfo(alias="isCompleted")

    is_failed: bool = FieldInfo(alias="isFailed")

    in_progress: bool = FieldInfo(alias="inProgress")


class PinCreateResponseResourceDiffSummary(BaseModel):
    additions: float

    deletions: float


class PinCreateResponseResourcePullRequestDiffSummary(BaseModel):
    additions: float

    deletions: float


class PinCreateResponseResourcePullRequest(BaseModel):
    status: Literal["open", "merged", "closed"]

    is_draft: bool = FieldInfo(alias="isDraft")

    diff_summary: Optional[PinCreateResponseResourcePullRequestDiffSummary] = FieldInfo(
        alias="diffSummary", default=None
    )


class PinCreateResponseResourceSessionSourceSessionSourceCodeRepositoryCodeRepositoryIntegration(BaseModel):
    type: Literal["github", "gitlab", "bitbucket"]


class PinCreateResponseResourceSessionSourceSessionSourceCodeRepositoryCodeRepository(BaseModel):
    id: str

    name: str

    integration: PinCreateResponseResourceSessionSourceSessionSourceCodeRepositoryCodeRepositoryIntegration


class PinCreateResponseResourceSessionSourceSessionSourceCodeRepository(BaseModel):
    code_repository: PinCreateResponseResourceSessionSourceSessionSourceCodeRepositoryCodeRepository = FieldInfo(
        alias="codeRepository"
    )


class PinCreateResponseResourceSessionSource(BaseModel):
    type: str

    name: str

    session_source_code_repositories: List[PinCreateResponseResourceSessionSourceSessionSourceCodeRepository] = (
        FieldInfo(alias="sessionSourceCodeRepositories")
    )


class PinCreateResponseResourceVM(BaseModel):
    id: str

    status: Literal["Initializing", "Running", "Warm", "Stopping", "Idle", "Terminated"]


class PinCreateResponseResource(BaseModel):
    id: str

    title: str

    kind: str

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    last_queued_at: Optional[datetime] = FieldInfo(alias="lastQueuedAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    level: int

    visibility: Literal["public", "private"]

    vm: Optional[PinCreateResponseResourceVM] = None

    session_source: PinCreateResponseResourceSessionSource = FieldInfo(alias="sessionSource")

    pull_requests: List[PinCreateResponseResourcePullRequest] = FieldInfo(alias="pullRequests")

    diff_summary: Optional[PinCreateResponseResourceDiffSummary] = FieldInfo(alias="diffSummary", default=None)

    state: PinCreateResponseResourceState


class PinCreateResponse(BaseModel):
    type: Literal["session"]

    resource: PinCreateResponseResource


PinCreateResponse: TypeAlias = Union[PinCreateResponse, PinCreateResponse2, PinCreateResponse3]
