from typing import TypedDict


class SkewerCommand(TypedDict, total=False):
    arguments_key: str
    help_option: list[str]
    version_option: list[str]


class SkewerOption(TypedDict, total=False):
    key: str
    type: str
    cmd: list[str]


class SkewerCommandDetail(TypedDict, total=False):
    command: SkewerCommand
    options: list[SkewerOption]


type SkewerParserResult = dict[str, str | int | bool | None | list[str]]


class SkewerShowHelpException(Exception):
    pass


class SkewerShowVersionException(Exception):
    pass


class SkewerValueError(ValueError):
    pass
