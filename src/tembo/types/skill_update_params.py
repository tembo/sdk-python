# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SkillUpdateParams", "File"]


class SkillUpdateParams(TypedDict, total=False):
    description: str
    """Summary of what the skill does and when to use it."""

    name: str
    """Display name of the skill."""

    files: Iterable[File]
    """Complete file set, including a required SKILL.md. On update, replaces all existing files rather than merging them."""


class File(TypedDict, total=False):
    content: Required[str]
    """Complete file content: plain text, or base64 when encoding is base64."""

    encoding: Literal["utf8", "base64"]
    """utf8 for text files; base64 for binary files such as images."""

    filename: Required[str]
    """Relative file path within the skill, such as SKILL.md."""
