import sys

from . import parser_minimum, parser_smart, types


def parser(
    command_detail: types.SkewerCommandDetail | None = None,
    args: list[str] | None = None,
) -> dict[str, str | int | bool | None | list[str]]:
    if args is None:
        args = sys.argv[1:]
    if command_detail is None:
        return parser_minimum.parser(args)
    else:
        return parser_smart.parser(command_detail, args)
