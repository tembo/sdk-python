# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["ArtifactCreateParams", "Output", "Output2", "Output3", "Output4", "Output5", "Output6"]


class ArtifactCreateParams(TypedDict, total=False):
    title: Required[str]
    """Human-readable title for the artifact."""

    description: str
    """Short description of what the artifact shows."""

    category: Literal[
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
    """Artifact category for display and filtering."""

    output: Required[Output]
    """Artifact content or a reference to an uploaded asset. The type field selects the required fields."""

    related_pull_request_urls: Annotated[SequenceNotStr[str], PropertyInfo(alias="relatedPullRequestUrls")]
    """URLs of pull requests related to this artifact."""

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """Session to attach the artifact to."""


class Output6(TypedDict, total=False):
    type: Required[Literal["asset"]]

    asset_id: Required[Annotated[str, PropertyInfo(alias="assetId")]]
    """ID of an existing uploaded Tembo asset."""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Optional display filename for the uploaded asset."""


class Output5(TypedDict, total=False):
    type: Required[Literal["csv"]]

    content: Required[str]
    """CSV content for audits, tables, inventories, reports, and spreadsheet-friendly exports. Must be at most 5242880 bytes after UTF-8 encoding."""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Optional stored filename. The extension is normalized."""


class Output4(TypedDict, total=False):
    type: Required[Literal["json"]]

    content: Required[str]
    """JSON text for structured data, diagnostics, or machine-readable findings. Send the JSON as a string, not as an object. Must be at most 5242880 bytes after UTF-8 encoding."""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Optional stored filename. The extension is normalized."""


class Output3(TypedDict, total=False):
    type: Required[Literal["markdown"]]

    content: Required[str]
    """Markdown content for a readable report, checklist, walkthrough, or notes artifact. Must be at most 5242880 bytes after UTF-8 encoding."""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Optional stored filename. The extension is normalized."""


class Output2(TypedDict, total=False):
    type: Required[Literal["html"]]

    content: Required[str]
    """Complete self-contained HTML document. Inline CSS and JavaScript are allowed. Do not depend on external network assets. Must be at most 5242880 bytes after UTF-8 encoding."""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Optional stored filename. The extension is normalized."""


Output: TypeAlias = Union[Output2, Output3, Output4, Output5, Output6]
