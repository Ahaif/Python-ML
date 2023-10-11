import sys
import string

def text_analyzer(input_argument):
    print(f"The text contains {len(input_argument)} characters:")

    if not isinstance(input_argument, str):
        print("ERROR: Provide a single string argument")
        return

    count_upper = 0
    count_lower = 0
    count_space = 0
    count_punctuation = 0

    for c in input_argument:
        if c.isalpha():
            if c.isupper():
                count_upper += 1
            elif c.islower():
                count_lower += 1
        elif c.isspace():
            count_space += 1
        elif c in string.punctuation:
            count_punctuation += 1

    print(f"Uppercase letters: {count_upper}")
    print(f"Lowercase letters: {count_lower}")
    print(f"Spaces: {count_space}")
    print(f"Punctuation characters: {count_punctuation}")

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("ERROR: Provide a single string argument")
    else:
        input_argument = sys.argv[1]
        text_analyzer(input_argument)
