# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserDeleteResponse"]


class UserDeleteResponse(BaseModel):
    deletion_job_id: str = FieldInfo(alias="deletionJobId")

    deletion_queued: Literal[True] = FieldInfo(alias="deletionQueued")

    id: str
