import typing
import unittest

from fruits_skewers.helper import strtobool


class TestHelperHelper(unittest.TestCase):
    @typing.override
    def setUp(self):
        pass

    def test_strtobool_true(self):
        self.assertTrue(strtobool("y"))
        self.assertTrue(strtobool("yes"))
        self.assertTrue(strtobool("t"))
        self.assertTrue(strtobool("true"))
        self.assertTrue(strtobool("on"))
        self.assertTrue(strtobool("1"))
        self.assertTrue(strtobool("anything else"))
        self.assertTrue(strtobool("Y"))
        self.assertTrue(strtobool("Yes"))
        self.assertTrue(strtobool("T"))
        self.assertTrue(strtobool("True"))
        self.assertTrue(strtobool("On"))

    def test_strtobool_false(self):
        self.assertFalse(strtobool("n"))
        self.assertFalse(strtobool("no"))
        self.assertFalse(strtobool("f"))
        self.assertFalse(strtobool("false"))
        self.assertFalse(strtobool("off"))
        self.assertFalse(strtobool("0"))
        self.assertFalse(strtobool(""))
        self.assertFalse(strtobool("N"))
        self.assertFalse(strtobool("No"))
        self.assertFalse(strtobool("F"))
        self.assertFalse(strtobool("False"))
        self.assertFalse(strtobool("Off"))
