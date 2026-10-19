# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContentRevisionRestoreParams"]


class ContentRevisionRestoreParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    expected_content_version: Required[Annotated[int, PropertyInfo(alias="expectedContentVersion")]]
    """The agent’s current instruction version, used to reject a restore if the instructions have changed."""
