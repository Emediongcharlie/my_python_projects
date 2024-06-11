from collections import Counter


# digits = [2, 3, 5, 2, 5, 3]
#
#
# def multiply_elements(numbers):
#     new_numbers = []
#     for element in numbers:
#         new_numbers.append(element * 2)
#     return new_numbers
#
# print(multiply_elements(digits))


#DICTIONARIES

days_in_months = {31: 'january', 'february': 28, 'march':30}
for month, days in days_in_months.items():
    print(f'{month} has {days}days')

for months in days_in_months.keys():
    print(months, end=" ")

text = ('this is a car and the car is fine and the fine car is good')

Counter = Counter(text.split())

for word, count in sorted(Counter.items()):
    print(f"{word:<12}{count}")





