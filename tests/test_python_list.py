import unittest
# from python_list import even_numbers
# from multiples import multiply_elements
from len_function import len_function


# class MyTestCase(unittest.TestCase):
#     def test_that_numbers_are_even_numbers(self):
#        # result = even_numbers([1,2,3,4,5,6,7,8,9,10])
#         self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10]), [2,4,6,8,10])  # add assertion here
#
class MyTestCase(unittest.TestCase):
    # def test_that_elements_are_multiplied(self):
    #     self.assertEqual(multiply_elements([2,3,5,2,5,3]), [4,6,10,4,10,6])

    def test_that_it_can_count(self):
       self.assertEqual(len_function("emediong"), 8)

if __name__ == '__main__':
    unittest.main()
