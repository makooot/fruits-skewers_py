from typing import TypedDict


class C:
    pass


class SkewerOption(TypedDict, total=False):
    key: str
    type: str
    cmd: list[str]


class SkewerCommandDetail(TypedDict, total=False):
    arguments_key: str
    options: list[SkewerOption]
    help_option: list[str]
    version_option: list[str]


type SkewerParserResult = dict[str, str | int | bool | None | list[str]]


class SkewerShowHelpException(Exception):
    pass


class SkewerShowVersionException(Exception):
    pass

class SkewerValueError(ValueError):
    pass
