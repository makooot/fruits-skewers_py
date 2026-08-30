import typing
import unittest

from fruits_skewers import parser_minimum


class TestParserMinimum(unittest.TestCase):
    @typing.override
    def setUp(self):
        pass

    def test_empty_argv(self):
        args = []
        result = parser_minimum.parser(args)
        self.assertEqual(result["ARGV"], [])

    def test_named_0_args_1(self):
        args = ["v1"]
        result = parser_minimum.parser(args)
        self.assertEqual(result["ARGV"], ["v1"])

    def test_named_0_args_2(self):
        args = ["v1", "v2"]
        result = parser_minimum.parser(args)
        self.assertEqual(result["ARGV"], ["v1", "v2"])

    def test_named_0_args_3(self):
        args = ["v1", "v2", "v3"]
        result = parser_minimum.parser(args)
        self.assertEqual(result["ARGV"], ["v1", "v2", "v3"])

    def test_short_null(self):
        args = ["-a"]
        result = parser_minimum.parser(args)
        self.assertIsNone(result["a"])

    def test_short_len_0(self):
        args = ["-a="]
        result = parser_minimum.parser(args)
        self.assertEqual(result["a"], "")

    def test_short_anystring(self):
        args = ["-a=foo"]
        result = parser_minimum.parser(args)
        self.assertEqual(result["a"], "foo")

    def test_short_chain_null(self):
        args = ["-abc"]
        result = parser_minimum.parser(args)
        self.assertIsNone(result["a"])
        self.assertIsNone(result["b"])
        self.assertIsNone(result["c"])

    def test_short_chain_len_0(self):
        args = ["-abc="]
        result = parser_minimum.parser(args)
        self.assertIsNone(result["a"])
        self.assertIsNone(result["b"])
        self.assertEqual(result["c"], "")

    def test_short_chain_anystring(self):
        args = ["-abc=foo"]
        result = parser_minimum.parser(args)
        self.assertIsNone(result["a"])
        self.assertIsNone(result["b"])
        self.assertEqual(result["c"], "foo")

    def test_long_null(self):
        args = ["--abc-def"]
        result = parser_minimum.parser(args)
        self.assertIsNone(result["abc-def"])

    def test_long_len_0(self):
        args = ["--abc-def="]
        result = parser_minimum.parser(args)
        self.assertEqual(result["abc-def"], "")

    def test_long_anystring(self):
        args = ["--abc-def=foo"]
        result = parser_minimum.parser(args)
        self.assertEqual(result["abc-def"], "foo")

    def test_mix(self):
        args = ["--abc", "--def=123", "-ghi=boo", "jkl", "mno"]
        result = parser_minimum.parser(args)
        self.assertIsNone(result["abc"])
        self.assertEqual(result["def"], "123")
        self.assertIsNone(result["g"])
        self.assertIsNone(result["h"])
        self.assertEqual(result["i"], "boo")
        self.assertEqual(result["ARGV"], ["jkl", "mno"])

    def test_double_hyphen(self):
        args = ["--abc", "--def=123", "--", "-ghi=boo", "jkl", "mno"]
        result = parser_minimum.parser(args)
        self.assertIsNone(result["abc"])
        self.assertEqual(result["def"], "123")
        self.assertEqual(result["ARGV"], ["-ghi=boo", "jkl", "mno"])

    def test_short_invalid_name(self):
        args = ["-#"]
        with self.assertRaises(ValueError):
            parser_minimum.parser(args)

    def test_long_invalid_name(self):
        args = ["--###-###"]
        with self.assertRaises(ValueError):
            parser_minimum.parser(args)

    def test_short_showhelp_exception(self):
        args = ["-h"]
        with self.assertRaises(parser_minimum.types.ShowHelpException):
            parser_minimum.parser(args)

    def test_long_showhelp_exception(self):
        args = ["--help"]
        with self.assertRaises(parser_minimum.types.ShowHelpException):
            parser_minimum.parser(args)

    def test_long_showversion_exception(self):
        args = ["--version"]
        with self.assertRaises(parser_minimum.types.ShowVersionException):
            parser_minimum.parser(args)
