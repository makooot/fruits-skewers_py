
# skewer_parser -- method

`skewer_parser(command_detail, args=None)`

Arguments:
- command_detail -- Parser settings.
- args -- List of strings to be parsed.

Return value is dict object stored results.

Exception:
- SkewerShowHelpException -- Need to display the application help.
- SkewerShowVersionException -- Need to display the application version.
- SkewerValueError -- Error occurred on parsing.

## command_detail -- argument

Parser settings.

```python
{
    "arguments_key": "ARGS"
    "options": [
        {
            "key": "foo"
            "type": "string"
            "cmd": ["-f", "--foo"]
        }
    ]
    "help_option": ["-h", "--help"]
    "version_option": ["--version"]
}
```

### arguments_key

keyword to refer return value excluding options(start with "-") from args.
(default: "ARGS")

### options
(default: [])

**key** is keyword to refer return value.

**type** is option types: "string", "int", and "bool".
(default: "string")

**cmd** is list of command-line option.

### help_option
Command-line options to display help.  If One of thees is specified, throw
SkewerShowHelpException.  The caller display the help, if it catches
the exception.
(default: ["-h", "--help"])

### version_option
Command-line options to display version. If One of thees is specified, throw
SkewerShowversionException.
(default: ["--version"])

## args -- argument
List of strings to be parsed.
 (default: sys.argv[1:])

## Return value

Return value is dict object stored results.

## SkewerShowHelpException -- exception

An option contained in help_option was specified in args. If the caller of
skewer_parse() catches this exception, it displays the application's help
information.

## SkewerShowVersionException -- exception

An option contained in version_option was specified in args. If the caller of
skewer_parse() catches this exception, it displays the application version.

## SkewerValueError -- exception

Error occurred on parsing.

