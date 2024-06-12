import unittest

from src.Roasted_corn.random_numbers import count_random_numbers, count_numbers, sum_of_even_numbers, \
    sum_of_odd_numbers, multiply_element_at_third_position, average_of_all_element, largest_number


class MyTestCase(unittest.TestCase):
    def test_number_is_random(self):
        self.assertEqual(count_random_numbers(), [32, 18, 24, 41, 16, 45, 31, 22, 6, 35])

    def test_length_of_number(self):
        self.assertEqual(count_numbers(), 10)

    def test_sum_of_even_numbers(self):
        self.assertEqual(sum_of_even_numbers(), 118)

    def test_sum_of_odd_numbers(self):
        self.assertEqual(sum_of_odd_numbers(), 152)

    def test_it_can_multiply_at_third_indexes(self):
        self.assertEqual(multiply_element_at_third_position(), 116640)

    def test_average_of_all_element(self):
        self.assertEqual(average_of_all_element(), 27.0)

    def test_the_largest_number(self):
        self.assertEqual(largest_number(), 45)


if __name__ == '__main__':
    unittest.main()
