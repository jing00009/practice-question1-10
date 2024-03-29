"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""

def case_counter(text):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0

    # Iterate through each character in the string
    for char in text:
        # Check if the character is alphabetic
        if char.isalpha():
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1

    # Print the counts or 0 if no letters of a particular case are found
    if uppercase_count > 0:
        print("Uppercase letters:", uppercase_count)
    else:
        print("Uppercase letters: 0")

    if lowercase_count > 0:
        print("Lowercase letters:", lowercase_count)
    else:
        print("Lowercase letters: 0")



print(case_counter("Hello World"))
print(case_counter("PYTHON"))
print(case_counter("python"))
print(case_counter("1234!@#$"))


