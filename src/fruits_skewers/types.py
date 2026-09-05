from typing import TypedDict, TypeAlias


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


SkewerParserResult: TypeAlias = dict[str, str | int | bool | None | list[str]]


class ShowHelpException(Exception):
    pass


class ShowVersionException(Exception):
    pass
