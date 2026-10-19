# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["ArtifactListParams"]


class ArtifactListParams(TypedDict, total=False):
    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    job_id: Annotated[str, PropertyInfo(alias="jobId")]
    """Filter artifacts created by this job."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """Filter artifacts attached to this session."""

    types: List[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]]
    """Filter artifact types, supplied as a comma-separated list."""
