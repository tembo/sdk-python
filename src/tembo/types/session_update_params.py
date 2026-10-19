# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["SessionUpdateParams", "AgentOptions", "AgentOptionsGoal", "RichContent", "RichContentMark"]


class SessionUpdateParams(TypedDict, total=False):
    agent: Optional[str]
    """Change the agent and model key. Null clears the session override."""

    agent_options: Annotated[AgentOptions, PropertyInfo(alias="agentOptions")]
    """Change agent-specific runtime options, such as reasoning effort."""

    base_branch: Annotated[Optional[str], PropertyInfo(alias="baseBranch")]
    """Change the starting Git branch. Null clears the session override."""

    branch_name: Annotated[Optional[str], PropertyInfo(alias="branchName")]
    """Change the session Git branch name. Null clears the stored name."""

    description: str
    """Replace the initial task prompt; only the session creator can change it. Use createMessage to send a follow-up task."""

    rich_content: Annotated[Optional[RichContent], PropertyInfo(alias="richContent")]
    """Replace the initial prompt rich-text document, or null to clear it. Only the session creator can change it."""

    level: int
    """Archive or restore the session and set its priority: 0 archives and stops its VM; 1 restores without restarting work; 2–100 also keep it unarchived and set its priority level. Omit to preserve the current level."""

    mcp_servers: Annotated[SequenceNotStr[str], PropertyInfo(alias="mcpServers")]
    """Replace the enabled MCP server or connection IDs. An empty array clears the selection."""

    mode: Literal["normal", "planning"]
    """Switch between Build (normal) and Plan (planning) modes."""

    project_id: Annotated[Optional[str], PropertyInfo(alias="projectId")]
    """Change the project environment used for the workspace. Null clears the session override."""

    sandbox_size: Annotated[
        Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]],
        PropertyInfo(alias="sandboxSize"),
    ]
    """Change the workspace VM size. Null clears the session override."""

    target_branch: Annotated[Optional[str], PropertyInfo(alias="targetBranch")]
    """Change the default pull request target branch. Null clears the session override."""

    title: str
    """Rename the session."""

    visibility: Literal["private", "public"]
    """Change session visibility: private or visible to workspace (public). Only the session creator can change it."""


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


from .session_document_node_param import SessionDocumentNodeParam
from .tip_tap_document_param import TipTapDocumentParam
from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_code_block_node_param import TipTapCodeBlockNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
