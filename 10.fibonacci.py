def fibonacci_sequence(max_value):
    # Handle edge cases for 0 and negative inputs
    if max_value <= 0:
        return [0]

    # Initialize the Fibonacci sequence
    sequence = [0, 1]

    # Generate the Fibonacci sequence using a while loop
    while sequence[-1] + sequence[-2] <= max_value:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence


print(fibonacci_sequence(10))  
print(fibonacci_sequence(1))   
print(fibonacci_sequence(7))   
print(fibonacci_sequence(-1))




