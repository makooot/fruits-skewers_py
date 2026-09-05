import typing
import unittest

from fruits_skewers.skewer import parser
from fruits_skewers.types import SkewerCommandDetail
from fruits_skewers.types import SkewerShowHelpException
from fruits_skewers.types import SkewerShowVersionException
from fruits_skewers.types import SkewerValueError


class TestPackageSmart(unittest.TestCase):
    @typing.override
    def setUp(self):
        pass

    def test_empty(self):
        args = []
        command_detail: SkewerCommandDetail = {}
        result = parser(command_detail, args)
        self.assertEqual(result["ARGV"], [])

    def test_args_1(self):
        args = ["v1"]
        command_detail: SkewerCommandDetail = {}
        result = parser(command_detail, args)
        self.assertEqual(result["ARGV"], ["v1"])

    def test_args_2(self):
        args = ["v1", "v2"]
        command_detail: SkewerCommandDetail = {}
        result = parser(command_detail, args)
        self.assertEqual(result["ARGV"], ["v1", "v2"])

    def test_args_3(self):
        args = ["v1", "v2", "v3"]
        command_detail: SkewerCommandDetail = {}
        result = parser(command_detail, args)
        self.assertEqual(result["ARGV"], ["v1", "v2", "v3"])

    def test_short_bool(self):
        args = ["-b"]
        command_detail: SkewerCommandDetail = {
            "options": [{"key": "b", "type": "bool", "cmd": ["-b"]}]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["b"])

    def test_short_string_connected(self):
        args = ["-s=foo"]
        command_detail: SkewerCommandDetail = {
            "options": [{"key": "s", "type": "string", "cmd": ["-s"]}]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["s"], "foo")

    def test_short_string_seperated(self):
        args = ["-s", "foo"]
        command_detail: SkewerCommandDetail = {
            "options": [{"key": "s", "type": "string", "cmd": ["-s"]}]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["s"], "foo")

    def test_short_int_connected(self):
        args = ["-n=123"]
        command_detail: SkewerCommandDetail = {
            "options": [{"key": "n", "type": "int", "cmd": ["-n"]}]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["n"], 123)

    def test_short_int_seperated(self):
        args = ["-n", "123"]
        command_detail: SkewerCommandDetail = {
            "options": [{"key": "n", "type": "int", "cmd": ["-n"]}]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["n"], 123)

    def test_short_chain_bbb(self):
        args = ["-abc"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "c", "type": "bool", "cmd": ["-c"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["a"])
        self.assertTrue(result["b"])
        self.assertTrue(result["c"])

    def test_short_chain_bbs_empty(self):
        args = ["-abs="]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "c", "type": "bool", "cmd": ["-c"]},
                {"key": "s", "type": "string", "cmd": ["-s"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["a"])
        self.assertTrue(result["b"])
        self.assertEqual(result["s"], "")

    def test_short_chain_bbs_any(self):
        args = ["-abs=foo"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "c", "type": "bool", "cmd": ["-c"]},
                {"key": "s", "type": "string", "cmd": ["-s"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["a"])
        self.assertTrue(result["b"])
        self.assertEqual(result["s"], "foo")

    def test_short_chain_bbi(self):
        args = ["-abn=1234"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "a", "type": "bool", "cmd": ["-a"]},
                {"key": "b", "type": "bool", "cmd": ["-b"]},
                {"key": "n", "type": "int", "cmd": ["-n"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["a"])
        self.assertTrue(result["b"])
        self.assertEqual(result["n"], 1234)

    def test_long_bool(self):
        args = ["--allow"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "allow", "type": "bool", "cmd": ["--allow"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["allow"])

    def test_long_string_connected_empty(self):
        args = ["--prefix="]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "prefix", "type": "string", "cmd": ["--prefix"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["prefix"], "")

    def test_long_string_connected_any(self):
        args = ["--prefix=I:"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "prefix", "type": "string", "cmd": ["--prefix"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["prefix"], "I:")

    def test_long_string_seperated(self):
        args = ["--prefix", "I:"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "prefix", "type": "string", "cmd": ["--prefix"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["prefix"], "I:")

    def test_long_int_connected(self):
        args = ["--port=8080"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["port"], 8080)

    def test_long_int_seperated(self):
        args = ["--port", "8080"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["port"], 8080)

    def test_both_def_short(self):
        args = ["-p=8080"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["port"], 8080)

    def test_both_def_long(self):
        args = ["--port=8080"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertEqual(result["port"], 8080)

    def test_mix(self):
        args = ["-ap", "8080", "--prefix=BEEF", "jkl", "mno"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "allow", "type": "bool", "cmd": ["-a", "--allow"]},
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
                {"key": "prefix", "type": "string", "cmd": ["-x", "--prefix"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["allow"])
        self.assertEqual(result["prefix"], "BEEF")
        self.assertEqual(result["port"], 8080)
        self.assertEqual(result["ARGV"], ["jkl", "mno"])

    def test_double_hyphen(self):
        args = ["-ap", "8080", "--", "--prefix=BEEF", "jkl", "mno"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "allow", "type": "bool", "cmd": ["-a", "--allow"]},
                {"key": "prefix", "type": "string", "cmd": ["-x", "--prefix"]},
                {"key": "port", "type": "int", "cmd": ["-p", "--port"]},
            ]
        }
        result = parser(command_detail, args)
        self.assertTrue(result["allow"])
        self.assertEqual(result["port"], 8080)
        self.assertEqual(result["ARGV"], ["--prefix=BEEF", "jkl", "mno"])

    def test_short_invalid_name(self):
        args = ["-#"]
        command_detail: SkewerCommandDetail = {}
        with self.assertRaises(SkewerValueError):
            parser(command_detail, args)

    def test_short_undefined_name(self):
        args = ["-q"]
        command_detail: SkewerCommandDetail = {}
        with self.assertRaises(SkewerValueError):
            parser(command_detail, args)

    def test_long_invalid_name(self):
        args = ["--###-###"]
        command_detail: SkewerCommandDetail = {}
        with self.assertRaises(SkewerValueError):
            parser(command_detail, args)

    def test_invlid_int_1(self):
        args = ["--port", "0A"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(SkewerValueError):
            parser(command_detail, args)

    def test_invlid_int_2(self):
        args = ["--port=0A"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(SkewerValueError):
            parser(command_detail, args)

    def test_invlid_int_3(self):
        args = ["-p", "0A"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(SkewerValueError):
            parser(command_detail, args)

    def test_invlid_int_4(self):
        args = ["-p=0A"]
        command_detail: SkewerCommandDetail = {
            "options": [
                {"key": "port", "type": "int", "cmd": ["--port"]},
            ]
        }
        with self.assertRaises(SkewerValueError):
            parser(command_detail, args)

    def test_invalid_name_1(self):
        args = ["--verbose"]
        with self.assertRaises(SkewerValueError):
            parser({}, args)

    def test_invalid_name_2(self):
        args = ["-v"]
        with self.assertRaises(SkewerValueError):
            parser({}, args)

    def test_short_showhelp_exception(self):
        args = ["-h"]
        command_detail: SkewerCommandDetail = {}
        with self.assertRaises(SkewerShowHelpException):
            parser(command_detail, args)

    def test_long_showhelp_exception(self):
        args = ["--help"]
        command_detail: SkewerCommandDetail = {}
        with self.assertRaises(SkewerShowHelpException):
            parser(command_detail, args)

    def test_long_showversion_exception(self):
        args = ["--version"]
        command_detail: SkewerCommandDetail = {}
        with self.assertRaises(SkewerShowVersionException):
            parser(command_detail, args)
