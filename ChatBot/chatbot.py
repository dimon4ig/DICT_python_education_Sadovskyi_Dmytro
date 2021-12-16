def name():
    print("Hello! My name is Creeper.")
    print("I was created in 2009.")
    print("Please, remind me your name.")
    your_neme = input()
    print(f"What a great name you have, {your_neme}!")


def age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age_f = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f'Your age is {age_f}; thats a good time to start programming!')


def game():
    print("Now I will prove to you that I can count to any number you want.")
    for h in range(int(input())+1):
        print(str(h) + '!')


def test():
    print("Completed, have a nice day!")
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    b = ()
    while b != 2:
        b = int(input())
        if b == 2:
            print("Congratulations, have a nice day!")
        else:
            print("Please, try again.")


name()
age()
game()
test()
