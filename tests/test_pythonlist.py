# from python_list import even_numbers
# from list_journey import appending
from len_function import len_function
# rom multiples import multiply_elements


# def test_that_the_number_is_even():
#     num = [1,2,3,4,5,6,7,8,9,10]
#     assert even_numbers(num) == [2,4,6,8,10]
#
# def test_number_is_even_():
#     #lst = [1,2,3,4,5,6,7,8,9,10]
#     assert even_numbers([1,2,3,4,5,6,7,8,9,10]) == [2,4,6,8,10]
#
# def test_number_appends():
#     my_list = [1,2,3,4,5]
#     assert appending([my_list]) == [1,2,3,4,5]

# def test_multiplication_of_elements():
#     digits = [2, 3, 5, 2, 5, 3]
#     assert multiply_elements(digits) == [4, 6, 10, 4, 10, 6]


def test_that_it_can_count():
    name = "emediong"
    assert len_function(name) == 8
