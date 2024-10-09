import unittest
from task_5 import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle_1 = Rectangle(5, 4)
        self.rectangle_2 = Rectangle(8, 1)
        self.rectangle_3 = Rectangle(3, 2)

    def test_equal(self):
        self.assertEqual(self.rectangle_1, self.rectangle_2)

    def test_lt(self):
        self.assertTrue(self.rectangle_3 < self.rectangle_1)

    def test_lt_(self):
        self.assertTrue(self.rectangle_2 > self.rectangle_3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
