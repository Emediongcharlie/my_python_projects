def sum_of_odd_integers_in_tuple():
    tuple1 = ()
    sum_element = 0

    for numbers in range(1,21):
        if numbers % 2 == 1:
            sum_element = sum_element + numbers
    return sum_element

print(sum_of_odd_integers_in_tuple())

def sum_of_even_integers_in_tuple():
    sum_element = 0

    for numbers in range(1, 21):
        if numbers % 2 == 0:
            sum_element = sum_element + numbers
    return sum_element

print(sum_of_even_integers_in_tuple())

def sum_of_highest_and_lowest_element():
    numbers = range(1,21)
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number
    sum_of_numbers = largest + smallest
    return sum_of_numbers

print(sum_of_highest_and_lowest_element())

# def unpacking_of_first_five_elements():
#     numbers = range(1,21)
#     for number in numbers:
#         nu


