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
    
    def test_radd(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        result = 4.0 + v1
        expected_values = [[5.0], [6.0], [7.0]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)
    
    def test_subtraction_same_shape(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        v2 = Vector([[4.0], [5.0], [6.0]])
        result = v1 - v2
        expected_values = [[-3.0], [-3.0], [-3.0]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)

    def test_subtraction_different_shape(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        v2 = Vector([[4.0], [5.0]])
        
        with self.assertRaises(ValueError):
            result = v1 - v2

    def test_rsub(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        result = 4.0 - v1
        expected_values = [[3.0], [2.0], [1.0]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)
    
    def test_multiplication(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        result = v1 * 3
        expected_values = [[3.0], [6.0], [9.0]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)
    
    def test_rmul(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        result = 3 * v1
        expected_values = [[3.0], [6.0], [9.0]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)

    def test_division(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        result = v1 / 3
        expected_values = [[1/3], [2/3], [3/3]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)
    
    def test_rdiv(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        result = 3 / v1
        expected_values = [[3.0], [1.5], [1.0]]
        expected_shape = (3, 1)

        self.assertEqual(result.values, expected_values)
        self.assertEqual(result.shape, expected_shape)
    
    def test_dot(self):
        v1 = Vector([[1.0], [2.0], [3.0]])
        v2 = Vector([[4.0], [5.0], [6.0]])
        result = v1.dot(v2)
        expected = 32.0

        self.assertEqual(result, expected)
    
  

if __name__ == '__main__':
    unittest.main()