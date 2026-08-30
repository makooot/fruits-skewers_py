import re

from . import types


def parse_long_option(
    arg: str, values: dict[str, str | int | bool | None | list[str]]
) -> None:
    match = re.match(r"--([a-z][a-z-]+)(=(.*))?", arg)
    if not match:
        raise ValueError(f"Invalid long option: {arg}")
    option_name = match.group(1)
    if match.group(2) is None:
        option_value = None
    else:
        option_value = match.group(3)
    values[option_name] = option_value


def parse_short_option(
    arg: str, values: dict[str, str | int | bool | None | list[str]]
) -> None:
    match = re.match(r"-([a-zA-Z]*)([a-zA-Z])(=(.*))?", arg)
    if not match:
        raise ValueError(f"Invalid short option: {arg}")
    for option_name in list(match.group(1)):
        values[option_name] = None
    option_name = match.group(2)
    option_value = match.group(4)
    values[option_name] = option_value


def parser(args_raw: list[str]) -> dict[str, str | int | bool | None | list[str]]:
    values: dict[str, str | int | bool | None | list[str]] = {}
    args = args_raw[:]
    while args:
        arg = args.pop(0)
        if arg == "--":
            break
        elif arg in ["-h", "--help"]:
            raise types.ShowHelpException()
        elif arg in ["--version"]:
            raise types.ShowVersionException()
        elif arg.startswith("--"):
            parse_long_option(arg, values)
        elif arg.startswith("-"):
            parse_short_option(arg, values)
        else:
            args.insert(0, arg)
            break
    values["ARGV"] = args
    return values
