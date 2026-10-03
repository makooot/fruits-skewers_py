import tomllib
from pathlib import Path

import nox
from nox_uv import session

nox.options.default_venv_backend = "uv"


@session(python=["3.12", "3.13", "3.14", "3.15"])
def tests(s: nox.Session) -> None:
    """session for testing the module"""

    # run the tests
    s.run("python", "-m", "unittest", "discover", "-s", "test")


@session(python=["3.12", "3.13", "3.14", "3.15"])
def tests_package(s: nox.Session) -> None:
    """session for testing the package"""

    # get name and version number
    pyproject_path = Path(__file__).parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    project_name = data["project"]["name"].lower().translate(str.maketrans("-.", "__"))
    project_version = data["project"]["version"]

    # install the package
    s.install(f"./dist/{project_name}-{project_version}-py3-none-any.whl")

    # run the tests
    s.run("python", "-m", "unittest", "discover", "-s", "test_package")
