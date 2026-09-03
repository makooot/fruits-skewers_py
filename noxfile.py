import nox
from nox_uv import session

nox.options.default_venv_backend = "uv"


@session(python=["3.14"])
def tests(s: nox.Session) -> None:
    """session for testing the module"""

    # run the tests
    s.run("python", "-m", "unittest", "discover", "-s", "test")


@session(python=["3.14"])
def tests_package(s: nox.Session) -> None:
    """session for testing the package"""

    # install the package
    s.install("./dist/fruits_skewers-0.2.0-py3-none-any.whl")

    # run the tests
    s.run("python", "-m", "unittest", "discover", "-s", "test_package")
