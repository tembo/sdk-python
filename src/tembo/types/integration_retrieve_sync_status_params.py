# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntegrationRetrieveSyncStatusParams"]


class IntegrationRetrieveSyncStatusParams(TypedDict, total=False):
    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]
