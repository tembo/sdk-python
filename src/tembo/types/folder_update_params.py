# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["FolderUpdateParams", "Placement", "AddSession", "AddSessionPlacement", "RemoveSession"]


class FolderUpdateParams(TypedDict, total=False):
    name: str
    """Folder name shown in the sidebar."""

    color: Literal["neutral", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"]
    """Folder icon color, from the same palette as project icons."""

    placement: Placement
    """Where to put this folder in your sidebar folder list. Pinned folders are ordered with updatePin instead."""

    add_session: Annotated[AddSession, PropertyInfo(alias="addSession")]
    """Session to put in this folder, taking it out of any other folder of yours, or to reorder within it."""

    remove_session: Annotated[RemoveSession, PropertyInfo(alias="removeSession")]
    """Session to take out of this folder."""


class RemoveSession(TypedDict, total=False):
    id: Required[str]


class AddSessionPlacement(TypedDict, total=False):
    target: Required[str]
    """Session in this folder to place the added session next to."""

    position: Required[Literal["before", "after"]]
    """Whether to place the session before or after the target."""


class AddSession(TypedDict, total=False):
    id: Required[str]

    placement: AddSessionPlacement
    """Where to put the session in the folder. Omit to put a newly added session first and leave one already here where it is."""


class Placement(TypedDict, total=False):
    target: Required[str]
    """Another of your folders to place this folder next to."""

    position: Required[Literal["before", "after"]]
    """Whether to place this folder before or after the target."""
