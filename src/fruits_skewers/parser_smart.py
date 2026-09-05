import re
import typing

from . import types
from .types import SkewerParserResult
from .types import SkewerValueError

default_command_detail: types.SkewerCommandDetail = {
    "arguments_key": "ARGV",
    "options": [],
    "help_option": ["--help"],
    "version_option": ["-h", "--version"],
}


def get_arguments_key(command_detail: types.SkewerCommandDetail) -> str:
    try:
        return command_detail["arguments_key"]
    except KeyError:
        return default_command_detail["arguments_key"]


class OptionDictContent(typing.TypedDict, total=False):
    type: str
    key: str


class OptionNames(typing.TypedDict, total=False):
    short: dict[str, OptionDictContent]
    long: dict[str, OptionDictContent]


def get_option_names(command_detail: types.SkewerCommandDetail) -> OptionNames:
    option_names: OptionNames = {"short": {}, "long": {}}
    for option in command_detail.get("options", []):
        key = option["key"]
        type = option.get("type", "string")
        for name in option.get("cmd", []):
            match = re.match(r"^(--?)(.*)", name)
            if not match:
                raise SkewerValueError("FATAL")
            if match.group(1) == "--":
                option_names["long"][match.group(2)] = {"type": type, "key": key}
            elif match.group(1) == "-":
                option_names["short"][match.group(2)] = {"type": type, "key": key}
    return option_names


def parse_short_option(
    arg: str,
    args: list[str],
    option_dict: OptionNames,
    values: SkewerParserResult,
) -> None:
    match = re.match(r"^-([a-zA-Z]*)(([a-zA-Z])(=(.*))?)", arg)
    if not match:
        raise SkewerValueError(f"Invalid option: {arg}")
    for option_name in list(match.group(1)):
        try:
            option_dict_content = option_dict["short"][option_name]
        except KeyError:
            raise SkewerValueError(f"Invalid option: {arg}")
        option_key = option_dict_content["key"]
        if option_dict_content["type"] == "bool":
            option_value = True
        elif (
            option_dict_content["type"] == "string"
            or option_dict_content["type"] == "int"
        ):
            raise SkewerValueError(f"Invalid option: {option_name} in: {arg}")
        else:
            raise SkewerValueError("FATAL")
        values[option_key] = option_value
    if match.group(2):
        option_value = None
        option_name = match.group(3)
        try:
            option_dict_content = option_dict["short"][option_name]
        except KeyError:
            raise SkewerValueError(f"Invalid option: {arg}")
        option_key = option_dict_content["key"]
        if option_dict_content["type"] == "string":
            if match.group(4):
                option_value = match.group(5)
            else:
                try:
                    option_value = args.pop(0)
                except ValueError:
                    raise SkewerValueError(f"Invalid option: {arg}")
        elif option_dict_content["type"] == "int":
            if match.group(4):
                try:
                    option_value = int(match.group(5), 10)
                except ValueError:
                    raise SkewerValueError(f"Invalid option: {arg}")
            else:
                try:
                    value_string = args.pop(0)
                except ValueError:
                    raise SkewerValueError(f"Invalid option: {arg}")
                try:
                    option_value = int(value_string, 10)
                except ValueError:
                    raise SkewerValueError(f"Invalid option: {arg} {value_string}")
        elif option_dict_content["type"] == "bool":
            if match.group(4):
                option_value = not match.group(5).lower in [
                    "",
                    "false",
                    "f",
                    "off",
                    "no",
                    "0",
                ]
            else:
                option_value = True
        else:
            raise SkewerValueError("FATAL")

        values[option_key] = option_value


def parse_long_option(
    arg: str,
    args: list[str],
    option_dict: OptionNames,
    values: SkewerParserResult,
) -> None:
    match = re.match(r"^--([a-z][a-z-]+)(=(.*))?", arg)
    if not match:
        raise SkewerValueError(f"Invalid option: {arg}")
    name = match.group(1)
    try:
        option_dict_content = option_dict["long"][name]
    except KeyError:
        raise SkewerValueError(f"Invalid option: {arg}")
    option_key = option_dict_content["key"]
    if option_dict_content["type"] == "string":
        if match.group(2) is None:
            try:
                option_value = args.pop(0)
            except ValueError:
                raise SkewerValueError(f"Invalid option: {arg}")
        else:
            option_value = match.group(3)
    elif option_dict_content["type"] == "int":
        if match.group(2) is None:
            try:
                value_string = args.pop(0)
            except ValueError:
                raise SkewerValueError(f"Invalid option: {arg}")
            try:
                option_value = int(value_string, 10)
            except ValueError:
                raise SkewerValueError(f"Invalid value: {arg} {value_string}")
        else:
            value_string = match.group(3)
            try:
                option_value = int(value_string, 10)
            except ValueError:
                raise SkewerValueError(f"Invalid value: {arg}")
    elif option_dict_content["type"] == "bool":
        if match.group(2) is None:
            option_value = True
        else:
            option_value = not match.group(3).lower in ["", "false", "f", "off", "no"]
    elif option_dict_content["type"] == "nullable_string":
        if match.group(2) is None:
            option_value = None
        else:
            option_value = match.group(3)
    else:
        raise SkewerValueError("FATAL")

    values[option_key] = option_value


def parser(
    command_detail: types.SkewerCommandDetail, args_raw: list[str]
) -> types.SkewerParserResult:
    values: types.SkewerParserResult = {}
    option_names = get_option_names(command_detail)
    args = args_raw[:]
    while args:
        arg = args.pop(0)
        if arg == "--":
            break
        elif arg in ["-h", "--help"]:
            raise types.SkewerShowHelpException()
        elif arg in ["--version"]:
            raise types.SkewerShowVersionException()
        elif arg.startswith("--"):
            parse_long_option(arg, args, option_names, values)
        elif arg.startswith("-"):
            parse_short_option(arg, args, option_names, values)
        else:
            args.insert(0, arg)
            break
    values[get_arguments_key(command_detail)] = args
    return values
