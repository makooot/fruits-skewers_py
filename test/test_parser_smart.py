import typing
import unittest

from fruits_skewers import parser_smart


class TestParserSmart(unittest.TestCase):
    @typing.override
    def setUp(self):
        pass

    def test_parser_no_options(self):
        opts, unnamed = parser_smart.parser({}, [])
        self.assertEqual(opts, {})
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser({}, ["v1"])
        self.assertEqual(opts, {})
        self.assertEqual(unnamed, ["v1"])
        opts, unnamed = parser_smart.parser({}, ["v1", "v2"])
        self.assertEqual(opts, {})
        self.assertEqual(unnamed, ["v1", "v2"])
        opts, unnamed = parser_smart.parser({}, ["v1", "v2", "v3"])
        self.assertEqual(opts, {})
        self.assertEqual(unnamed, ["v1", "v2", "v3"])
        opts, unnamed = parser_smart.parser({}, ["--", "v1", "v2", "v3"])
        self.assertEqual(opts, {})
        self.assertEqual(unnamed, ["v1", "v2", "v3"])

    def test_parser_invalid_option(self):
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser({}, ["-#"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser({}, ["--####"])

    def test_parser_undefined_option(self):
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser({}, ["-X"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser({}, ["--xxxx"])

    def test_parser_bool_option(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "b", "type": "bool", "cmd": ["-b", "--bbb"]}]
        }
        opts, unnamed = parser_smart.parser(command_detail, ["-b"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=true"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=TRUE"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=t"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=T"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=on"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=ON"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=yes"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=YES"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=y"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=Y"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=1"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=anything"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=false"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=FALSE"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=f"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=F"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=off"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=OFF"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=no"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=NO"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=n"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=N"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=0"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b="])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=true"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=TRUE"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=t"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=T"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=on"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=ON"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=yes"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=YES"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=y"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=Y"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=1"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=anything"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=false"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=FALSE"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=f"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=F"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=off"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=OFF"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=no"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=NO"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=n"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=N"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb=0"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb="])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])

    def test_parser_string_option(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "s", "type": "string", "cmd": ["-s", "--sss"]}]
        }
        opts, unnamed = parser_smart.parser(command_detail, ["-s=foo"])
        self.assertEqual(opts["s"], "foo")
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-s", "foo"])
        self.assertEqual(opts["s"], "foo")
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--sss=foo"])
        self.assertEqual(opts["s"], "foo")
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--sss", "foo"])
        self.assertEqual(opts["s"], "foo")
        self.assertEqual(unnamed, [])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-s"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["--sss"])

    def test_parser_int_option(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "n", "type": "int", "cmd": ["-n", "--nnn"]}]
        }
        opts, unnamed = parser_smart.parser(command_detail, ["-n=123"])
        self.assertEqual(opts["n"], 123)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-n", "123"])
        self.assertEqual(opts["n"], 123)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--nnn=123"])
        self.assertEqual(opts["n"], 123)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-n", "123"])
        self.assertEqual(opts["n"], 123)
        self.assertEqual(unnamed, [])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-n"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-n=NaN"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-n", "NaN"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["--nnn"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["--nnn=NaN"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["--nnn", "NaN"])

    def test_parser_chaining_short_options(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "c", "type": "bool", "cmd": ["-c"]},
                {"key": "s", "type": "string", "cmd": ["-s"]},
                {"key": "n", "type": "int", "cmd": ["-n"]},
            ]
        }
        opts, unnamed = parser_smart.parser(command_detail, ["-abc"])
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertTrue(opts["c"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-abc=t"])
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertTrue(opts["c"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-abc=f"])
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertFalse(opts["c"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-abs=foo"])
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertEqual(opts["s"], "foo")
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-abs", "foo"])
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertEqual(opts["s"], "foo")
        self.assertEqual(unnamed, [])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-asb"])
        opts, unnamed = parser_smart.parser(command_detail, ["-abn=123"])
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertEqual(opts["n"], 123)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-abn", "123"])
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertEqual(opts["n"], 123)
        self.assertEqual(unnamed, [])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-anb"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-aX"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-Xa"])

    def test_parser_same_option_multiple_times(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "b", "type": "bool", "cmd": ["-b", "--bbb"]},
                {"key": "n", "type": "int", "cmd": ["-n", "--nnn"]},
                {"key": "s", "type": "string", "cmd": ["-s", "--sss"]},
            ]
        }
        opts, unnamed = parser_smart.parser(command_detail, ["-b", "-b"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=f", "-b"])
        self.assertTrue(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b", "-b=f"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b=f", "-b=f"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-bb=f"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--bbb", "-b=f"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-b", "--bbb=f"])
        self.assertFalse(opts["b"])
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-n=1", "-n=2"])
        self.assertEqual(opts["n"], 2)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--nnn=1", "-n=2"])
        self.assertEqual(opts["n"], 2)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-n=1", "--nnn=2"])
        self.assertEqual(opts["n"], 2)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-s=abc", "-s=xyz"])
        self.assertEqual(opts["s"], "xyz")
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["--sss=abc", "-s=xyz"])
        self.assertEqual(opts["s"], "xyz")
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-s=abc", "--sss=xyz"])
        self.assertEqual(opts["s"], "xyz")
        self.assertEqual(unnamed, [])

    def test_parser_help_option(self):
        with self.assertRaises(parser_smart.SkewerShowHelpException):
            parser_smart.parser({}, ["-h"])
        with self.assertRaises(parser_smart.SkewerShowHelpException):
            parser_smart.parser({}, ["--help"])
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"help_option": ["--cmd-help"]}
        }
        with self.assertRaises(parser_smart.SkewerShowHelpException):
            parser_smart.parser(command_detail, ["--cmd-help"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["-h"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["--help"])

    def test_parser_version_option(self):
        with self.assertRaises(parser_smart.SkewerShowVersionException):
            parser_smart.parser({}, ["--version"])
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"version_option": ["--cmd-version"]}
        }
        with self.assertRaises(parser_smart.SkewerShowVersionException):
            parser_smart.parser(command_detail, ["--cmd-version"])
        with self.assertRaises(parser_smart.SkewerValueError):
            parser_smart.parser(command_detail, ["--version"])

    def test_parser_fatal_error_invalid_option_type(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "b", "type": "invalid_type", "cmd": ["-b", "--bool"]},
            ]
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])

    def test_parser_fatal_error_help_option(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"help_option": ["-aa"]}
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"help_option": ["--a"]}
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"help_option": ["--AAAA"]}
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])

    def test_parser_fatal_error_version_option(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"version_option": ["-aa"]}
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"version_option": ["--a"]}
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "cmdline": {"version_option": ["--AAAA"]}
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])

    def test_parser_fatal_error_invalid_option_name(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": [""]},
            ]
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["a"]},
            ]
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-ab"]},
            ]
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["--A"]},
            ]
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["--0"]},
            ]
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "invalidtype", "cmd": ["--abc"]},
            ]
        }
        with self.assertRaises(parser_smart.SkewerFatalError):
            parser_smart.parser(command_detail, [])

    def test_parser_various_arguments(self):
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "allow", "type": "bool", "cmd": ["-a", "--allow"]},
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
                {"key": "prefix", "type": "string", "cmd": ["-x", "--prefix"]},
            ]
        }
        opts, unnamed = parser_smart.parser(command_detail, [])
        self.assertFalse("allow" in opts)
        self.assertFalse("prefix" in opts)
        self.assertFalse("port" in opts)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["v1", "v2", "v3"])
        self.assertFalse("allow" in opts)
        self.assertFalse("prefix" in opts)
        self.assertFalse("port" in opts)
        self.assertEqual(unnamed, ["v1", "v2", "v3"])
        opts, unnamed = parser_smart.parser(command_detail, ["-a"])
        self.assertTrue(opts["allow"])
        self.assertFalse("prefix" in opts)
        self.assertFalse("port" in opts)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-p=12380"])
        self.assertFalse("allow" in opts)
        self.assertFalse("prefix" in opts)
        self.assertEqual(opts["port"], 12380)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(command_detail, ["-x=BEEF"])
        self.assertFalse("allow" in opts)
        self.assertEqual(opts["prefix"], "BEEF")
        self.assertFalse("port" in opts)
        self.assertEqual(unnamed, [])
        opts, unnamed = parser_smart.parser(
            command_detail, ["-ap", "8080", "--prefix=BEEF", "jkl", "mno"]
        )
        self.assertTrue(opts["allow"])
        self.assertEqual(opts["prefix"], "BEEF")
        self.assertEqual(opts["port"], 8080)
        self.assertEqual(unnamed, ["jkl", "mno"])
        opts, unnamed = parser_smart.parser(
            command_detail, ["-ap", "8080", "--", "--prefix=BEEF", "jkl", "mno"]
        )
        self.assertTrue(opts["allow"])
        self.assertEqual(opts["port"], 8080)
        self.assertFalse("prefix" in opts)
        self.assertEqual(unnamed, ["--prefix=BEEF", "jkl", "mno"])
