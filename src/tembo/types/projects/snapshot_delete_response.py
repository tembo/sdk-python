# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SnapshotDeleteResponse"]


class SnapshotDeleteResponse(BaseModel):
    cleanup_job_count: int = FieldInfo(alias="cleanupJobCount")

    deleted: Literal[True]

    id: str
