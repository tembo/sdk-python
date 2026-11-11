# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionImportParams", "Message"]


class SessionImportParams(TypedDict, total=False):
    source: Required[Literal["conductor", "chatgpt", "claude", "devin"]]
    """Application the chat is imported from."""

    external_id: Required[Annotated[str, PropertyInfo(alias="externalId")]]
    """Chat ID in the source application. Importing the same chat again returns the existing session."""

    title: Required[str]
    """Title of the chat."""

    messages: Required[Iterable[Message]]
    """Chat messages in the order they were sent."""


class Message(TypedDict, total=False):
    id: Required[str]

    role: Required[Literal["user", "assistant", "summary"]]
    """Who wrote the row. Conductor assistant rows hold Claude Agent SDK JSON; local ChatGPT/Codex, Claude Code, and Devin rows hold native message JSON for API conversion."""

    content: Required[str]

    sent_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="sentAt", format="iso8601")]]
