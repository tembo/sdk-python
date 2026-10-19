# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelUpdateParams"]


class ModelUpdateParams(TypedDict, total=False):
    enabled: bool
    """Enable or disable this model for the organization."""

    inference_provider: Annotated[
        Optional[Literal["TemboManagedInference", "BYOK", "AWSBedrock", "GCPVertexAI", "OpenRouter"]],
        PropertyInfo(alias="inferenceProvider"),
    ]
    """Select the inference provider used to run this model. Use listModels to discover available provider access."""
