# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Union
from typing_extensions import TypeAlias

from .tip_tap_image_node import TipTapImageNode
from .tip_tap_mention_node import TipTapMentionNode
from .tip_tap_heading_node import TipTapHeadingNode
from .tip_tap_ordered_list_node import TipTapOrderedListNode
from .tip_tap_task_item_node import TipTapTaskItemNode
from .tip_tap_code_block_node import TipTapCodeBlockNode
from .tip_tap_content_node import TipTapContentNode

__all__ = ["TipTapDocument"]

TipTapDocument: TypeAlias = Union[
    TipTapImageNode,
    TipTapMentionNode,
    TipTapHeadingNode,
    TipTapOrderedListNode,
    TipTapTaskItemNode,
    TipTapCodeBlockNode,
    TipTapContentNode,
    Dict[str, object],
]
