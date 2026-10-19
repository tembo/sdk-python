# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .agent_options_input_param import AgentOptionsInputParam

__all__ = ["MessageCreateParams", "SlashCommand"]


class MessageCreateParams(TypedDict, total=False):
    artifact_id: Annotated[str, PropertyInfo(alias="artifactId")]
    """Artifact to associate with this message."""

    content: Required[str]
    """Text of the task, follow-up, or steering instruction to send to the session agent."""

    mcp_servers: Annotated[SequenceNotStr[str], PropertyInfo(alias="mcpServers")]
    """MCP server or connection IDs selected for this message."""

    pull_request_id: Annotated[str, PropertyInfo(alias="pullRequestId")]
    """Pull request to associate with this message."""

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """Session to receive this message. Use this operation to continue work in an existing session."""

    agent_options: Annotated[AgentOptionsInputParam, PropertyInfo(alias="agentOptions")]
    """Agent-specific runtime options for this message, such as reasoning effort."""

    delivery_mode: Annotated[Literal["queue", "steer"], PropertyInfo(alias="deliveryMode")]
    """queue adds a follow-up task; steer sends guidance to an active agent turn when supported."""

    rich_content: Annotated["TipTapDocumentParam", PropertyInfo(alias="richContent")]
    """Optional rich-text representation of the message. Provide the required text content separately."""

    slash_command: Annotated[SlashCommand, PropertyInfo(alias="slashCommand")]
    """Structured slash command to execute with this message."""


class SlashCommand(TypedDict, total=False):
    command: Required[str]

    arguments: str


from .tip_tap_document_param import TipTapDocumentParam
from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_code_block_node_param import TipTapCodeBlockNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
