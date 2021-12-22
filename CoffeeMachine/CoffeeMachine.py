count_water = 400
count_milk = 540
count_coffee_beans = 120
count_cups = 9
count_money = 550


def remaining():
    print("В кофе машине есть:\n",
          str(count_water), "воды\n",
          str(count_milk), "молока\n",
          str(count_coffee_beans), "зерен кофе\n",
          str(count_cups), "одноразовых стаканчиков\n",
          str(count_money), "денег\n")


def start():
    choice_user = input(
        "Напишите действие (buy - купить, fill - заполнить, take - взять, remaining - остаток, exit - выход):")
    if choice_user == "buy":
        buy()
    elif choice_user == "fill":
        fill()
    elif choice_user == "take":
        take()
    elif choice_user == "remaining":
        remaining()
    elif choice_user == "exit":
        return "exit"


def enough():
    global count_water, count_milk, count_coffee_beans, count_money
    if count_water <= 0:
        print("Извините, недостаточно воды")
    elif count_milk <= 0:
        print("Извините, недостаточно молока")
    elif count_coffee_beans <= 0:
        print("Извините, недостаточно кофейных зерен")
    elif count_cups <= 0:
        print("К сожалению, одноразовых стаканчиков недостаточно")


def buy():
    print("Что ты хочешь купить: 1 - эспрессо, 2 - латте, 3 - капучино, back - вернуться в главное меню")
    global count_water, count_milk, count_coffee_beans, count_cups, count_money
    choice_user = input()
    if choice_user == str(1):
        count_water -= 250
        count_coffee_beans -= 16
        count_cups -= 1
        count_money += 4
        if enough() == None:
            print("У меня достаточно ресурсов, чтобы приготовить тебе кофе!")
        else:
            print(enough())
    elif choice_user == str(2):
        count_water -= 350
        count_milk -= 75
        count_coffee_beans -= 20
        count_cups -= 1
        count_money += 7
        if enough() == None:
            print("У меня достаточно ресурсов, чтобы приготовить тебе кофе!")
        else:
            print(enough())
    elif choice_user == str(3):
        count_water -= 200
        count_milk -= 100
        count_coffee_beans -= 12
        count_cups -= 1
        count_money += 6
        if enough() == None:
            print("У меня достаточно ресурсов, чтобы приготовить тебе кофе!")
        else:
            print(enough())
    elif choice_user == "back":
        return "back"


def fill():
    global count_water, count_milk, count_coffee_beans, count_cups, count_money
    result_water = int(input("Напишите, сколько мл воды вы хотите добавить:"))
    count_water += result_water
    result_milk = int(input("Напишите, сколько мл молока вы хотите добавить:"))
    count_milk += result_milk
    result_coffee_beans = int(input("Напишите, сколько граммов кофейных зерен вы хотите добавить:"))
    count_coffee_beans += result_coffee_beans
    result_cups = int(input("Напишите, сколько одноразовых кофейных стаканчиков вы хотите добавить:"))
    count_cups += result_cups


def take():
    global count_money
    print("Вам выдали: " + str(count_money))
    count_money = 0


facts_start = 0
while facts_start != "exit":
    facts_start = start()
