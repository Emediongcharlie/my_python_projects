import unittest

from src.Roasted_corn.set_collections import creating_a_set, sum_collections, intersection_in_set, union_in_set, \
    subset_in_set, remove_element


class MyTestCase(unittest.TestCase):
    def test_creation_of_set(self):
        self.assertEqual(creating_a_set(), {2, 3, 4, 5, 6, 7, 8, 9}) # add assertion here
    def test_sum_can_be_collected(self):
        self.assertEqual(sum_collections(), 44)
    def test_set_intersection_in_active(self, set1, set2):
        self.assertEqual(intersection_in_set(self.set1,self.set2), {2, 4, 7})
    def test_union_in_set_is_active(self):
        self.assertEqual(union_in_set(number1,number2), {2, 3, 4, 5, 7, 8})

    def test_function_can_find_subset_in_set(self):
        self.assertEqual(subset_in_set(number1,number2),False)

    def test_function_can_remove_element(self):
        self.assertEqual(remove_element(number), None)


if __name__ == '__main__':
    unittest.main()
