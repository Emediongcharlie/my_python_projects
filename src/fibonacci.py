print("Welcome to Python")
#fibonnaci
count = 0
a = 0
b = 1
next_number = a
for items in range(13):
    print(next_number, end=", ")
    a, b = b, next_number
    next_number = a + b