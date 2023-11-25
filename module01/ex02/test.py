import unittest
from vector import Vector  # Assuming your Vector class is in a file named 'vector.py'

class TestVectorAddition(unittest.TestCase):
    def test_addition_same_shape(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        v2 = Vector([[4.0], [5.0], [6.0]])
        result = v1 + v2
        expected_values = [[5.0], [7.0], [9.0]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)

    def test_addition_different_shape(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        v2 = Vector([[4.0], [5.0]])
        
        with self.assertRaises(ValueError):
            result = v1 + v2

if __name__ == '__main__':
    unittest.main()
