def creating_a_set(*numbers):
    given_set = set(numbers)
    return given_set

print(creating_a_set(2,3,6,3,8,2,9,4,5,7,5))

def sum_collections(*numbers):
    sum_elements = 0
    given_set = set(numbers)
    for numbers in given_set:
        sum_elements = sum_elements + numbers
    return sum_elements

print(sum_collections(2,3,4,5,6,7,8,9))

# def remove_items(numbers):
#     element = 0
#     given_number = set(numbers)
#     for numbers in given_number:
#         if numbers == element:
#             numbers.remove(numbers)
#         else:
#             "none"
#     return numbers
#
# numbers = {2,3,4,5,6,7,8,9}
# numbers.remove(3)
# print(remove_items(numbers))

number1 = {2,3,7,8,4}
number2 = {2,4,7,5}

def intersection_in_set(set1,set2):

    result = set1.intersection(set2)
    return result

print(intersection_in_set(number1, number2))

def union_in_set(set1,set2):

    result = set1.union(set2)
    return result

print(union_in_set(number1,number2))

def subset_in_set(set1,set2):

    result = set1.issubset((set2))
    return result

print(subset_in_set(number1,number2))

def remove_element(number):
    result = number.clear()
    return result

print(remove_element(number1))

def min_max_values(number):
    minimum_number = 0
    maximum_number = [0]

    for count in number:
        if number > maximum_number:
            maximum_number = number
    return maximum_number

print(min_max_values(number1))

def find_length_of_number(numbers):
    count = 0
    for number in numbers:
        count = count + 1
    return count

print(find_length_of_number("emediong",)
)

