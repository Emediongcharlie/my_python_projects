numbers = [5,7,2,1,8,3]

for number in range(len(numbers) - 1):
    for item in range(len(numbers) - number - 1):
        if numbers[item] > numbers[item + 1]:
            temp = numbers[item]
            numbers[item] = numbers[item + 1]
            numbers[item + 1] = temp
print(numbers)
