# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["SessionCreateParams", "AgentOptions", "AgentOptionsGoal", "RichContent", "RichContentMark"]


class SessionCreateParams(TypedDict, total=False):
    agent: str
    """Agent and model key to run, such as claudeCode:claude-fable-5-1. Omit to use the default."""

    base_branch: Annotated[Optional[str], PropertyInfo(alias="baseBranch")]
    """Git branch to start work from. Omit or use null for the repository default."""

    mcp_servers: Annotated[SequenceNotStr[str], PropertyInfo(alias="mcpServers")]
    """MCP server or connection IDs to enable for the session."""

    project_id: Annotated[Optional[str], PropertyInfo(alias="projectId")]
    """Project environment to use for the workspace. Omit or use null for the default."""

    sandbox_size: Annotated[
        Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"], PropertyInfo(alias="sandboxSize")
    ]
    """VM size for the session workspace."""

    target_branch: Annotated[Optional[str], PropertyInfo(alias="targetBranch")]
    """Default target branch for pull requests created by the session."""

    visibility: Literal["private", "public"]
    """Session visibility: private or visible to workspace (public)."""

    agent_options: Annotated[AgentOptions, PropertyInfo(alias="agentOptions")]
    """Agent-specific runtime options, such as reasoning effort."""

    branch_name: Annotated[Optional[str], PropertyInfo(alias="branchName")]
    """Git branch for this session. Omit or use null to generate a branch name."""

    code_repository_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="codeRepositoryIds")]
    """Repository IDs to make available in the session workspace."""

    description: Required[str]
    """Initial task or prompt for the session."""

    id: str
    """Optional caller-supplied session UUID. Omit to generate one."""

    rich_content: Annotated[RichContent, PropertyInfo(alias="richContent")]
    """Optional rich-text representation of the initial task. Provide description separately."""

    pull_request_id: Annotated[str, PropertyInfo(alias="pullRequestId")]
    """Pull request to associate with the session. Requires richContent."""

    queue_right_away: Annotated[bool, PropertyInfo(alias="queueRightAway")]
    """Whether to queue the initial task immediately instead of only creating the session."""

    automatic_sizing: Annotated[bool, PropertyInfo(alias="automaticSizing")]
    """Size the VM automatically. Only for sessions created without a project (projectId "tembo")."""

    session_mode: Annotated[Literal["chat", "terminal"], PropertyInfo(alias="sessionMode")]
    """Whether to create a chat session or a terminal session."""

    startup_agent: Annotated[
        Literal["claudeCode", "codex", "opencode", "pi", "amp", "cursor"], PropertyInfo(alias="startupAgent")
    ]
    """Coding agent to start in a terminal session."""


class RichContentMark(TypedDict, total=False):
    type: Required[str]

    attrs: Dict[str, object]


class RichContent(TypedDict, total=False):
    type: str

    text: str

    attrs: Dict[str, object]

    marks: Iterable[RichContentMark]

    content: Iterable["SessionDocumentNodeParam"]


class AgentOptionsGoal(TypedDict, total=False):
    enabled: bool

    objective: str


class AgentOptions(TypedDict, total=False):
    reasoning_level: Annotated[str, PropertyInfo(alias="reasoningLevel")]

    mode: Literal["normal", "planning"]
    """Use Build (normal) to execute work or Plan (planning) to plan before writing code."""

    speed: Literal["normal", "fast", "ultrafast"]
    """Preferred execution speed when supported by the selected runtime."""

    goal: AgentOptionsGoal

    ultracode: bool
    """Whether the agent orchestrates multi-agent workflows for every task when supported by the selected runtime and model."""


from .session_document_node_param import SessionDocumentNodeParam
from .tip_tap_document_param import TipTapDocumentParam
from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_code_block_node_param import TipTapCodeBlockNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
