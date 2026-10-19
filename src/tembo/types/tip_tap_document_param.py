# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypeAlias

__all__ = ["TipTapDocumentParam"]


TipTapDocumentParam: TypeAlias = Union[
    "TipTapImageNodeParam",
    "TipTapMentionNodeParam",
    "TipTapHeadingNodeParam",
    "TipTapOrderedListNodeParam",
    "TipTapTaskItemNodeParam",
    "TipTapCodeBlockNodeParam",
    "TipTapContentNodeParam",
    Dict[str, object],
]


from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_code_block_node_param import TipTapCodeBlockNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
