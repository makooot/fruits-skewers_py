import typing
import unittest

from fruits_skewers import parser_smart


class TestParserSmart(unittest.TestCase):
    @typing.override
    def setUp(self):
        pass

    def test_empty(self):
        args = []
        command_detail: parser_smart.SkewerCommandDetail = {}
        _, unnamed = parser_smart.parser(command_detail, args)
        self.assertEqual(unnamed, [])

    def test_args_1(self):
        args = ["v1"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        _, unnamed = parser_smart.parser(command_detail, args)
        self.assertEqual(unnamed, ["v1"])

    def test_args_2(self):
        args = ["v1", "v2"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        _, unnamed = parser_smart.parser(command_detail, args)
        self.assertEqual(unnamed, ["v1", "v2"])

    def test_args_3(self):
        args = ["v1", "v2", "v3"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        _, unnamed = parser_smart.parser(command_detail, args)
        self.assertEqual(unnamed, ["v1", "v2", "v3"])

    def test_short_bool(self):
        args = ["-b"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "b", "type": "bool", "cmd": ["-b"]}]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["b"])

    def test_short_string_connected(self):
        args = ["-s=foo"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "s", "type": "string", "cmd": ["-s"]}]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["s"], "foo")

    def test_short_string_seperated(self):
        args = ["-s", "foo"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "s", "type": "string", "cmd": ["-s"]}]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["s"], "foo")

    def test_short_int_connected(self):
        args = ["-n=123"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "n", "type": "int", "cmd": ["-n"]}]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["n"], 123)

    def test_short_int_seperated(self):
        args = ["-n", "123"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [{"key": "n", "type": "int", "cmd": ["-n"]}]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["n"], 123)

    def test_short_chain_bbb(self):
        args = ["-abc"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "c", "type": "bool", "cmd": ["-c"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertTrue(opts["c"])

    def test_short_chain_bbs_empty(self):
        args = ["-abs="]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "c", "type": "bool", "cmd": ["-c"]},
                {"key": "s", "type": "string", "cmd": ["-s"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertEqual(opts["s"], "")

    def test_short_chain_bbs_any(self):
        args = ["-abs=foo"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "c", "type": "bool", "cmd": ["-c"]},
                {"key": "s", "type": "string", "cmd": ["-s"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertEqual(opts["s"], "foo")

    def test_short_chain_bbi(self):
        args = ["-abn=1234"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "n", "type": "int", "cmd": ["-n"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["a"])
        self.assertTrue(opts["b"])
        self.assertEqual(opts["n"], 1234)

    def test_long_bool(self):
        args = ["--allow"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "allow", "type": "bool", "cmd": ["--allow"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["allow"])

    def test_long_string_connected_empty(self):
        args = ["--prefix="]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "prefix", "type": "string", "cmd": ["--prefix"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["prefix"], "")

    def test_long_string_connected_any(self):
        args = ["--prefix=I:"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "prefix", "type": "string", "cmd": ["--prefix"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["prefix"], "I:")

    def test_long_string_seperated(self):
        args = ["--prefix", "I:"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "prefix", "type": "string", "cmd": ["--prefix"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["prefix"], "I:")

    def test_long_int_connected(self):
        args = ["--port=8080"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["port"], 8080)

    def test_long_int_seperated(self):
        args = ["--port", "8080"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["port"], 8080)

    def test_both_def_short(self):
        args = ["-p=8080"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["port"], 8080)

    def test_both_def_long(self):
        args = ["--port=8080"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
            ]
        }
        opts, _ = parser_smart.parser(command_detail, args)
        self.assertEqual(opts["port"], 8080)

    def test_mix(self):
        args = ["-ap", "8080", "--prefix=BEEF", "jkl", "mno"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "allow", "type": "bool", "cmd": ["-a", "--allow"]},
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
                {"key": "prefix", "type": "string", "cmd": ["-x", "--prefix"]},
            ]
        }
        opts, unnamed = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["allow"])
        self.assertEqual(opts["prefix"], "BEEF")
        self.assertEqual(opts["port"], 8080)
        self.assertEqual(unnamed, ["jkl", "mno"])

    def test_double_hyphen(self):
        args = ["-ap", "8080", "--", "--prefix=BEEF", "jkl", "mno"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "allow", "type": "bool", "cmd": ["-a", "--allow"]},
                {"key": "prefix", "type": "string", "cmd": ["-x", "--prefix"]},
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
            ]
        }
        opts, unnamed = parser_smart.parser(command_detail, args)
        self.assertTrue(opts["allow"])
        self.assertEqual(opts["port"], 8080)
        self.assertEqual(unnamed, ["--prefix=BEEF", "jkl", "mno"])

    def test_short_invalid_name(self):
        args = ["-#"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        with self.assertRaises(ValueError):
            parser_smart.parser(command_detail, args)

    def test_short_undefined_name(self):
        args = ["-q"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        with self.assertRaises(ValueError):
            parser_smart.parser(command_detail, args)

    def test_long_invalid_name(self):
        args = ["--###-###"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        with self.assertRaises(ValueError):
            parser_smart.parser(command_detail, args)

    def test_invlid_int_1(self):
        args = ["--port", "0A"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(ValueError):
            parser_smart.parser(command_detail, args)

    def test_invlid_int_2(self):
        args = ["--port=0A"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(ValueError):
            parser_smart.parser(command_detail, args)

    def test_invlid_int_3(self):
        args = ["-p", "0A"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(ValueError):
            parser_smart.parser(command_detail, args)

    def test_invlid_int_4(self):
        args = ["-p=0A"]
        command_detail: parser_smart.SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(ValueError):
            parser_smart.parser(command_detail, args)

    def test_invalid_name_1(self):
        args = ["--verbose"]
        with self.assertRaises(ValueError):
            parser_smart.parser({}, args)

    def test_invalid_name_2(self):
        args = ["-v"]
        with self.assertRaises(ValueError):
            parser_smart.parser({}, args)

    def test_short_showhelp_exception(self):
        args = ["-h"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        with self.assertRaises(parser_smart.SkewerShowHelpException):
            parser_smart.parser(command_detail, args)

    def test_long_showhelp_exception(self):
        args = ["--help"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        with self.assertRaises(parser_smart.SkewerShowHelpException):
            parser_smart.parser(command_detail, args)

    def test_long_showversion_exception(self):
        args = ["--version"]
        command_detail: parser_smart.SkewerCommandDetail = {}
        with self.assertRaises(parser_smart.SkewerShowVersionException):
            parser_smart.parser(command_detail, args)

    def test_parse_short(self):
        args = ["-ap", "8080", "--", "foo"]
        option_dict: parser_smart.OptionNames = {
            "short": {
                "a": {"key": "a", "type": "bool"},
                "p": {"key": "p", "type": "int"},
            }
        }
        values = {}
        arg = args.pop(0)
        parser_smart.parse_short_option(arg, args, option_dict, values)
        self.assertEqual(args, ["--", "foo"])
        self.assertTrue(values["a"])
        self.assertEqual(values["p"], 8080)
