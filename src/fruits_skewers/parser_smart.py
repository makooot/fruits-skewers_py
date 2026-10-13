import re
import typing

from .helper import strtobool
from .types import (
    SkewerCommandDetail,
    SkewerFatalError,
    SkewerParserResult,
    SkewerShowHelpException,
    SkewerShowVersionException,
    SkewerValueError,
)

default_command_detail: SkewerCommandDetail = {
    "cmdline": {
        "help_option": ["-h", "--help"],
        "version_option": ["--version"],
    },
    "options": [],
}


def get_help_option(command_detail: SkewerCommandDetail) -> list[str]:
    try:
        help_option = command_detail["cmdline"]["help_option"]
    except KeyError:
        return default_command_detail["cmdline"]["help_option"]
    for option in help_option:
        if not re.match(r"^(-[a-zA-Z]|--[a-z][a-z-]+)$", option):
            raise SkewerFatalError(f"Invalid parser setting: help option: {option}")
    return help_option


def get_version_option(command_detail: SkewerCommandDetail) -> list[str]:
    try:
        version_option = command_detail["cmdline"]["version_option"]
    except KeyError:
        return default_command_detail["cmdline"]["version_option"]
    for option in version_option:
        if not re.match(r"^(-[a-zA-Z]|--[a-z][a-z-]+)$", option):
            raise SkewerFatalError(f"Invalid parser setting: version option: {option}")
    return version_option


class OptionDictContent(typing.TypedDict, total=False):
    type: str
    key: str


class OptionNames(typing.TypedDict, total=False):
    short: dict[str, OptionDictContent]
    long: dict[str, OptionDictContent]


def get_option_names(command_detail: SkewerCommandDetail) -> OptionNames:
    option_names: OptionNames = {"short": {}, "long": {}}
    for option in command_detail.get("options", []):
        key = option["key"]
        type = option.get("type", "string")
        if not type in ("string", "int", "bool"):
            raise SkewerFatalError(f"Invalid parser setting: option type: {type}")
        for name in option.get("cmd", []):
            match = re.match(
                r"^(-(?P<shortname>[a-zA-Z])|--(?P<longname>[a-z][a-z-]+))$", name
            )
            if not match:
                raise SkewerFatalError(f"Invalid parser setting: option name: {name}")
            if match["longname"]:
                option_names["long"][match["longname"]] = {
                    "type": type,
                    "key": key,
                }
            elif match["shortname"]:
                option_names["short"][match["shortname"]] = {
                    "type": type,
                    "key": key,
                }
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
        else:  # "string", "int"
            raise SkewerValueError(f"Invalid option: {option_name} in: {arg}")
        values[option_key] = option_value
    if match.group(2):
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
                except IndexError:
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
                except IndexError:
                    raise SkewerValueError(f"Invalid option: {arg}")
                try:
                    option_value = int(value_string, 10)
                except ValueError:
                    raise SkewerValueError(f"Invalid option: {arg} {value_string}")
        else:  # "bool"
            if match.group(4):
                option_value = strtobool(match.group(5))
            else:
                option_value = True
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
            except IndexError:
                raise SkewerValueError(f"Invalid option: {arg}")
        else:
            option_value = match.group(3)
    elif option_dict_content["type"] == "int":
        if match.group(2) is None:
            try:
                value_string = args.pop(0)
            except IndexError:
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
    else:  # "bool"
        if match.group(2) is None:
            option_value = True
        else:
            option_value = strtobool(match.group(3))

    values[option_key] = option_value


def parser(
    command_detail: SkewerCommandDetail, args_raw: list[str]
) -> tuple[SkewerParserResult, list[str]]:
    values: SkewerParserResult = {}
    help_option = get_help_option(command_detail)
    version_option = get_version_option(command_detail)
    option_names = get_option_names(command_detail)
    args = args_raw[:]
    while args:
        arg = args.pop(0)
        if arg == "--":
            break
        elif arg in help_option:
            raise SkewerShowHelpException()
        elif arg in version_option:
            raise SkewerShowVersionException()
        elif arg.startswith("--"):
            parse_long_option(arg, args, option_names, values)
        elif arg.startswith("-"):
            parse_short_option(arg, args, option_names, values)
        else:
            args.insert(0, arg)
            break
    return values, args
