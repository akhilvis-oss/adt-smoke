import unittest

from smoke_add import add


class TestAdd(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_zero_integers(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(4, 0), 4)

    def test_negative_integers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(2, -3), -1)


if __name__ == "__main__":
    unittest.main()
