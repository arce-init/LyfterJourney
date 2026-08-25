import unittest
from my_module.number_functions import sum_numbers, get_average, celsius_to_fahrenheit


class TestNumberFunctions(unittest.TestCase):

    # --- sum_numbers ---

    def test_sum_numbers_with_positive_numbers(self):
        a = 5
        b = 3
        result = sum_numbers(a, b)
        self.assertEqual(result, 8)

    def test_sum_numbers_with_negative_numbers(self):
        a = -5
        b = -3
        result = sum_numbers(a, b)
        self.assertEqual(result, -8)

    def test_sum_numbers_with_zeros(self):
        a = 0
        b = 0
        result = sum_numbers(a, b)
        self.assertEqual(result, 0)

    # --- get_average ---

    def test_get_average_with_positive_numbers(self):
        numbers_list = [10, 20, 30]
        result = get_average(numbers_list)
        self.assertEqual(result, 20)

    def test_get_average_with_negative_numbers(self):
        numbers_list = [-10, -20, -30]
        result = get_average(numbers_list)
        self.assertEqual(result, -20)

    def test_get_average_with_zeros(self):
        numbers_list = [0, 0, 0]
        result = get_average(numbers_list)
        self.assertEqual(result, 0)

    # --- celsius_to_fahrenheit ---

    def test_celsius_to_fahrenheit_with_positive_number(self):
        celsius = 100
        result = celsius_to_fahrenheit(celsius)
        self.assertEqual(result, 212)

    def test_celsius_to_fahrenheit_with_negative_number(self):
        celsius = -40
        result = celsius_to_fahrenheit(celsius)
        self.assertEqual(result, -40)

    def test_celsius_to_fahrenheit_with_zero(self):
        celsius = 0
        result = celsius_to_fahrenheit(celsius)
        self.assertEqual(result, 32)


if __name__ == '__main__':
    unittest.main()