import sys

from . import parser_smart, types


def parser(
    command_detail: types.SkewerCommandDetail ,
    args: list[str] | None = None,
) -> dict[str, str | int | bool | None | list[str]]:
    if args is None:
        args = sys.argv[1:]
    return parser_smart.parser(command_detail, args)
