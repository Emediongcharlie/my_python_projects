
# number = []
#
# for index in range(4):
#   for count in range(5):
#        print(number[index][count], end='')

def even_numbers(number):
    numbers = []

    for count in number:
        if count % 2 == 0:
            numbers.append(count)
    return numbers


lst = []
for i in range(1, 51):
    lst.append(i)

print(even_numbers(lst))

num = list(range(1,51))
print(num)
print(even_numbers(num))

