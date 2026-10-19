# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SessionListResponse",
    "Item",
    "ItemArtifact",
    "ItemArtifactPullRequest",
    "ItemArtifactPullRequestCodeRepository",
    "ItemDiffSummary",
    "ItemProject",
    "ItemSessionSource",
    "ItemSessionSourceRepository",
    "ItemSourcePullRequest",
    "ItemState",
]


class ItemState(BaseModel):
    current: Optional[Literal["inProgress", "queued", "completed", "failed", "cancelled"]] = None

    is_queued: bool = FieldInfo(alias="isQueued")

    is_cancelled: bool = FieldInfo(alias="isCancelled")

    is_completed: bool = FieldInfo(alias="isCompleted")

    is_failed: bool = FieldInfo(alias="isFailed")

    in_progress: bool = FieldInfo(alias="inProgress")


class ItemSourcePullRequest(BaseModel):
    id: str

    url: str

    title: Optional[str] = None

    status: Literal["open", "merged", "closed"]

    is_draft: bool = FieldInfo(alias="isDraft")


class ItemSessionSourceRepository(BaseModel):
    id: str


class ItemSessionSource(BaseModel):
    id: str

    name: str

    type: str

    repositories: List[ItemSessionSourceRepository]


class ItemProject(BaseModel):
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


class ItemDiffSummary(BaseModel):
    additions: int

    deletions: int


class ItemArtifactPullRequestCodeRepository(BaseModel):
    id: str

    provider: str


class ItemArtifactPullRequest(BaseModel):
    agent: Optional[str] = None

    code_repository: Optional[ItemArtifactPullRequestCodeRepository] = FieldInfo(alias="codeRepository", default=None)

    id: str

    is_draft: bool = FieldInfo(alias="isDraft")

    status: Literal["open", "merged", "closed"]

    url: str


class ItemArtifact(BaseModel):
    id: str

    pull_requests: List[ItemArtifactPullRequest] = FieldInfo(alias="pullRequests")

    type: Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]


class Item(BaseModel):
    agent: Optional[str] = None

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    id: str

    kind: str

    last_queued_at: Optional[datetime] = FieldInfo(alias="lastQueuedAt", default=None)

    last_seen_at: datetime = FieldInfo(alias="lastSeenAt")

    level: int

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    title: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    visibility: Literal["public", "private"]

    artifacts: List[ItemArtifact]

    diff_summary: Optional[ItemDiffSummary] = FieldInfo(alias="diffSummary", default=None)

    is_pinned: bool = FieldInfo(alias="isPinned")

    project: Optional[ItemProject] = None

    session_source: ItemSessionSource = FieldInfo(alias="sessionSource")

    source_pull_request: Optional[ItemSourcePullRequest] = FieldInfo(alias="sourcePullRequest", default=None)

    state: ItemState


class SessionListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
