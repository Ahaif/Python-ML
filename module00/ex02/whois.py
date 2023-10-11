import sys



def main():
    if len(sys.argv) != 2:
        print("ERROR: MORE THAN ONE ARGS")
        return
    number = sys.argv[1]
    if not number.isdigit():
        print("ERROR - Input is not a number")
        return
    else:
        number = int(number)
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")


if __name__ == "__main__":
    main()

