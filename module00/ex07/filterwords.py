import sys
import string




def main():
    if len(sys.argv) != 3 or sys.argv[1].isdigit() or sys.argv[2].isalpha():
        print("ERROR")
        return
    print("success")

    data = sys.argv[1].split()
    cleanedData = []
    for str in data:
        test_str = str.translate(str.maketrans('', '', string.punctuation))
        if len(test_str) > int(sys.argv[2]):
            cleanedData.append(test_str)

    print(cleanedData)
   


if __name__ == '__main__':
    main()


