# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .tip_tap_document import TipTapDocument

__all__ = ["MessageCreateResponse", "HotPath", "Job", "Message", "MessageSlashCommand", "Session"]


class Session(BaseModel):
    id: str

    title: str


class MessageSlashCommand(BaseModel):
    command: str

    arguments: Optional[str] = None


class Message(BaseModel):
    artifact_id: Optional[str] = FieldInfo(alias="artifactId", default=None)

    content: str

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    external_avatar_url: Optional[str] = FieldInfo(alias="externalAvatarUrl", default=None)

    external_url: Optional[str] = FieldInfo(alias="externalUrl", default=None)

    id: str

    parent_message_id: Optional[str] = FieldInfo(alias="parentMessageId", default=None)

    pull_request_id: Optional[str] = FieldInfo(alias="pullRequestId", default=None)

    role: Literal["user", "assistant", "system"]

    session_id: Optional[str] = FieldInfo(alias="sessionId", default=None)

    type: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    rich_content: Optional[TipTapDocument] = FieldInfo(alias="richContent", default=None)
    """Rich-text representation of the message, including formatting and mentions. The content field contains its text representation."""

    slash_command: Optional[MessageSlashCommand] = FieldInfo(alias="slashCommand", default=None)

    source: Optional[str] = None

    is_queued: bool = FieldInfo(alias="isQueued")


class Job(BaseModel):
    id: str

    task: str


class HotPath(BaseModel):
    active_provider_turn_id: Optional[str] = FieldInfo(alias="activeProviderTurnId", default=None)

    mode: Optional[Literal["started", "steered", "queued"]] = None

    provider_session_id: Optional[str] = FieldInfo(alias="providerSessionId", default=None)

    queued_turn_id: Optional[str] = FieldInfo(alias="queuedTurnId", default=None)

    transport: Optional[str] = None


class MessageCreateResponse(BaseModel):
    hot_path: Optional[HotPath] = FieldInfo(alias="hotPath", default=None)

    job: Optional[Job] = None

    message: Message

    session: Session
