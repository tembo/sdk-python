# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PullRequestRetrieveResponse", "Author", "CodeRepository", "Diff", "Reviewer", "Session"]


class Session(BaseModel):
    id: str

    title: str

    kind: str

    html_url: str = FieldInfo(alias="htmlUrl")

    visibility: Optional[Literal["private", "public"]] = None


class Reviewer(BaseModel):
    id: str

    login: str

    name: str

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)

    profile_url: Optional[str] = FieldInfo(alias="profileUrl", default=None)

    type: Optional[Literal["bot", "user"]] = None

    review_requested: bool = FieldInfo(alias="reviewRequested")

    commented: bool

    approved: bool

    state: Optional[Literal["approved", "changes_requested", "commented", "awaiting"]] = None

    changes_requested: Optional[bool] = FieldInfo(alias="changesRequested", default=None)

    awaiting_review: Optional[bool] = FieldInfo(alias="awaitingReview", default=None)


class Diff(BaseModel):
    additions: int

    deletions: int

    data: str


class CodeRepository(BaseModel):
    id: str

    name: str

    url: str

    owner: Optional[str] = None

    target_branch: Optional[str] = FieldInfo(alias="targetBranch", default=None)

    base_branch: Optional[str] = FieldInfo(alias="baseBranch", default=None)

    provider: str


class Author(BaseModel):
    id: Optional[str] = None

    login: Optional[str] = None

    name: Optional[str] = None

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)

    profile_url: Optional[str] = FieldInfo(alias="profileUrl", default=None)


class PullRequestRetrieveResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    external_id: str = FieldInfo(alias="externalId")

    external_provider: str = FieldInfo(alias="externalProvider")

    id: str

    is_draft: bool = FieldInfo(alias="isDraft")

    merged_at: Optional[datetime] = FieldInfo(alias="mergedAt", default=None)

    review_decision: Optional[Literal["APPROVED", "CHANGES_REQUESTED", "REVIEW_REQUIRED"]] = FieldInfo(
        alias="reviewDecision", default=None
    )

    source_branch: Optional[str] = FieldInfo(alias="sourceBranch", default=None)

    status: Literal["open", "merged", "closed"]

    title: Optional[str] = None

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str

    author: Author

    base_branch: Optional[str] = FieldInfo(alias="baseBranch", default=None)

    code_repository: Optional[CodeRepository] = FieldInfo(alias="codeRepository", default=None)

    diff: Optional[Diff] = None

    head_sha: Optional[str] = FieldInfo(alias="headSha", default=None)

    number: Optional[int] = None

    owner: Optional[str] = None

    reviewers: List[Reviewer]

    state: Literal["approved", "needs review", "draft", "merged", "closed"]

    session: Optional[Session] = None
