import random

numbers_list = []


def count_random_numbers():
    random.seed(50)

    for numbers in range(10):
        random_number = random.randrange(1, 50)
        numbers_list.append(random_number)
    return numbers_list


print(count_random_numbers())

def count_numbers():
    count = 0
    for item in numbers_list:
        count = count + 1
    return count

print(count_numbers())

def sum_of_even_numbers():
    even_sum = 0
    for numbers in numbers_list:
        if numbers % 2 == 0:
            even_sum = even_sum + numbers
    return even_sum

print(sum_of_even_numbers())

def sum_of_odd_numbers():
    odd_numbers = 0
    for numbers in numbers_list:
        if numbers % 2 == 1:
            odd_numbers = odd_numbers + numbers
    return odd_numbers

print(sum_of_odd_numbers())

def multiply_element_at_third_position():
    third_position = 1
    for numbers in numbers_list:
        if numbers % 3 == 0:
            third_position = third_position * numbers
    return third_position

print(multiply_element_at_third_position())

def average_of_all_element():
    sum_of_numbers = 0
    average = 0
    for numbers in numbers_list:
        sum_of_numbers = sum_of_numbers + numbers
        average = sum_of_numbers / len(numbers_list)
    return average

print(average_of_all_element())

def largest_number():
    largest = 0
    for numbers in numbers_list:
        if numbers > largest:
            largest = numbers
    return largest

print(largest_number())





