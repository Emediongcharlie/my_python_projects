def sequential_list_of_numbers():

    number = []

    for numbers in range(1,16):
        number.append(numbers)
    return number

print(sequential_list_of_numbers())


def duplicate_numbers():
    number = []
    for numbers in range(1,16):
        for items in range(2):
            number.append(numbers)
    return number

print(duplicate_numbers())

# def eliminate_duplicate():
#     number = []
#     for numbers in

def add_third_element():
    number = []
    sum_number = 0
    for numbers in range(1,16):
        if numbers % 3 == 0:
            sum_number = sum_number + numbers
    return sum_number

print(add_third_element())

# def sum_of_selected_element():
#     for numbers in range(1,16):
#         add_numbers = numbers[1] + numbers[7] + numbers[- 1]
#     return add_numbers

# print(sum_of_selected_element())





