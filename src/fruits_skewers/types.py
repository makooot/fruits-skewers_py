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


class ShowHelpException(Exception):
    pass


class ShowVersionException(Exception):
    pass
