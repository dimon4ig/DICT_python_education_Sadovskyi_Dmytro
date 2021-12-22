class CoffeeMachine:
    def __init__(self):  # смециальный метод определяет в классах конструктор
        self.count_water = 400  # чтобы функция могла обращатся сам к себе и делать самовызов
        self.count_milk = 540
        self.count_coffee_beans = 120
        self.count_cups = 9
        self.count_money = 550

    def remaining(self):
        print("В кофе машине есть:\n",
              str(self.count_water), "воды\n",
              str(self.count_milk), "молока\n",
              str(self.count_coffee_beans), "зерен кофе\n",
              str(self.count_cups), "одноразовых стаканчиков\n",
              str(self.count_money), "денег\n")

    def start(self):
        choice_user = input(
            "Напишите действие (buy - купить, fill - заполнить, take - взять, remaining - остаток, exit - выход):")
        if choice_user == "buy":
            objects.buy()
        elif choice_user == "fill":
            objects.fill()
        elif choice_user == "take":
            objects.take()
        elif choice_user == "remaining":
            objects.remaining()
        elif choice_user == "exit":
            return "exit"

    def enough(self):
        if self.count_water <= 0:
            print("Извините, недостаточно воды")
        elif self.count_milk <= 0:
            print("Извините, недостаточно молока")
        elif self.count_coffee_beans <= 0:
            print("Извините, недостаточно кофейных зерен")
        elif self.count_cups <= 0:
            print("К сожалению, одноразовых стаканчиков недостаточно")

    def buy(self):
        print("Что ты хочешь купить: 1 - эспрессо, 2 - латте, 3 - капучино, back - вернуться в главное меню")
        choice_user = input()
        if choice_user == str(1):
            self.count_water -= 250
            self.count_coffee_beans -= 16
            self.count_cups -= 1
            self.count_money += 4
            if objects.enough() is None:
                print("У меня достаточно ресурсов, чтобы приготовить тебе кофе!")
            else:
                print(objects.enough())
        elif choice_user == str(2):
            self.count_water -= 350
            self.count_milk -= 75
            self.count_coffee_beans -= 20
            self.count_cups -= 1
            self.count_money += 7
            if objects.enough() is None:
                print("У меня достаточно ресурсов, чтобы приготовить тебе кофе!")
            else:
                print(objects.enough())
        elif choice_user == str(3):
            self.count_water -= 200
            self.count_milk -= 100
            self.count_coffee_beans -= 12
            self.count_cups -= 1
            self.count_money += 6
            if objects.enough() is None:
                print("У меня достаточно ресурсов, чтобы приготовить тебе кофе!")
            else:
                print(objects.enough())
        elif choice_user == "back":
            return "back"

    def fill(self):
        result_water = int(input("Напишите, сколько мл воды вы хотите добавить:"))
        self.count_water += result_water
        result_milk = int(input("Напишите, сколько мл молока вы хотите добавить:"))
        self.count_milk += result_milk
        result_coffee_beans = int(input("Напишите, сколько граммов кофейных зерен вы хотите добавить:"))
        self.count_coffee_beans += result_coffee_beans
        result_cups = int(input("Напишите, сколько одноразовых кофейных стаканчиков вы хотите добавить:"))
        self.count_cups += result_cups

    def take(self):
        print("Вам выдали: " + str(self.count_money))
        self.count_money = 0


objects = CoffeeMachine()

facts_start = 0
while facts_start != "exit":
    facts_start = objects.start()
