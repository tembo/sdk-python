# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

from .trigger_filters_param import TriggerFiltersParam

__all__ = ["TriggerCreateParams"]


class TriggerCreateParams(TypedDict, total=False):
    name: Required[str]
    """Integration event name. Use listIntegrationTriggers to discover supported triggers."""

    integration_type: Annotated[str, PropertyInfo(alias="integrationType")]
    """Provider type for the trigger, such as github or slack."""

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]
    """Connected integration that supplies trigger events."""

    filters: TriggerFiltersParam
    """Event-specific trigger filters. Use retrieveIntegrationTrigger and listIntegrationTriggerFilterOptions to discover supported fields and values."""
