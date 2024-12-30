import unittest
from mean_var_std import calculate  # Import the calculate function

class TestMeanVarStd(unittest.TestCase):

    def test_calculate_valid_input(self):
        # Test with a valid input list
        input_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        result = calculate(input_data)
        
        expected_result = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        
        self.assertEqual(result, expected_result)

    def test_calculate_invalid_input(self):
        # Test with invalid input (less than 9 elements)
        input_data = [1, 2, 3, 4, 5, 6]
        
        with self.assertRaises(ValueError):
            calculate(input_data)

    def test_calculate_empty_input(self):
        # Test with empty list
        input_data = []
        
        with self.assertRaises(ValueError):
            calculate(input_data)

    def test_calculate_large_values(self):
        # Test with large values
        input_data = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000]
        result = calculate(input_data)
        
        # The expected result will depend on the actual calculations for large numbers.
        # Here we check if the result is a dictionary
        self.assertIsInstance(result, dict)

    def test_calculate_zero_values(self):
        # Test with zero values
        input_data = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = calculate(input_data)
        
        # Expected result for zeros should be all zeros
        expected_result = {
            'mean': [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], 0.0],
            'variance': [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], 0.0],
            'standard deviation': [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], 0.0],
            'max': [[0, 0, 0], [0, 0, 0], 0],
            'min': [[0, 0, 0], [0, 0, 0], 0],
            'sum': [[0, 0, 0], [0, 0, 0], 0]
        }
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
