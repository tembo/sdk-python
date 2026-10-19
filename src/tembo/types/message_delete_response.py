# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageDeleteResponse"]


class MessageDeleteResponse(BaseModel):
    cancelled_jobs_count: int = FieldInfo(alias="cancelledJobsCount")

    cancelled_sessions_count: int = FieldInfo(alias="cancelledSessionsCount")

    deleted: Literal[True]

    deleted_jobs_count: Literal[0] = FieldInfo(alias="deletedJobsCount")

    id: str
