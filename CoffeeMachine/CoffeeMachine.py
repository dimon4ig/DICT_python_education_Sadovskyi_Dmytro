count_water = 400
count_milk = 540
count_coffee_beans = 120
count_cups = 9
count_money = 550


def info():
    print("В кофе машине есть:\n",
          str(count_water), "воды\n",
          str(count_milk), "молока\n",
          str(count_coffee_beans), "зерен кофе\n",
          str(count_cups), "одноразовых стаканчиков\n",
          str(count_money), "денег\n")


info()


def start():
    choice_user = input("Напишите действие (buy - купить, fill - заполнить, take - взять):")
    if choice_user == "buy":
        buy()
        info()
    elif choice_user == "fill":
        fill()
        info()
    elif choice_user == "take":
        take()
        info()


def buy():
    print("Что ты хочешь купить? 1 - эспрессо, 2 - латте, 3 - капучино:")
    global count_water
    global count_milk
    global count_coffee_beans
    global count_cups
    global count_money
    choice_user = int(input())
    if choice_user == 1:
        count_water -= 250
        count_coffee_beans -= 16
        count_cups -= 1
        count_money += 4
    elif choice_user == 2:
        count_water -= 350
        count_milk -= 75
        count_coffee_beans -= 20
        count_cups -= 1
        count_money += 7
    elif choice_user == 3:
        count_water -= 200
        count_milk -= 100
        count_coffee_beans -= 12
        count_cups -= 1
        count_money += 6


def fill():
    global count_water
    global count_milk
    global count_coffee_beans
    global count_cups
    global count_money
    result_water = int(input("Напишите, сколько мл воды вы хотите добавить:"))
    count_water += result_water
    result_milk = int(input("Напишите, сколько мл молока вы хотите добавить"))
    count_milk += result_milk
    result_coffee_beans = int(input("Напишите, сколько граммов кофейных зерен вы хотите добавить:"))
    count_coffee_beans += result_coffee_beans
    result_cups = int(input("Напишите, сколько одноразовых кофейных стаканчиков вы хотите добавить:"))
    count_cups += result_cups


def take():
    global count_money
    print("Вам выдали: " + str(count_money))
    count_money = 0


start()
