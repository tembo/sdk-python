# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ArtifactCreateResponse", "Runtime"]


class Runtime(BaseModel):
    hostname: Optional[str] = None

    service_name: Optional[str] = FieldInfo(alias="serviceName", default=None)

    service_type: Optional[str] = FieldInfo(alias="serviceType", default=None)


class ArtifactCreateResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    id: str

    session_id: str = FieldInfo(alias="sessionId")

    type: Literal["PullRequest", "ToolCall", "Plan", "Response", "File", "Service", "Source"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    asset_id: Optional[str] = FieldInfo(alias="assetId", default=None)

    asset_url: Optional[str] = FieldInfo(alias="assetUrl", default=None)

    category: Optional[
        Literal[
            "code_walkthrough",
            "bug_report",
            "incident_report",
            "license_audit",
            "data_flow_map",
            "security_findings",
            "cost_map",
            "ux_variations",
            "architecture_map",
            "migration_summary",
            "release_checklist",
            "shipped_summary",
            "rollout_plan",
            "diagram",
            "chart",
            "dashboard",
            "timeline",
            "comparison",
            "report",
        ]
    ] = None

    content: str

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    description: Optional[str] = None

    file_kind: Literal["image", "video", "audio", "html", "markdown", "text", "file"] = FieldInfo(alias="fileKind")

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    output_type: Optional[Literal["html", "markdown", "json", "csv", "asset"]] = FieldInfo(
        alias="outputType", default=None
    )

    related_pull_request_urls: List[str] = FieldInfo(alias="relatedPullRequestUrls")

    runtime: Optional[Runtime] = None

    service_port: Optional[int] = FieldInfo(alias="servicePort", default=None)

    service_url: Optional[str] = FieldInfo(alias="serviceUrl", default=None)

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    title: str
