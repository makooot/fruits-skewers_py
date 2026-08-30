# Option format
Option format has short option, and long option.

Short option format begins with a single hyphen (-) followed by a single character (uppercase or lowercase).
The options without value is chainable.  For example, `-abc` is equivalent to `-a -b -c`.  However, only the last option can have a value. For example, `-abcd=efgh`  is equivalent to `-a -b -c -d=efgh`; in this case, `d` has value.

Long option format begin with two hyphens (--), followed by two or more characters (lowercase English letters and hyphens).

# Value specification
Value specification format has connected format, and separated format.

In the connected format, the name and value are connected by an equals sign (=).  For example, `--host=example.com`.

In the separated format, the name and value are separated.  For example, `--host example.com`.
If you want to specify an empty string, use the escape syntax for your shell. For example, in `bash`, use `--prefix ""`.

# Value type
Valid value types are string, integer, and boolean.

String type needs value.

Integer type needs value.  Specify the value in decimal.

Boolean type’s value is optional.
The option without value is `True`.
The following is `True`: `true`, `t`, `on`, `yes`, `1`.
The following is `False`: `false`, `f`, `off`, `no`, `0`, Empty string.
Any other string of one  or more characters is `True`.
The value is case insensitive.
