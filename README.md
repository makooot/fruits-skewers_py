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
from fruits_skewers import skewer

command_detail:skewer.types.SkewerCommandDetail = {
    "options": [
        {"key": "verbose", "type": "bool", "cmd": ["-v", "--verbose"]},
        {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
        {"key": "host", "type": "string", "cmd": ["-H", "--host"]},
    ]
}
result = skewer.parser(command_detail)
if result.get("verbose, False):
    if "host" in result:
        print(f"Host: {resut.get('host')}")
    else:
        print("Host: (default) ")
    if "port" in result:
        print(f"Port: {resut.get('port')}")
    else:
        print("Port: (default) ")
```

## Contributing

Please refer to CONTRIBUTING.md for details on how this repository handles issues, pull requests, and forks.

## License

MIT License
