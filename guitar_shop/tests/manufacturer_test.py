import unittest
from models.manufacturer import Manufacturer


class TestManufacturer(unittest.Testcase):
    def setup(self):

        self.manufacturer = Manufacturer("ESP")

    def test_get_mfctr_name(self):
        self.assertEqual("ESP", self.manufacturer.name)
