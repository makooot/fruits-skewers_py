import typing
import unittest

import fruits_skewers.helper


class TestPackageHelper(unittest.TestCase):
    @typing.override
    def setUp(self):
        pass

    def test_strtobool_true(self):
        self.assertTrue(fruits_skewers.helper.strtobool("y"))
        self.assertTrue(fruits_skewers.helper.strtobool("yes"))
        self.assertTrue(fruits_skewers.helper.strtobool("t"))
        self.assertTrue(fruits_skewers.helper.strtobool("true"))
        self.assertTrue(fruits_skewers.helper.strtobool("on"))
        self.assertTrue(fruits_skewers.helper.strtobool("1"))
        self.assertTrue(fruits_skewers.helper.strtobool("anything else"))

    def test_strtobool_false(self):
        self.assertFalse(fruits_skewers.helper.strtobool("n"))
        self.assertFalse(fruits_skewers.helper.strtobool("no"))
        self.assertFalse(fruits_skewers.helper.strtobool("f"))
        self.assertFalse(fruits_skewers.helper.strtobool("false"))
        self.assertFalse(fruits_skewers.helper.strtobool("off"))
        self.assertFalse(fruits_skewers.helper.strtobool("0"))
        self.assertFalse(fruits_skewers.helper.strtobool(""))
