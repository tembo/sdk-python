# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TriggerListFilterOptionsParams"]


class TriggerListFilterOptionsParams(TypedDict, total=False):
    integration_id: Required[Annotated[str, PropertyInfo(alias="integrationId")]]

    trigger_name: Required[Annotated[str, PropertyInfo(alias="triggerName")]]

    cursor: str
    """Continuation cursor from the previous response nextCursor. Omit for the first page; null nextCursor means there are no more pages."""

    limit: int
    """Maximum number of items to return in one page. Use nextCursor from the response to fetch more items."""

    search: str
    """Search selectable values for this integration trigger filter."""
