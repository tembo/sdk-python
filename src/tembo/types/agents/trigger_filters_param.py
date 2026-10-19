# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Annotated, Literal, TypeAlias, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = [
    "TriggerFiltersParam",
    "Variant",
    "Variant2",
    "Variant3",
    "Variant4",
    "Variant5",
    "Variant6",
    "Variant7",
    "Variant8",
    "Variant9",
    "Variant10",
    "Variant11",
    "Variant12",
    "Variant13",
    "Variant14",
    "Variant15",
    "Variant16",
    "Variant17",
    "Variant18",
    "Variant19",
    "Variant20",
    "Variant21",
    "Variant22",
    "Variant23",
    "Variant24",
    "Variant25",
    "Variant26",
    "Variant27",
    "Variant28",
    "Variant29",
    "Variant30",
    "Variant31",
    "Variant32",
    "Variant33",
    "Variant34",
    "Variant35",
    "Variant36",
    "Variant37",
    "Variant38",
    "Variant39",
    "Variant40",
    "Variant41",
    "Variant42",
]


class Variant42(TypedDict, total=False):
    spaces: SequenceNotStr[str]
    """Only trigger if the page is in a space with one of these names or IDs"""

    title_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="titleContains")]
    """Only trigger if the page title contains one of these substrings"""

    labels: SequenceNotStr[str]
    """Only trigger if the removed label has one of these values"""

    comment_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="commentContains")]
    """Only trigger if the comment contains one of these substrings"""


class Variant41(TypedDict, total=False):
    spaces: SequenceNotStr[str]
    """Only trigger if the page is in a space with one of these names or IDs"""

    title_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="titleContains")]
    """Only trigger if the page title contains one of these substrings"""

    labels: SequenceNotStr[str]
    """Only trigger if the added label has one of these values"""

    comment_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="commentContains")]
    """Only trigger if the comment contains one of these substrings"""


class Variant40(TypedDict, total=False):
    spaces: SequenceNotStr[str]
    """Only trigger if the page is in a space with one of these names or IDs"""

    title_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="titleContains")]
    """Only trigger if the page title contains one of these substrings"""

    locations: List[Literal["footer", "inline"]]
    """Only trigger for footer comments, inline comments, or both"""


class Variant39(TypedDict, total=False):
    spaces: SequenceNotStr[str]
    """Only trigger if the page is in a space with one of these names or IDs"""

    title_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="titleContains")]
    """Only trigger if the page title contains one of these substrings"""

    previous_spaces: Annotated[SequenceNotStr[str], PropertyInfo(alias="previousSpaces")]
    """Only trigger if the page was moved from a space with one of these names or IDs"""


class Variant38(TypedDict, total=False):
    spaces: SequenceNotStr[str]
    """Only trigger if the page is in a space with one of these names or IDs"""

    title_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="titleContains")]
    """Only trigger if the page title contains one of these substrings"""


class Variant37(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """Only trigger if the message is sent in one of the channels"""

    users: SequenceNotStr[str]
    """Only trigger if the message was sent by one of these user names"""

    message_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="messageContains")]
    """Only trigger if the message contains one of these substrings"""

    message_not_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="messageNotContains")]
    """Skip messages containing any of these case-sensitive substrings (for example, On-call handover:)"""


class Variant36(TypedDict, total=False):
    emojis: SequenceNotStr[str]
    """Only trigger if one of these emoji reactions is added"""

    channels: SequenceNotStr[str]
    """Only trigger if the reaction is added in one of these channels"""

    users: SequenceNotStr[str]
    """Only trigger if the reaction is added by one of these user names"""


class Variant35(TypedDict, total=False):
    priorities: List[Literal["high", "medium", "low"]]
    """Only trigger if the issue has one of the specified priorities"""

    project_slugs: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectSlugs")]
    """Only trigger if the issue is in one of the specified projects"""


class Variant34(TypedDict, total=False):
    teams: SequenceNotStr[str]
    """Only trigger if the issue belongs to one of the specified teams"""

    states: SequenceNotStr[str]
    """Only trigger if the issue state type matches one of the specified types"""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""

    tembo_issues: Annotated[bool, PropertyInfo(alias="temboIssues")]
    """Enable agent for Tembo-updated issues (disabled by default)"""


class Variant33(TypedDict, total=False):
    teams: SequenceNotStr[str]
    """Only trigger if the issue belongs to one of the specified teams"""

    statuses: SequenceNotStr[str]
    """Only trigger if the issue was moved to one of the specified statuses"""

    previous_statuses: Annotated[SequenceNotStr[str], PropertyInfo(alias="previousStatuses")]
    """Only trigger when the issue changes from one of the specified previous statuses."""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""


class Variant32(TypedDict, total=False):
    teams: SequenceNotStr[str]
    """Only trigger if the issue belongs to one of the specified teams"""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if one of the specified labels was added to the issue"""


class Variant31(TypedDict, total=False):
    teams: SequenceNotStr[str]
    """Only trigger if the issue belongs to one of the specified teams"""

    states: SequenceNotStr[str]
    """Only trigger if the issue state type matches one of the specified types"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the issue was opened by one of the specified users"""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""

    tembo_issues: Annotated[bool, PropertyInfo(alias="temboIssues")]
    """Enable agent for Tembo-created issues (disabled by default)"""


class Variant30(TypedDict, total=False):
    repositories: SequenceNotStr[str]

    ref_type: Annotated[List[Literal["branch", "tag"]], PropertyInfo(alias="refType")]
    """Only trigger for the specified Git reference type: branch or tag."""

    branch_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="branchNames")]

    tag_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="tagNames")]


class Variant29(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pipeline is in one of the repositories"""

    branches: SequenceNotStr[str]
    """Only trigger for specific branches"""


class Variant28(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the merge request is in one of the repositories"""

    pushed_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="pushedBy")]
    """Only trigger if the commits were pushed by one of the specified users"""

    draft_mrs: Annotated[bool, PropertyInfo(alias="draftMrs")]
    """Include draft merge requests. Drafts are excluded when omitted or false."""

    tembo_mrs: Annotated[bool, PropertyInfo(alias="temboMrs")]
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class Variant27(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the merge request is in one of the repositories"""

    draft_mrs: Annotated[bool, PropertyInfo(alias="draftMrs")]
    """Include draft merge requests. Drafts are excluded when omitted or false."""

    tembo_mrs: Annotated[bool, PropertyInfo(alias="temboMrs")]
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class Variant26(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the merge request is in one of the repositories"""

    merged_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergedBy")]
    """Only trigger if the merge request was merged by one of the specified users"""

    tembo_mrs: Annotated[bool, PropertyInfo(alias="temboMrs")]
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class Variant25(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the merge request is in one of the repositories"""

    closed_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="closedBy")]
    """Only trigger if the merge request was closed by one of the specified users"""

    tembo_mrs: Annotated[bool, PropertyInfo(alias="temboMrs")]
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class Variant24(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the issue is in one of the repositories"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the issue was opened by one of the specified users"""

    tembo_issues: Annotated[bool, PropertyInfo(alias="temboIssues")]
    """Enable agent for Tembo-created issues (disabled by default)"""


class Variant23(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the issue is in one of the repositories"""

    closed_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="closedBy")]
    """Only trigger if the issue was closed by one of the specified users"""

    tembo_issues: Annotated[bool, PropertyInfo(alias="temboIssues")]
    """Enable agent for Tembo-created issues (disabled by default)"""


class Variant22(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the comment is in one of the repositories"""

    bot_usernames: Annotated[SequenceNotStr[str], PropertyInfo(alias="botUsernames")]
    """Only trigger if the comment is from one of these bot usernames"""


class Variant21(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the workflow run is in one of the repositories"""

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
    """Only trigger for specific workflow names"""

    branches: SequenceNotStr[str]
    """Only trigger for specific branches"""

    conclusions: List[
        Literal["success", "failure", "neutral", "cancelled", "timed_out", "action_required", "stale", "skipped"]
    ]
    """Only trigger for these completed workflow results, such as success"""

    events: SequenceNotStr[str]
    """Only trigger for these originating GitHub events; use schedule for cron runs, not push or pull_request"""


class Variant20(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the workflow run is in one of the repositories"""

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
    """Only trigger for specific workflow names"""

    branches: SequenceNotStr[str]
    """Only trigger for specific branches"""


class Variant19(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pull request is in one of the repositories"""

    draft_prs: Annotated[bool, PropertyInfo(alias="draftPrs")]
    """Also trigger for draft pull requests"""


class Variant18(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pull request is in one of the repositories"""

    pushed_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="pushedBy")]
    """Only trigger if the commits were pushed by one of the specified users"""

    draft_prs: Annotated[bool, PropertyInfo(alias="draftPrs")]
    """Trigger even if the pull request is a draft"""

    tembo_prs: Annotated[bool, PropertyInfo(alias="temboPrs")]
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class Variant17(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the release is in one of the repositories"""


class Variant16(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pull request is in one of the repositories"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the pull request was opened by one of the specified users"""

    tembo_prs: Annotated[bool, PropertyInfo(alias="temboPrs")]
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class Variant15(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pull request is in one of the repositories"""

    labels: SequenceNotStr[str]
    """Only trigger if the pull request has at least one of the specified labels"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the pull request was opened by one of the specified users"""

    branches: SequenceNotStr[str]
    """Only trigger if the pull request targets one of these branches"""

    draft_prs: Annotated[bool, PropertyInfo(alias="draftPrs")]
    """Trigger also for draft pull requests (disabled by default)"""

    tembo_prs: Annotated[bool, PropertyInfo(alias="temboPrs")]
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class Variant14(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pull request is in one of the repositories"""

    merged_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="mergedBy")]
    """Only trigger if the pull request was merged by one of the specified users"""

    tembo_prs: Annotated[bool, PropertyInfo(alias="temboPrs")]
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class Variant13(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pull request is in one of the repositories"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the pull request was opened by one of the specified users"""

    tembo_prs: Annotated[bool, PropertyInfo(alias="temboPrs")]
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class Variant12(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the issue is in one of the repositories"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the issue was opened by one of the specified users"""

    tembo_issues: Annotated[bool, PropertyInfo(alias="temboIssues")]
    """Enable agent for Tembo-created issues (disabled by default)"""


class Variant11(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the comment is in one of the repositories"""

    commented_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="commentedBy")]
    """Only trigger if the comment was created by one of the specified users"""

    comment_on: Annotated[List[Literal["issues", "pull_requests"]], PropertyInfo(alias="commentOn")]
    """Trigger on comments on issues, pull requests, or both"""

    message_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="messageContains")]
    """Only trigger if the comment contains one of these substrings"""


class Variant10(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the issue is in one of the repositories"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the issue was opened by one of the specified users"""

    tembo_issues: Annotated[bool, PropertyInfo(alias="temboIssues")]
    """Enable agent for Tembo-created issues (disabled by default)"""


class Variant9(TypedDict, total=False):
    repositories: SequenceNotStr[str]

    ref_type: Annotated[List[Literal["branch", "tag"]], PropertyInfo(alias="refType")]
    """Only trigger for the specified Git reference type: branch or tag."""

    branch_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="branchNames")]

    tag_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="tagNames")]


class Variant8(TypedDict, total=False):
    repositories: SequenceNotStr[str]
    """Only trigger if the pull request is in one of the repositories"""

    opened_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="openedBy")]
    """Only trigger if the pull request was opened by one of the specified users"""

    tembo_prs: Annotated[bool, PropertyInfo(alias="temboPrs")]
    """Enable agent for Tembo-created pull requests (disabled by default)"""


class Variant7(TypedDict, total=False):
    projects: SequenceNotStr[str]
    """Only trigger if the issue is in one of the specified projects"""

    issue_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="issueTypes")]
    """Only trigger for the specified issue types, such as Story, Bug, or Sub-task."""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""


class Variant6(TypedDict, total=False):
    projects: SequenceNotStr[str]
    """Only trigger if the issue is in one of the specified projects"""

    statuses: SequenceNotStr[str]
    """Only trigger if the issue was moved to one of the specified statuses"""

    previous_statuses: Annotated[SequenceNotStr[str], PropertyInfo(alias="previousStatuses")]
    """Only trigger when the issue changes from one of the specified previous statuses."""

    issue_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="issueTypes")]
    """Only trigger for the specified issue types, such as Story, Bug, or Sub-task."""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""


class Variant5(TypedDict, total=False):
    projects: SequenceNotStr[str]
    """Only trigger if the issue is in one of the specified projects"""

    teams: SequenceNotStr[str]
    """Only trigger if the issue belongs to one of these Jira teams. Enter exact team names or team IDs (from the team profile URL)."""

    labels: SequenceNotStr[str]
    """Only trigger if one of the specified labels was added"""


class Variant4(TypedDict, total=False):
    projects: SequenceNotStr[str]
    """Only trigger if the issue is in one of the specified projects"""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    issue_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="issueTypes")]
    """Only trigger for the specified issue types, such as Story, Bug, or Sub-task."""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""


class Variant3(TypedDict, total=False):
    projects: SequenceNotStr[str]
    """Only trigger if the issue is in one of the specified projects"""

    commented_by: Annotated[SequenceNotStr[str], PropertyInfo(alias="commentedBy")]
    """Only trigger if the comment was added by one of the specified users"""

    message_contains: Annotated[SequenceNotStr[str], PropertyInfo(alias="messageContains")]
    """Only trigger if the comment contains one of these substrings"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""


class Variant2(TypedDict, total=False):
    projects: SequenceNotStr[str]
    """Only trigger if the issue is in one of the specified projects"""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""

    include_new_issues: Annotated[bool, PropertyInfo(alias="includeNewIssues")]
    """Also trigger for newly created issues that are already assigned"""


class Variant(TypedDict, total=False):
    projects: SequenceNotStr[str]
    """Only trigger if the issue is in one of the specified projects"""

    boards: SequenceNotStr[str]
    """Only trigger if the issue is on one of the specified boards"""

    statuses: SequenceNotStr[str]
    """Only trigger if the issue was moved to one of the specified statuses (board columns)"""

    assigned_to: Annotated[SequenceNotStr[str], PropertyInfo(alias="assignedTo")]
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: SequenceNotStr[str]
    """Only trigger if the issue has at least one of the specified labels"""

    include_new_issues: Annotated[bool, PropertyInfo(alias="includeNewIssues")]
    """Also trigger for newly created issues (not just status changes)"""


TriggerFiltersParam: TypeAlias = Union[
    Variant,
    Variant2,
    Variant3,
    Variant4,
    Variant5,
    Variant6,
    Variant7,
    Variant8,
    Variant9,
    Variant10,
    Variant11,
    Variant12,
    Variant13,
    Variant14,
    Variant15,
    Variant16,
    Variant17,
    Variant18,
    Variant19,
    Variant20,
    Variant21,
    Variant22,
    Variant23,
    Variant24,
    Variant25,
    Variant26,
    Variant27,
    Variant28,
    Variant29,
    Variant30,
    Variant31,
    Variant32,
    Variant33,
    Variant34,
    Variant35,
    Variant36,
    Variant37,
    Variant38,
    Variant39,
    Variant40,
    Variant41,
    Variant42,
    object,
]
