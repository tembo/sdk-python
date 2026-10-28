# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BillingListUsageResponse", "Item", "Item2", "Item3"]


class Item3(BaseModel):
    id: str

    virtual_machine_id: str = FieldInfo(alias="virtualMachineId")

    started_at: datetime = FieldInfo(alias="startedAt")

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)

    runtime_ms: float = FieldInfo(alias="runtimeMs")

    cpu: float

    memory_mb: float = FieldInfo(alias="memoryMb")

    compute_credits: float = FieldInfo(alias="computeCredits")

    type: Literal["warm-pool"]


class Item2(BaseModel):
    agent: Optional[str] = None

    id: str

    title: str

    kind: str

    created_at: datetime = FieldInfo(alias="createdAt")

    managed_inference_credits: float = FieldInfo(alias="managedInferenceCredits")

    compute_credits: float = FieldInfo(alias="computeCredits")

    total_credits: float = FieldInfo(alias="totalCredits")

    type: Literal["session"]


Item: TypeAlias = Union[Item2, Item3]


class BillingListUsageResponse(BaseModel):
    items: List[Item]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    as_of: datetime = FieldInfo(alias="asOf")
