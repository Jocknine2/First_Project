import unittest
from models.shop import Shop


class Testshop(unittest.Testcase):
    def setup(self):

        self.shop = Shop([], [], 2000)
