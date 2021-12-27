from random import choice
count = int(input("Введите количество присоединяющихся друзей (включая вас):"))
n = {}  # создал пустой словарь: {ключ : значение}
sh = []  # список в котором счастливчик
if count >= 0:
    print("Введите имя каждого друга (включая вас), каждое с новой строки:")
    for i in range(count):  # список от 0 до count
        name = input()
        n[name] = 0  # вставка значений под каждый ключ словаря
        sh.append(name)
else:
    print("Никто не присоединяется к вечеринке")
summa = int(input("Введите полную сумму:"))
certain = round(summa / count, 2)  # округление, после запятой два знака
for name in n:
    n[name] = certain  # вставка значений под каждый ключ словаря
sh_name = choice(sh)
question = input("Хотите использовать особеннность \"Кому повезло?\"? Напишите Yes/No:")
if question == "Yes":
    print(sh_name, "счастливчик!")
else:
    print("Значит никому не повезет)")
