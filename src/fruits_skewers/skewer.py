import sys

from . import parser_smart, types
from .types import SkewerParserResult


def parser(
    command_detail: types.SkewerCommandDetail,
    args: list[str] | None = None,
) -> SkewerParserResult:
    if args is None:
        args = sys.argv[1:]
    return parser_smart.parser(command_detail, args)
