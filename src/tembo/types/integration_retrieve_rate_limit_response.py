# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationRetrieveRateLimitResponse", "Core", "Graphql", "Search"]


class Search(BaseModel):
    limit: float

    remaining: float

    reset_at: datetime = FieldInfo(alias="resetAt")

    used: float


class Graphql(BaseModel):
    limit: float

    remaining: float

    reset_at: datetime = FieldInfo(alias="resetAt")

    used: float


class Core(BaseModel):
    limit: float

    remaining: float

    reset_at: datetime = FieldInfo(alias="resetAt")

    used: float


class IntegrationRetrieveRateLimitResponse(BaseModel):
    core: Core

    graphql: Graphql

    search: Search
