# Define a dictionary to map alphanumeric characters to Morse code

import sys

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

def text_to_morse(text):
    morse_code = ""
    for char in text:
        char = char.upper()
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += '/ '
    return morse_code

def main():
    if len(sys.argv) > 1:
        # Merge command-line arguments into a single string
        input_text = ' '.join(sys.argv[1:])
        encoded_text = text_to_morse(input_text)
        print(encoded_text)
    else:
        # Print usage if no arguments provided
        print("Usage: python morse_code_encoder.py <text to encode>")


if __name__ == '__main__':
    main()