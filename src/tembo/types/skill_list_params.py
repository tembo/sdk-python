# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["SkillListParams"]


class SkillListParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    names: SequenceNotStr[str]
    """Filter by exact skill names."""

    repository_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="repositoryIds")]
    """Repository IDs to search for checked-in skills, supplied as a comma-separated list."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project whose repositories to search for checked-in skills."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Session whose repositories to search for checked-in skills."""

    search: str
    """Search skills by name, description, or keywords."""

    source: Literal["organization", "repository"]
    """organization lists saved organization skills; repository lists checked-in skills from the selected repositories, project, or session."""
