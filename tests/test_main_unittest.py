import unittest
from main import calculate_offset


class TestCalculateOffset(unittest.TestCase):
    def test_gain(self):
        offset, message = calculate_offset(20)
        self.assertEqual(offset, -16.67)
        self.assertEqual(message, "You need a 16.67% loss to offset your 20% gain")

    def test_loss(self):
        offset, message = calculate_offset(-20)
        self.assertEqual(offset, 25.0)
        self.assertEqual(message, "You need a 25.0% gain to offset your 20% loss")

    def test_no_change(self):
        offset, message = calculate_offset(0)
        self.assertEqual(offset, 0.0)
        self.assertEqual(message, "You need a 0.0% gain to offset your 0% loss")

    def test_large_gain(self):
        offset, message = calculate_offset(100)
        self.assertEqual(offset, -50.0)
        self.assertEqual(message, "You need a 50.0% loss to offset your 100% gain")

    def test_large_loss(self):
        offset, message = calculate_offset(-50)
        self.assertEqual(offset, 100.0)
        self.assertEqual(message, "You need a 100.0% gain to offset your 50% loss")


if __name__ == "__main__":
    unittest.main()
