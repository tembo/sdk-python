# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GitlabBotMergeRequestCommentFilters"]


class GitlabBotMergeRequestCommentFilters(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the comment is in one of the repositories"""

    bot_usernames: Optional[List[str]] = FieldInfo(alias="botUsernames", default=None)
    """Only trigger if the comment is from one of these bot usernames"""
