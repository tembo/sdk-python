# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["PullRequestListParams"]


class PullRequestListParams(TypedDict, total=False):
    author_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="authorIds")]
    """Filter authors by comma-separated provider:identifier values, such as github:octocat."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Only pull requests created after this ISO 8601 timestamp."""

    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    exclude_author_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeAuthorIds")]
    """Exclude authors by comma-separated provider:identifier values."""

    exclude_organization_name: Annotated[str, PropertyInfo(alias="excludeOrganizationName")]
    """Exclude pull requests from the named organization within the caller access scope."""

    exclude_returned_author_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeReturnedAuthorIds")]
    """Exclude returned pull requests by these comma-separated provider:identifier author values."""

    exclude_reviewer_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeReviewerIds")]
    """Exclude pull requests assigned to these comma-separated reviewer identifiers."""

    has_tembo_session: Annotated[bool, PropertyInfo(alias="hasTemboSession")]
    """When true, only return pull requests with a linked Tembo session."""

    include_authors: Annotated[bool, PropertyInfo(alias="includeAuthors")]
    """Request author filter options. Public responses do not include organization-wide author options."""

    include_total: Annotated[bool, PropertyInfo(alias="includeTotal")]
    """Include the total count of matching pull requests."""

    repository_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="repositoryIds")]
    """Filter by repository IDs, supplied as a comma-separated list."""

    reviewer_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="reviewerIds")]
    """Filter by assigned reviewer identifiers, supplied as a comma-separated list."""

    merged_after: Annotated[Union[str, datetime], PropertyInfo(alias="mergedAfter", format="iso8601")]
    """Only pull requests merged after this ISO 8601 timestamp."""

    search: str
    """Search pull requests."""

    sort_by: Annotated[Literal["createdAt", "updatedAt"], PropertyInfo(alias="sortBy")]
    """Sort by creation time or last update time."""

    state: Literal["open", "returned", "approved", "needs review", "draft", "merged", "closed"]
    """Filter by lifecycle or review state, including open, returned, approved, needs review, draft, merged, or closed."""

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Only pull requests updated after this ISO 8601 timestamp."""
