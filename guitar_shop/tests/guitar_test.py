import unittest
from models.guitar import Guitar


class TestGuitar(unittest.TestCase):
    def setup(self):
        self.guitar = Guitar("x106s", "Axe", 250, 599, "6 string, 24 frets")

    def test_guitar_has_model(self):
        self.assertEqual("x106s", self.guitar.model)
