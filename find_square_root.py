def exhaustive_counting (number):
    result = 0

    while (result ** 2) < number:
        result += 1

    if (result ** 2) == number:
        return result
    else: 
        return None

def approximate_solutions (number):
    result = 0
    epsilon = 0.001
    step = epsilon ** 2

    while abs((result ** 2) - number) >= epsilon and result <= number:
        result += step
    
    if abs((result ** 2) - number) >= epsilon:
        return None
    else:
        return result

def bisector_binary_search (number):
    epsilon = 0.001
    bottom_point = 0
    high_point = max(1.0, number)
    result = (bottom_point + high_point) / 2

    while abs((result ** 2) - number) >= epsilon:
        if (result ** 2) > number:
            high_point = result
        else:
            bottom_point = result

        result = (bottom_point + high_point) / 2

    return result

number_to_find = int(input("Enter a Number to find its Square Root:  "))
print(f"""
    Available Functions to find the Square Root of {number_to_find}:
        - 1: Exhaustive Counting
        - 2: Approxiamte Solutions
        - 3: Bisector Binary Search
""")
function_to_use = input("Use Function N°:  ")
result_square_root = 0

if function_to_use == "1":
    result_square_root = exhaustive_counting(number_to_find)
elif function_to_use == "2":
    result_square_root = approximate_solutions(number_to_find)
elif function_to_use == "3":
    result_square_root = bisector_binary_search(number_to_find)
else: 
    print("Please Enter an option from the menu")

if result_square_root:
    print(f"The Square Root of {number_to_find} is:  {result_square_root}")
    print(result_square_root ** 2)
else:
    print(f"The Square Root of {number_to_find} not found. Try another Function.")