import sys

from . import parser_smart
from .types import (
    SkewerParserResult,
    SkewerCommandDetail,
)


def skewer_parser(
    command_detail: SkewerCommandDetail,
    args: list[str] | None = None,
) -> SkewerParserResult:
    if args is None:
        args = sys.argv[1:]
    return parser_smart.parser(command_detail, args)
