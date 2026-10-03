# fruits-skewers

Command line argument parser

## Installation

```bash
pip install fruits-skewers
```

## Quick Start

Here is a simple example of how to use the library:

```python
import fruits_skewers


command_detail: fruits_skewers.SkewerCommandDetail = {
    "options": [
        {"key": "verbose", "type": "bool", "cmd": ["-v", "--verbose"]},
        {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
        {"key": "host", "type": "string", "cmd": ["-H", "--host"]},
    ]
}
try:
    opts, unnamed = fruits_skewers.skewer_parser(command_detail)
except fruits_skewers.SkewerShowHelpException:
    print("usage: COMMAND OPTIONS")
    exit(0)
except fruits_skewers.SkewerShowVersionException:
    print("COMMAND 0.0.0")
    exit(0)
except fruits_skewers.SkewerValueError as e:
    print(e)
    exit(1)

if opts.get("verbose", False):
    if "host" in opts:
        print(f"Host: {opts.get('host')}")
    else:
        print("Host: (default) ")
    if "port" in opts:
        print(f"Port: {opts.get('port')}")
    else:
        print("Port: (default) ")
print(f"ARGV: {len(unnamed)}")
for i, arg in enumerate(unnamed):
    print(f"  [{i}]: {arg}")
```

## Contributing

Please refer to CONTRIBUTING.md for details on how this repository handles
issues, pull requests, and forks.

## License

MIT License
