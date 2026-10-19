# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionEventData", "Scope", "Event", "ToolResult"]


class ToolResult(BaseModel):
    status: Literal["running", "completed", "error"]

    output: Optional[str] = None

    exit_code: Optional[float] = FieldInfo(alias="exitCode", default=None)

    error: Optional[str] = None


class Event(BaseModel):
    event: str

    message: str

    provider: Optional[str] = None

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)


class Scope(BaseModel):
    kind: Literal["foreground", "subagent", "background"]

    parent_tool_use_id: Optional[str] = FieldInfo(alias="parentToolUseId", default=None)

    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)


class SessionEventData(BaseModel):
    type: str

    scope: Optional[Scope] = None

    source: Optional[str] = None

    provider_event: Optional[bool] = FieldInfo(alias="providerEvent", default=None)

    delivery: Optional[Literal["realtime", "persist"]] = None

    event: Optional[Event] = None

    index: Optional[int] = None

    item_id: Optional[str] = FieldInfo(alias="itemId", default=None)

    sequence_number: Optional[int] = FieldInfo(alias="sequenceNumber", default=None)

    accumulated_text: Optional[str] = FieldInfo(alias="accumulatedText", default=None)

    delta_type: Optional[Literal["text_delta", "input_json_delta"]] = FieldInfo(alias="deltaType", default=None)

    response_phase: Optional[Literal["commentary", "final_answer"]] = FieldInfo(alias="responsePhase", default=None)

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)

    tool_result: Optional[ToolResult] = FieldInfo(alias="toolResult", default=None)

    snapshot_id: Optional[str] = FieldInfo(alias="snapshotId", default=None)

    snapshot_created_at: Optional[str] = FieldInfo(alias="snapshotCreatedAt", default=None)
