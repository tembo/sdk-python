# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PinListResponse",
    "Resource",
    "Resource2",
    "Resource2Resource",
    "Resource2ResourceVM",
    "Resource2ResourceSessionSource",
    "Resource2ResourceSessionSourceSessionSourceCodeRepository",
    "Resource2ResourceSessionSourceSessionSourceCodeRepositoryCodeRepository",
    "Resource2ResourceSessionSourceSessionSourceCodeRepositoryCodeRepositoryIntegration",
    "Resource2ResourcePullRequest",
    "Resource2ResourcePullRequestDiffSummary",
    "Resource2ResourceDiffSummary",
    "Resource2ResourceState",
    "Resource3",
    "Resource3Resource",
    "Resource3ResourceAuthor",
    "Resource3ResourceCodeRepository",
    "Resource3ResourceCodeRepositoryIntegration",
    "Resource4",
    "Resource4Resource",
]


class Resource4Resource(BaseModel):
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


class Resource4(BaseModel):
    type: Literal["project"]

    resource: Resource4Resource


class Resource3ResourceCodeRepositoryIntegration(BaseModel):
    type: Literal["github", "gitlab", "bitbucket"]


class Resource3ResourceCodeRepository(BaseModel):
    name: str

    owner: Optional[str] = None

    integration: Resource3ResourceCodeRepositoryIntegration


class Resource3ResourceAuthor(BaseModel):
    login: Optional[str] = None

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)


class Resource3Resource(BaseModel):
    id: str

    url: str

    title: Optional[str] = None

    status: Literal["open", "merged", "closed"]

    is_draft: bool = FieldInfo(alias="isDraft")

    author: Optional[Resource3ResourceAuthor] = None

    code_repository: Optional[Resource3ResourceCodeRepository] = FieldInfo(alias="codeRepository", default=None)


class Resource3(BaseModel):
    type: Literal["pull_request"]

    resource: Resource3Resource


class Resource2ResourceState(BaseModel):
    current: Optional[Literal["inProgress", "queued", "completed", "failed", "cancelled"]] = None

    is_queued: bool = FieldInfo(alias="isQueued")

    is_cancelled: bool = FieldInfo(alias="isCancelled")

    is_completed: bool = FieldInfo(alias="isCompleted")

    is_failed: bool = FieldInfo(alias="isFailed")

    in_progress: bool = FieldInfo(alias="inProgress")


class Resource2ResourceDiffSummary(BaseModel):
    additions: float

    deletions: float


class Resource2ResourcePullRequestDiffSummary(BaseModel):
    additions: float

    deletions: float


class Resource2ResourcePullRequest(BaseModel):
    status: Literal["open", "merged", "closed"]

    is_draft: bool = FieldInfo(alias="isDraft")

    diff_summary: Optional[Resource2ResourcePullRequestDiffSummary] = FieldInfo(alias="diffSummary", default=None)


class Resource2ResourceSessionSourceSessionSourceCodeRepositoryCodeRepositoryIntegration(BaseModel):
    type: Literal["github", "gitlab", "bitbucket"]


class Resource2ResourceSessionSourceSessionSourceCodeRepositoryCodeRepository(BaseModel):
    id: str

    name: str

    integration: Resource2ResourceSessionSourceSessionSourceCodeRepositoryCodeRepositoryIntegration


class Resource2ResourceSessionSourceSessionSourceCodeRepository(BaseModel):
    code_repository: Resource2ResourceSessionSourceSessionSourceCodeRepositoryCodeRepository = FieldInfo(
        alias="codeRepository"
    )


class Resource2ResourceSessionSource(BaseModel):
    type: str

    name: str

    session_source_code_repositories: List[Resource2ResourceSessionSourceSessionSourceCodeRepository] = FieldInfo(
        alias="sessionSourceCodeRepositories"
    )


class Resource2ResourceVM(BaseModel):
    id: str

    status: Literal["Initializing", "Running", "Warm", "Stopping", "Idle", "Terminated"]


class Resource2Resource(BaseModel):
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

    vm: Optional[Resource2ResourceVM] = None

    session_source: Resource2ResourceSessionSource = FieldInfo(alias="sessionSource")

    pull_requests: List[Resource2ResourcePullRequest] = FieldInfo(alias="pullRequests")

    diff_summary: Optional[Resource2ResourceDiffSummary] = FieldInfo(alias="diffSummary", default=None)

    state: Resource2ResourceState

    is_unread: Optional[bool] = FieldInfo(alias="isUnread", default=None)
    """Whether the latest turn finished after the caller last viewed the session."""


class Resource2(BaseModel):
    type: Literal["session"]

    resource: Resource2Resource


Resource: TypeAlias = Union[Resource2, Resource3, Resource4]


class PinListResponse(BaseModel):
    resources: List[Resource]
    """Accessible pinned resources in pin order."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor for the next page, even when resources is empty; null at the end."""
