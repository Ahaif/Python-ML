import sys


kata = "The right format"

# Calculate the number of dashes needed to reach a total length of 42

def main():
    num_dashes = 41 - len(kata)

    # Create the formatted string by adding dashes before the content
    formatted_string = "-" * num_dashes + kata
    print(formatted_string)



if __name__ == "__main__":
    main()