# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GithubIssueCommentCreatedFilters"]


class GithubIssueCommentCreatedFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the comment is in one of the repositories"""

    commented_by: Optional[List[str]] = FieldInfo(alias="commentedBy", default=None)
    """Only trigger if the comment was created by one of the specified users"""

    comment_on: Optional[List[Literal["issues", "pull_requests"]]] = FieldInfo(alias="commentOn", default=None)
    """Trigger on comments on issues, pull requests, or both"""

    message_contains: Optional[List[str]] = FieldInfo(alias="messageContains", default=None)
    """Only trigger if the comment contains one of these substrings"""
