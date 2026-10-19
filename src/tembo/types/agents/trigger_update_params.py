# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

from .trigger_filters_param import TriggerFiltersParam

__all__ = ["TriggerUpdateParams"]


class TriggerUpdateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    name: Required[str]
    """Integration event name. Use listIntegrationTriggers to discover supported triggers."""

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]
    """Connected integration that supplies trigger events."""

    filters: TriggerFiltersParam
    """Event-specific trigger filters. Use retrieveIntegrationTrigger and listIntegrationTriggerFilterOptions to discover supported fields and values."""
