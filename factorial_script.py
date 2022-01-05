def factorial_function (num):
    """ Gets a Number and calculates the factorial of it, using recursivity
        num, int > 0
        returns num!
    """
    result = 1

    if num != 1:
        result = num * (factorial_function(num - 1))
    
    return result

number_to_calc = int(input("Enter a Number to get its factorial:  "))
result_factorial = factorial_function(number_to_calc)

print(f"The Factorial of {number_to_calc} is: {result_factorial}")