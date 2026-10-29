# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Filter sessions created by this automation agent."""

    created_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="createdBy")]
    """Filter by creator IDs, supplied as a comma-separated list."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Only sessions created after this ISO 8601 timestamp."""

    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    exclude_pinned: Annotated[bool, PropertyInfo(alias="excludePinned")]
    """Exclude sessions pinned by the authenticated user."""

    external_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="externalIds")]
    """Filter by external source IDs, supplied as a comma-separated list."""

    has_project: Annotated[bool, PropertyInfo(alias="hasProject")]
    """Filter by whether a session has an assigned project."""

    include_archived: Annotated[bool, PropertyInfo(alias="includeArchived")]
    """Include archived sessions in the all-state view. Defaults to true; state=archived explicitly selects archived sessions."""

    include_total: Annotated[bool, PropertyInfo(alias="includeTotal")]
    """Include totalCount. Not supported with state=active."""

    parent_session_id: Annotated[str, PropertyInfo(alias="parentSessionId")]
    """Filter sessions created by this session."""

    participant: SequenceNotStr[str]
    """Filter by participant IDs, supplied as a comma-separated list."""

    pending_reviewer_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="pendingReviewerKeys")]
    """Filter by pending reviewer keys, supplied as a comma-separated list."""

    project_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectIds")]
    """Filter by project IDs, supplied as a comma-separated list."""

    pull_request_statuses: Annotated[
        List[Literal["open", "merged", "closed"]], PropertyInfo(alias="pullRequestStatuses")
    ]
    """Filter by linked pull request statuses: open, merged, or closed, supplied as a comma-separated list."""

    repository_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="repositoryIds")]
    """Filter by repository IDs, supplied as a comma-separated list."""

    search: str
    """Search session titles, task prompts, kinds, and source names or types."""

    sort_by: Annotated[Literal["lastQueuedAt", "createdAt", "updatedAt"], PropertyInfo(alias="sortBy")]
    """Timestamp used to sort sessions, newest first."""

    source_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="sourceIds")]
    """Filter by session source IDs, supplied as a comma-separated list."""

    source_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="sourceTypes")]
    """Filter by session source types, supplied as a comma-separated list."""

    state: Literal["all", "active", "archived"]
    """Select all sessions, currently active work, or archived sessions. Use archived to find sessions to restore."""
