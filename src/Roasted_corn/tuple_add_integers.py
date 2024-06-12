
new_numbers = (1,2,3,4,5,6,7,8,9)
def add_integers_to_a_tuple():
    tuple1 = ()
    numbers = list(tuple1)
    for number in range(1,21):
        numbers.append(number)
    return tuple(numbers)

print(add_integers_to_a_tuple())

def sum_of_elements_at_odd_positions():
    tuple1 = ()
    numbers = list(tuple1)
    sum = 0
    for number in range(1, 21):
        if number % 2 == 1:
            sum = sum + number
            numbers.append(number)
    return sum

print(sum_of_elements_at_odd_positions())

def sum_of_elements_at_even_positions():
    tuple1 = ()
    numbers = list(tuple1)
    sum = 0
    for number in range(1, 21):
        if number % 2 == 0:
            sum = sum + number
            numbers.append(number)
    return sum

print(sum_of_elements_at_even_positions())

def sum_of_smallest_and_highest_element():
    tuple1 = ()
    numbers = list(tuple1)
    sum = 0
    largest = 0
    smallest = 0
    digits = range(1,21)
    for number in digits:
        numbers.append(number)
        tuple2 = tuple(numbers)
        if number > largest:
            largest = number
        if largest < number:
            smallest = number

        sum = largest + smallest
    return sum


print(sum_of_smallest_and_highest_element())

def unpacking_tuples():
    tuple1 = ()
    numbers = list(tuple1)
    for number in range(1, 21):
        numbers.append(number)
        tuple2 = tuple(numbers)

        num1, num2, num3, num4, num5, *num = new_numbers

    return num1,num2,num3,num4,num5

print(unpacking_tuples())

