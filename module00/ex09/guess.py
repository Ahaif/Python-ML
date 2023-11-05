import sys
import random


answer = random.randint(1, 99) 




def main():
    count = 0
    while True:
        print("this is a guess game , Enter: a number between 1 and 99")
        input = sys.stdin.readline()
        if input == "exit\n":
            print("Goodbye")
            break
        if not input.isdigit():
            print("you should enter a INT")
        count += 1
        if input == answer:
            print("you guessed it in " + count + "tries")
            break 
        else:
            print("wrong answer")





    





if __name__ == '__main__':
    main()