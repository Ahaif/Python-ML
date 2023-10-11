import sys

def reverse_and_swap_case(text):
    reversed_text = text[::-1]
    swapped_case_text = ''.join(c.upper() if c.islower() else c.lower() for c in reversed_text)
    return swapped_case_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python reverse_swap_case.py <string>")
        return
    
    input_string = ' '.join(sys.argv[1:])
    result = reverse_and_swap_case(input_string)
    print(result)

if __name__ == "__main__":
    main()


