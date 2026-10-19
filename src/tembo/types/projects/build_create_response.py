# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BuildCreateResponse"]


class BuildCreateResponse(BaseModel):
    job_ids: List[str] = FieldInfo(alias="jobIds")
