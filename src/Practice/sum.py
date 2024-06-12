numbers = [2,5,4,7,5,8,3]
sum = 0

for i in range(len(numbers)):
    sum = sum + numbers[i]

    average = sum / len(numbers)


print(sum)
print(f'{average:.2f}')