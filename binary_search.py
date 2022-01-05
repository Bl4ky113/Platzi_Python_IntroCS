objective = int(input("Please Enter a Number:  "))
epsilon = 0.00001
down_point = 0.0
high_point = max(1.0, objective)
answer = (high_point + down_point) / 2

while abs((answer ** 2) - objective) >= epsilon:
    if (answer ** 2) < objective:
        down_point = answer
    else:
        high_point = answer

    answer = (high_point + down_point) / 2
    print(f"answer={answer}, difference={abs((answer ** 2) - objective)}, down={down_point}, high={high_point}")

print(f"The Square Root of the Number {objective} is: {answer}")
print(answer ** 2)