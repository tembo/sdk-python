# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    content: str
    """Replace the text of a queued message before processing starts."""

    rich_content: Annotated[Optional["TipTapDocumentParam"], PropertyInfo(alias="richContent")]
    """Replace the queued message rich-text document, or null to clear it."""


from .tip_tap_document_param import TipTapDocumentParam
from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_code_block_node_param import TipTapCodeBlockNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
