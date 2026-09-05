# fruits-kewers

> ⚠️ **Disclaimer: This is a learning-oriented project.**
> This repository is built strictly for personal learning and practicing Python library development. It is **not actively maintained for public production use**. Bug reports, feature requests, or Pull Requests may not be reviewed or addressed. Feel free to fork the repository for your own use under the MIT License.

Command line argument parser

## Installation

You can install this library locally (or from GitHub) using `pip`:

```bash
pip install git+https://github.com/makooot/fruits-skewers_py.git@main
```

## Quick Start

Here is a simple example of how to use the library:

```python
from fruits_skewers.skewer import skewer_parser
from fruits_skewers.types import (
    SkewerCommandDetail,
    SkewerShowHelpException,
    SkewerShowVersionException,
    SkewerValueError,
)


command_detail: SkewerCommandDetail = {
    "options": [
        {"key": "verbose", "type": "bool", "cmd": ["-v", "--verbose"]},
        {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
        {"key": "host", "type": "string", "cmd": ["-H", "--host"]},
    ]
}
try:
    result = skewer_parser(command_detail)
except SkewerShowHelpException:
    print("usage: COMMAND OPTIONS")
    exit(0)
except SkewerShowVersionException:
    print("COMMAND 0.0.0")
    exit(0)
except SkewerValueError as e:
    print(e)
    exit(1)

if result.get("verbose", False):
    if "host" in result:
        print(f"Host: {result.get('host')}")
    else:
        print("Host: (default) ")
    if "port" in result:
        print(f"Port: {result.get('port')}")
    else:
        print("Port: (default) ")
argv = result.get("ARGV")
print(f"ARGV: {len(argv)}")
for i, arg in enumerate(argv):
    print(f"  [{i}]: {arg}")
```

## Contributing

Please refer to CONTRIBUTING.md for details on how this repository handles issues, pull requests, and forks.

## License

MIT License
