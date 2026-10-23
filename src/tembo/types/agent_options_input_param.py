# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Annotated, Literal, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentOptionsInputParam", "Variant", "VariantGoal"]


class VariantGoal(TypedDict, total=False):
    enabled: bool

    objective: str


class Variant(TypedDict, total=False):
    reasoning_level: Annotated[str, PropertyInfo(alias="reasoningLevel")]

    mode: Literal["normal", "planning"]
    """Use Build (normal) to execute work or Plan (planning) to plan before writing code."""

    speed: Literal["normal", "fast", "ultrafast"]
    """Preferred execution speed when supported by the selected runtime."""

    goal: VariantGoal

    ultracode: bool
    """Whether the agent orchestrates multi-agent workflows for every task when supported by the selected runtime and model."""


AgentOptionsInputParam: TypeAlias = Union[Variant, Dict[str, object]]
