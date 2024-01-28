"""
Morse Code Translator Function

Objective:
Write a function named 'morse_translator' that translates a given string into Morse code.

Function Parameter:
text (string): The string to be translated into Morse code.

Instructions:
- Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
- The Morse code for each character should be separated by a space.
- Each word in the string should be separated by a forward slash (/).
- The function should handle both uppercase and lowercase alphabetic characters.
- The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
- Non-alphabetic characters (like numbers or symbols) should not be translated.
- https://en.wikipedia.org/wiki/Morse_code

Example Test Cases:
1. morse_translator("HELLO WORLD") should return the Morse code for the given string.
2. morse_translator("Python") should return the Morse code for the given string.
3. morse_translator("Morse Code") should return the Morse code for the given string.
"""


def morse_translator(input_string):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
    }

    morse_code = []
    words = input_string.split()

    for word in words:
        morse_word = []
        for char in word:
            if char.upper() in morse_code_dict:
                morse_word.append(morse_code_dict[char.upper()])
        morse_code.append(' '.join(morse_word))

    return '/'.join(morse_code)




print(
    morse_translator("HELLO WORLD")
)  
print(morse_translator("Python"))  
print(
    morse_translator("Morse Code")
)  
