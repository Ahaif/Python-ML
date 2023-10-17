import sys

def main():
    if len(sys.argv) >= 4 or len(sys.argv) < 3:
        print("ERROR: ARGS should be 2")
        return
    else:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
        if str1.isalpha()or str2.isalpha():
            print("ERROR: ARGS should be numbers")
        else:
            print("Sum: ", int(str1) + int(str2))
            print("Difference: ", int(str1) - int(str2))
            print("Product: ", int(str1) * int(str2))
            if int(str2) == 0:
                print("ERROR: Division by 0")
                print("ERROR: Modulo by 0")
            else:
                print("Quotient: ", int(str1) / int(str2))
                print("Remainder: ", int(str1) % int(str2))
        

if __name__ == "__main__":
    main()
