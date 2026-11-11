# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RoleDeleteParams"]


class RoleDeleteParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    replacement_role_id: Required[Annotated[str, PropertyInfo(alias="replacementRoleId")]]
