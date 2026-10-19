# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .tip_tap_link_mark_param import TipTapLinkMarkParam
from .tip_tap_mark_param import TipTapMarkParam

__all__ = ["TipTapCodeBlockNodeParam", "Mark", "Attrs"]


class TipTapCodeBlockNodeParam(TypedDict, total=False):
    text: str

    marks: Iterable[Mark]

    type: Required[Literal["codeBlock"]]

    attrs: Attrs

    content: Iterable["TipTapNodeParam"]


class Attrs(TypedDict, total=False):
    language: Optional[str]


Mark: TypeAlias = Union[TipTapLinkMarkParam, TipTapMarkParam]


from .tip_tap_node_param import TipTapNodeParam
from .tip_tap_image_node_param import TipTapImageNodeParam
from .tip_tap_mention_node_param import TipTapMentionNodeParam
from .tip_tap_heading_node_param import TipTapHeadingNodeParam
from .tip_tap_ordered_list_node_param import TipTapOrderedListNodeParam
from .tip_tap_task_item_node_param import TipTapTaskItemNodeParam
from .tip_tap_content_node_param import TipTapContentNodeParam
