import unittest

from roasted_corn.random_numbers import count_random_numbers,count_numbers,sum_of_even_numbers,sum_of_odd_numbers



class MyTestCase(unittest.TestCase):
    def test_random_numbers_selected(self):
        self.assertEqual(count_random_numbers(), [32, 18, 24, 41, 16, 45, 31, 50, 22, 6])

    def test_length_of_number(self):
        self.assertEqual(count_numbers(), 10)

    def test_sum_of_even_numbers(self):
        self.assertEqual(sum_of_even_numbers(), 168)

    def test_sum_of_odd_numbers(self):
        self.assertEqual(sum_of_odd_numbers(),117)




if __name__ == '__main__':
    unittest.main()
