import sys



kata00 = (19, 42, 21)

def main():
    if len(sys.argv) > 1:
        print("ERROR: MORE THAN ONE ARGS")
        return
    else:
        print("The 3 numbers are: ", kata00[0], ", ", kata00[1], ", ", kata00[2], sep='')





if __name__ == "__main__":
    main()