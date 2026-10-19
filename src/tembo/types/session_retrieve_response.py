# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SessionRetrieveResponse",
    "Artifact",
    "ArtifactPullRequest",
    "ArtifactPullRequestDiff",
    "ArtifactPullRequestAuthor",
    "ArtifactPullRequestCodeRepository",
    "DiffSummary",
    "Project",
    "SessionSource",
    "SessionSourceRepository",
    "SourcePullRequest",
    "State",
]


class State(BaseModel):
    current: Optional[Literal["inProgress", "queued", "completed", "failed", "cancelled"]] = None

    is_queued: bool = FieldInfo(alias="isQueued")

    is_cancelled: bool = FieldInfo(alias="isCancelled")

    is_completed: bool = FieldInfo(alias="isCompleted")

    is_failed: bool = FieldInfo(alias="isFailed")

    in_progress: bool = FieldInfo(alias="inProgress")


class SourcePullRequest(BaseModel):
    id: str

    url: str

    title: Optional[str] = None

    status: Literal["open", "merged", "closed"]

    is_draft: bool = FieldInfo(alias="isDraft")


class SessionSourceRepository(BaseModel):
    id: str

    name: str

    provider: str


class SessionSource(BaseModel):
    id: str

    name: str

    type: str

    repositories: List[SessionSourceRepository]


class Project(BaseModel):
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


class DiffSummary(BaseModel):
    additions: int

    deletions: int


class ArtifactPullRequestCodeRepository(BaseModel):
    id: str

    name: str

    owner: Optional[str] = None

    base_branch: Optional[str] = FieldInfo(alias="baseBranch", default=None)

    provider: str


class ArtifactPullRequestAuthor(BaseModel):
    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)

    login: Optional[str] = None


class ArtifactPullRequestDiff(BaseModel):
    additions: Optional[int] = None

    deletions: Optional[int] = None

    data: Optional[str] = None


class ArtifactPullRequest(BaseModel):
    id: str

    url: str

    title: Optional[str] = None

    status: Literal["open", "merged", "closed"]

    is_draft: bool = FieldInfo(alias="isDraft")

    source_branch: Optional[str] = FieldInfo(alias="sourceBranch", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    agent: Optional[str] = None

    diff: Optional[ArtifactPullRequestDiff] = None

    updated_at: datetime = FieldInfo(alias="updatedAt")

    base_branch: Optional[str] = FieldInfo(alias="baseBranch", default=None)

    head_sha: Optional[str] = FieldInfo(alias="headSha", default=None)

    author: Optional[ArtifactPullRequestAuthor] = None

    code_repository: Optional[ArtifactPullRequestCodeRepository] = FieldInfo(alias="codeRepository", default=None)


class Artifact(BaseModel):
    id: str

    type: Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    pull_requests: List[ArtifactPullRequest] = FieldInfo(alias="pullRequests")


class SessionRetrieveResponse(BaseModel):
    agent: Optional[str] = None

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    artifact_type: Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]] = (
        FieldInfo(alias="artifactType", default=None)
    )

    base_branch: Optional[str] = FieldInfo(alias="baseBranch", default=None)

    branch_name: Optional[str] = FieldInfo(alias="branchName", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    external_url: Optional[str] = FieldInfo(alias="externalUrl", default=None)

    id: str

    kind: str

    last_queued_at: Optional[datetime] = FieldInfo(alias="lastQueuedAt", default=None)

    last_seen_at: datetime = FieldInfo(alias="lastSeenAt")

    level: int

    mode: Literal["normal", "planning"]

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    sandbox_size: Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]] = FieldInfo(
        alias="sandboxSize", default=None
    )

    session_type: Literal["Chat", "Terminal"] = FieldInfo(alias="sessionType")

    target_branch: Optional[str] = FieldInfo(alias="targetBranch", default=None)

    title: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    visibility: Literal["public", "private"]

    artifacts: List[Artifact]

    description: Optional[str] = None

    diff_summary: Optional[DiffSummary] = FieldInfo(alias="diffSummary", default=None)

    html_url: str = FieldInfo(alias="htmlUrl")

    is_pinned: bool = FieldInfo(alias="isPinned")

    project: Optional[Project] = None

    session_source: SessionSource = FieldInfo(alias="sessionSource")

    source_pull_request: Optional[SourcePullRequest] = FieldInfo(alias="sourcePullRequest", default=None)

    state: State
