# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    agent: str
    """The agent to use for this task"""

    branch_name: Annotated[Optional[str], PropertyInfo(alias="branchName")]
    """The branch name to use for the work"""

    prompt: str
    """Description of the task to be performed. Supports tagging files."""

    queue_right_away: Annotated[Optional[bool], PropertyInfo(alias="queueRightAway")]
    """
    Whether to immediately queue the task for processing (optional, defaults to
    true)
    """

    repositories: SequenceNotStr[str]
    """Array of code repository urls that this task relates to"""

    target_branch: Annotated[Optional[str], PropertyInfo(alias="targetBranch")]
    """The branch to open the pull request against (e.g. main, develop)"""
