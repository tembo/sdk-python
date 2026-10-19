# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TriggerFilters",
    "TriggerFilters2",
    "TriggerFilters3",
    "TriggerFilters4",
    "TriggerFilters5",
    "TriggerFilters6",
    "TriggerFilters7",
    "TriggerFilters8",
    "TriggerFilters9",
    "TriggerFilters10",
    "TriggerFilters11",
    "TriggerFilters12",
    "TriggerFilters13",
    "TriggerFilters14",
    "TriggerFilters15",
    "TriggerFilters16",
    "TriggerFilters17",
    "TriggerFilters18",
    "TriggerFilters19",
    "TriggerFilters20",
    "TriggerFilters21",
    "TriggerFilters22",
    "TriggerFilters23",
    "TriggerFilters24",
    "TriggerFilters25",
    "TriggerFilters26",
    "TriggerFilters27",
    "TriggerFilters28",
    "TriggerFilters29",
    "TriggerFilters30",
    "TriggerFilters31",
    "TriggerFilters32",
    "TriggerFilters33",
    "TriggerFilters34",
    "TriggerFilters35",
    "TriggerFilters36",
    "TriggerFilters37",
    "TriggerFilters38",
    "TriggerFilters39",
    "TriggerFilters40",
    "TriggerFilters41",
    "TriggerFilters42",
    "TriggerFilters43",
]


class TriggerFilters43(BaseModel):
    spaces: Optional[List[str]] = None
    """Only trigger if the page is in a space with one of these names or IDs"""

    titleContains: Optional[List[str]] = None
    """Only trigger if the page title contains one of these substrings"""

    labels: Optional[List[str]] = None
    """Only trigger if the removed label has one of these values"""

    commentContains: Optional[List[str]] = None
    """Only trigger if the comment contains one of these substrings"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]


class TriggerFilters42(BaseModel):
    spaces: Optional[List[str]] = None
    """Only trigger if the page is in a space with one of these names or IDs"""

    titleContains: Optional[List[str]] = None
    """Only trigger if the page title contains one of these substrings"""

    labels: Optional[List[str]] = None
    """Only trigger if the added label has one of these values"""

    commentContains: Optional[List[str]] = None
    """Only trigger if the comment contains one of these substrings"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]


class TriggerFilters41(BaseModel):
    spaces: Optional[List[str]] = None
    """Only trigger if the page is in a space with one of these names or IDs"""

    titleContains: Optional[List[str]] = None
    """Only trigger if the page title contains one of these substrings"""

    locations: Optional[List[Literal["footer", "inline"]]] = None
    """Only trigger for footer comments, inline comments, or both"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]


class TriggerFilters40(BaseModel):
    spaces: Optional[List[str]] = None
    """Only trigger if the page is in a space with one of these names or IDs"""

    titleContains: Optional[List[str]] = None
    """Only trigger if the page title contains one of these substrings"""

    previousSpaces: Optional[List[str]] = None
    """Only trigger if the page was moved from a space with one of these names or IDs"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]


class TriggerFilters39(BaseModel):
    spaces: Optional[List[str]] = None
    """Only trigger if the page is in a space with one of these names or IDs"""

    titleContains: Optional[List[str]] = None
    """Only trigger if the page title contains one of these substrings"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...

    else:
        __pydantic_extra__: Dict[str, object]


class TriggerFilters38(BaseModel):
    channels: Optional[List[str]] = None
    """Only trigger if the message is sent in one of the channels"""

    users: Optional[List[str]] = None
    """Only trigger if the message was sent by one of these user names"""

    messageContains: Optional[List[str]] = None
    """Only trigger if the message contains one of these substrings"""

    messageNotContains: Optional[List[str]] = None
    """Skip messages containing any of these case-sensitive substrings (for example, On-call handover:)"""


class TriggerFilters37(BaseModel):
    emojis: Optional[List[str]] = None
    """Only trigger if one of these emoji reactions is added"""

    channels: Optional[List[str]] = None
    """Only trigger if the reaction is added in one of these channels"""

    users: Optional[List[str]] = None
    """Only trigger if the reaction is added by one of these user names"""


class TriggerFilters36(BaseModel):
    priorities: Optional[List[Literal["high", "medium", "low"]]] = None
    """Only trigger if the issue has one of the specified priorities"""

    projectSlugs: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""


class TriggerFilters35(BaseModel):
    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of the specified teams"""

    states: Optional[List[str]] = None
    """Only trigger if the issue state type matches one of the specified types"""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""

    temboIssues: Optional[bool] = None
    """Enable agent for Tembo-updated issues (disabled by default)"""


class TriggerFilters34(BaseModel):
    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of the specified teams"""

    statuses: Optional[List[str]] = None
    """Only trigger if the issue was moved to one of the specified statuses"""

    previousStatuses: Optional[List[str]] = None
    """Only trigger when the issue changes from one of the specified previous statuses."""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""


class TriggerFilters33(BaseModel):
    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of the specified teams"""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if one of the specified labels was added to the issue"""


class TriggerFilters32(BaseModel):
    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of the specified teams"""

    states: Optional[List[str]] = None
    """Only trigger if the issue state type matches one of the specified types"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the issue was opened by one of the specified users"""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""

    temboIssues: Optional[bool] = None
    """Enable agent for Tembo-created issues (disabled by default)"""


class TriggerFilters31(BaseModel):
    repositories: Optional[List[str]] = None

    refType: Optional[List[Literal["branch", "tag"]]] = None
    """Only trigger for the specified Git reference type: branch or tag."""

    branchNames: Optional[List[str]] = None

    tagNames: Optional[List[str]] = None


class TriggerFilters30(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pipeline is in one of the repositories"""

    branches: Optional[List[str]] = None
    """Only trigger for specific branches"""


class TriggerFilters29(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the merge request is in one of the repositories"""

    pushedBy: Optional[List[str]] = None
    """Only trigger if the commits were pushed by one of the specified users"""

    draftMrs: Optional[bool] = None
    """Include draft merge requests. Drafts are excluded when omitted or false."""

    temboMrs: Optional[bool] = None
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class TriggerFilters28(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the merge request is in one of the repositories"""

    draftMrs: Optional[bool] = None
    """Include draft merge requests. Drafts are excluded when omitted or false."""

    temboMrs: Optional[bool] = None
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class TriggerFilters27(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the merge request is in one of the repositories"""

    mergedBy: Optional[List[str]] = None
    """Only trigger if the merge request was merged by one of the specified users"""

    temboMrs: Optional[bool] = None
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class TriggerFilters26(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the merge request is in one of the repositories"""

    closedBy: Optional[List[str]] = None
    """Only trigger if the merge request was closed by one of the specified users"""

    temboMrs: Optional[bool] = None
    """Enable agent for Tembo-created merge requests (disabled by default)"""


class TriggerFilters25(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the issue is in one of the repositories"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the issue was opened by one of the specified users"""

    temboIssues: Optional[bool] = None
    """Enable agent for Tembo-created issues (disabled by default)"""


class TriggerFilters24(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the issue is in one of the repositories"""

    closedBy: Optional[List[str]] = None
    """Only trigger if the issue was closed by one of the specified users"""

    temboIssues: Optional[bool] = None
    """Enable agent for Tembo-created issues (disabled by default)"""


class TriggerFilters23(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the comment is in one of the repositories"""

    botUsernames: Optional[List[str]] = None
    """Only trigger if the comment is from one of these bot usernames"""


class TriggerFilters22(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the workflow run is in one of the repositories"""

    workflowNames: Optional[List[str]] = None
    """Only trigger for specific workflow names"""

    branches: Optional[List[str]] = None
    """Only trigger for specific branches"""

    conclusions: Optional[
        List[Literal["success", "failure", "neutral", "cancelled", "timed_out", "action_required", "stale", "skipped"]]
    ] = None
    """Only trigger for these completed workflow results, such as success"""

    events: Optional[List[str]] = None
    """Only trigger for these originating GitHub events; use schedule for cron runs, not push or pull_request"""


class TriggerFilters21(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the workflow run is in one of the repositories"""

    workflowNames: Optional[List[str]] = None
    """Only trigger for specific workflow names"""

    branches: Optional[List[str]] = None
    """Only trigger for specific branches"""


class TriggerFilters20(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    draftPrs: Optional[bool] = None
    """Also trigger for draft pull requests"""


class TriggerFilters19(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    pushedBy: Optional[List[str]] = None
    """Only trigger if the commits were pushed by one of the specified users"""

    draftPrs: Optional[bool] = None
    """Trigger even if the pull request is a draft"""

    temboPrs: Optional[bool] = None
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class TriggerFilters18(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the release is in one of the repositories"""


class TriggerFilters17(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the pull request was opened by one of the specified users"""

    temboPrs: Optional[bool] = None
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class TriggerFilters16(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    labels: Optional[List[str]] = None
    """Only trigger if the pull request has at least one of the specified labels"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the pull request was opened by one of the specified users"""

    branches: Optional[List[str]] = None
    """Only trigger if the pull request targets one of these branches"""

    draftPrs: Optional[bool] = None
    """Trigger also for draft pull requests (disabled by default)"""

    temboPrs: Optional[bool] = None
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class TriggerFilters15(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    mergedBy: Optional[List[str]] = None
    """Only trigger if the pull request was merged by one of the specified users"""

    temboPrs: Optional[bool] = None
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class TriggerFilters14(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the pull request was opened by one of the specified users"""

    temboPrs: Optional[bool] = None
    """Enable agent for Tembo-created pull requests (enabled by default)"""


class TriggerFilters13(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the issue is in one of the repositories"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the issue was opened by one of the specified users"""

    temboIssues: Optional[bool] = None
    """Enable agent for Tembo-created issues (disabled by default)"""


class TriggerFilters12(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the comment is in one of the repositories"""

    commentedBy: Optional[List[str]] = None
    """Only trigger if the comment was created by one of the specified users"""

    commentOn: Optional[List[Literal["issues", "pull_requests"]]] = None
    """Trigger on comments on issues, pull requests, or both"""

    messageContains: Optional[List[str]] = None
    """Only trigger if the comment contains one of these substrings"""


class TriggerFilters11(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the issue is in one of the repositories"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the issue was opened by one of the specified users"""

    temboIssues: Optional[bool] = None
    """Enable agent for Tembo-created issues (disabled by default)"""


class TriggerFilters10(BaseModel):
    repositories: Optional[List[str]] = None

    refType: Optional[List[Literal["branch", "tag"]]] = None
    """Only trigger for the specified Git reference type: branch or tag."""

    branchNames: Optional[List[str]] = None

    tagNames: Optional[List[str]] = None


class TriggerFilters9(BaseModel):
    repositories: Optional[List[str]] = None
    """Only trigger if the pull request is in one of the repositories"""

    openedBy: Optional[List[str]] = None
    """Only trigger if the pull request was opened by one of the specified users"""

    temboPrs: Optional[bool] = None
    """Enable agent for Tembo-created pull requests (disabled by default)"""


class TriggerFilters8(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    issueTypes: Optional[List[str]] = None
    """Only trigger for the specified issue types, such as Story, Bug, or Sub-task."""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""


class TriggerFilters7(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    statuses: Optional[List[str]] = None
    """Only trigger if the issue was moved to one of the specified statuses"""

    previousStatuses: Optional[List[str]] = None
    """Only trigger when the issue changes from one of the specified previous statuses."""

    issueTypes: Optional[List[str]] = None
    """Only trigger for the specified issue types, such as Story, Bug, or Sub-task."""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""


class TriggerFilters6(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    teams: Optional[List[str]] = None
    """Only trigger if the issue belongs to one of these Jira teams. Enter exact team names or team IDs (from the team profile URL)."""

    labels: Optional[List[str]] = None
    """Only trigger if one of the specified labels was added"""


class TriggerFilters5(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    issueTypes: Optional[List[str]] = None
    """Only trigger for the specified issue types, such as Story, Bug, or Sub-task."""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""


class TriggerFilters4(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    commentedBy: Optional[List[str]] = None
    """Only trigger if the comment was added by one of the specified users"""

    messageContains: Optional[List[str]] = None
    """Only trigger if the comment contains one of these substrings"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""


class TriggerFilters3(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""

    includeNewIssues: Optional[bool] = None
    """Also trigger for newly created issues that are already assigned"""


class TriggerFilters2(BaseModel):
    projects: Optional[List[str]] = None
    """Only trigger if the issue is in one of the specified projects"""

    boards: Optional[List[str]] = None
    """Only trigger if the issue is on one of the specified boards"""

    statuses: Optional[List[str]] = None
    """Only trigger if the issue was moved to one of the specified statuses (board columns)"""

    assignedTo: Optional[List[str]] = None
    """Only trigger if the issue is assigned to one of the specified users"""

    labels: Optional[List[str]] = None
    """Only trigger if the issue has at least one of the specified labels"""

    includeNewIssues: Optional[bool] = None
    """Also trigger for newly created issues (not just status changes)"""


TriggerFilters: TypeAlias = Union[
    TriggerFilters2,
    TriggerFilters3,
    TriggerFilters4,
    TriggerFilters5,
    TriggerFilters6,
    TriggerFilters7,
    TriggerFilters8,
    TriggerFilters9,
    TriggerFilters10,
    TriggerFilters11,
    TriggerFilters12,
    TriggerFilters13,
    TriggerFilters14,
    TriggerFilters15,
    TriggerFilters16,
    TriggerFilters17,
    TriggerFilters18,
    TriggerFilters19,
    TriggerFilters20,
    TriggerFilters21,
    TriggerFilters22,
    TriggerFilters23,
    TriggerFilters24,
    TriggerFilters25,
    TriggerFilters26,
    TriggerFilters27,
    TriggerFilters28,
    TriggerFilters29,
    TriggerFilters30,
    TriggerFilters31,
    TriggerFilters32,
    TriggerFilters33,
    TriggerFilters34,
    TriggerFilters35,
    TriggerFilters36,
    TriggerFilters37,
    TriggerFilters38,
    TriggerFilters39,
    TriggerFilters40,
    TriggerFilters41,
    TriggerFilters42,
    TriggerFilters43,
    object,
]
