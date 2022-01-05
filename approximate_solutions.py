objective = int(input("Enter a Number:  "))
epsilon = 0.005
step = epsilon ** 2
answer = 0

while abs((answer ** 2) - objective) >= epsilon and answer <= objective:
    print(abs((answer ** 2 ) - objective), answer)
    answer += step

if abs((answer ** 2) - objective) >= epsilon:
    print(f"Square Root of {objective}, not found")
else: 
    print(f"The Square Root of {objective} is: {answer}")