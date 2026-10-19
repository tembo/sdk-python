# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .tip_tap_image_node import TipTapImageNode
from .tip_tap_mention_node import TipTapMentionNode
from .tip_tap_heading_node import TipTapHeadingNode
from .tip_tap_ordered_list_node import TipTapOrderedListNode
from .tip_tap_task_item_node import TipTapTaskItemNode
from .tip_tap_code_block_node import TipTapCodeBlockNode
from .tip_tap_content_node import TipTapContentNode

__all__ = ["TipTapNode"]

TipTapNode: TypeAlias = Union[
    TipTapImageNode,
    TipTapMentionNode,
    TipTapHeadingNode,
    TipTapOrderedListNode,
    TipTapTaskItemNode,
    TipTapCodeBlockNode,
    TipTapContentNode,
]

# The node modules reference TipTapNode recursively. Importing it back at the bottom of
# each module made a circular import, so bind it here after the union is defined.
from . import tip_tap_image_node as _tip_tap_image_node
from . import tip_tap_mention_node as _tip_tap_mention_node
from . import tip_tap_heading_node as _tip_tap_heading_node
from . import tip_tap_ordered_list_node as _tip_tap_ordered_list_node
from . import tip_tap_task_item_node as _tip_tap_task_item_node
from . import tip_tap_code_block_node as _tip_tap_code_block_node
from . import tip_tap_content_node as _tip_tap_content_node

for _module in (
    _tip_tap_image_node,
    _tip_tap_mention_node,
    _tip_tap_heading_node,
    _tip_tap_ordered_list_node,
    _tip_tap_task_item_node,
    _tip_tap_code_block_node,
    _tip_tap_content_node,
):
    _module.TipTapNode = TipTapNode  # type: ignore[attr-defined]
