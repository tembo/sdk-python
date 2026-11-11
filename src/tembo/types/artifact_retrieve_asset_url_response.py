# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ArtifactRetrieveAssetURLResponse"]


class ArtifactRetrieveAssetURLResponse(BaseModel):
    asset_id: str = FieldInfo(alias="assetId")

    asset_url: str = FieldInfo(alias="assetUrl")
