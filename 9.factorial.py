def calculate_factorial(number):
    # Check for edge cases
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif number == 0:
        return 1

    # Initialize the factorial result to 1
    factorial_result = 1

    # Calculate the factorial using a for loop
    for i in range(1, number + 1):
        factorial_result *= i

    return factorial_result
print(calculate_factorial(5)) 
print(calculate_factorial(0))  
print(calculate_factorial(3))

try:
    calculate_factorial(-1)
except ValueError as e:
    print(str(e))

