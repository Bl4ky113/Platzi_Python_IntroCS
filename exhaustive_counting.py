import time

time.time()

objective = int(input("Enter a Number, which may have a square root:  "))
result = 0

while (result ** 2) < objective:
    result += 1

if (result ** 2) == objective:
    print(f"The Square root of the number {objective} is: {result}")
else:
    print(f"There isn't a exact square root of the number {objective}")

print(f"This Program took {time.time()} seconds")