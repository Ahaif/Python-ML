import string
import sys

def text_analyzer(input_text=None):
    """
    Analyze a text and display the sums of its upper-case characters, lower-case characters, punctuation characters,
    and spaces.

    Args:
    input_text (str): The text to be analyzed.

    Returns:
    None
    """

    # Check if input_text is None or an empty string
    if input_text is None or not input_text:
        input_text = input("Please provide a string: ")

    # Check if the input_text is a string
    if not isinstance(input_text, str):
        print("Error: Input is not a valid string.")
        return

    # Initialize counts
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0

    for char in input_text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isspace():
            space_count += 1

    # Display the results
    print(f"Number of uppercase characters: {upper_count}")
    print(f"Number of lowercase characters: {lower_count}")
    print(f"Number of punctuation characters: {punctuation_count}")
    print(f"Number of spaces: {space_count}")


    if __name__ == "__main__":
        if len(sys.argv) > 1:
            print("ERROR: MORE THAN ONE ARGS")
            return
        else:   
            text_analyzer(sys.argv[1])

# Test the function
# text_analyzer("Hello, World! This is a test.")
