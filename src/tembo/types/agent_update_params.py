# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .agent_options_input_param import AgentOptionsInputParam
from .agent_state import AgentState

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    expected_updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="expectedUpdatedAt", format="iso8601")]
    """Value of updatedAt from the last retrieved agent. A concurrent change causes a conflict instead of overwriting newer changes."""

    name: str
    """Rename the agent."""

    key: Optional[str]
    """Change the agent lookup key, or null to clear it."""

    instructions: Optional["TipTapDocumentParam"]
    """Replace the agent instruction document, or null to clear it."""

    mcp_servers: Annotated[SequenceNotStr[str], PropertyInfo(alias="mcpServers")]
    """Replace the MCP server or connection IDs. An empty array clears the selection."""

    agent: Optional[str]
    """Change the coding agent and model key. Null clears the override."""

    agent_options: Annotated[AgentOptionsInputParam, PropertyInfo(alias="agentOptions")]
    """Change agent-specific runtime options, such as reasoning effort."""

    user_state: Annotated[AgentState, PropertyInfo(alias="userState")]
    """Replace the user-managed persistent agent state."""

    sandbox_size: Annotated[
        Optional[Literal["nano", "micro", "small", "medium", "large", "xl", "xxl", "ultra"]],
        PropertyInfo(alias="sandboxSize"),
    ]
    """Change the workspace VM size. Null clears the override."""

    project_id: Annotated[Optional[Union[str, Literal["tembo"]]], PropertyInfo(alias="projectId")]
    """Change the project environment for runs. Null clears the override."""

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]
    """Change the associated agent template identifier, or null to clear it."""

    script: Optional[str]
    """Replace the agent script, or null to clear it."""

    artifact_type: Annotated[
        Optional[Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]],
        PropertyInfo(alias="artifactType"),
    ]
    """Change the artifact type produced by the agent, or null to clear it."""

    repository_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="repositoryIds")]
    """Replace repository associations. An empty array removes all associations."""

    enabled: bool
    """Enable or pause the agent and its schedules and triggers. Archived agents remain paused until restored."""

    archived: bool
    """Archive with true or restore with false. Archiving disables schedules and triggers; restoring follows the agent enabled state."""


from .tip_tap_document_param import TipTapDocumentParam
from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_code_block_node_param import TipTapCodeBlockNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
