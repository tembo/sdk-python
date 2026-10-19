# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .tip_tap_document import TipTapDocument

__all__ = ["MessageListResponse", "Item", "ItemSlashCommand"]


class ItemSlashCommand(BaseModel):
    command: str

    arguments: Optional[str] = None


class Item(BaseModel):
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

    slash_command: Optional[ItemSlashCommand] = FieldInfo(alias="slashCommand", default=None)

    source: Optional[str] = None


class MessageListResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
