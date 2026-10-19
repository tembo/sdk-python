# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional, TYPE_CHECKING, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentOptionsInput", "AgentOptionsInput2", "AgentOptionsInput2Goal"]


class AgentOptionsInput2Goal(BaseModel):
    enabled: Optional[bool] = None

    objective: Optional[str] = None


class AgentOptionsInput2(BaseModel):
    reasoningLevel: Optional[str] = None

    mode: Optional[Literal["normal", "planning"]] = None
    """Use Build (normal) to execute work or Plan (planning) to plan before writing code."""

    speed: Optional[Literal["normal", "fast", "ultrafast"]] = None
    """Preferred execution speed when supported by the selected runtime."""

    goal: Optional[AgentOptionsInput2Goal] = None

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


AgentOptionsInput: TypeAlias = Union[AgentOptionsInput2, Dict[str, object]]
