import random

print("ВИСЕЛИЦА")
list_version = ["python", "java", "javascript", "php"]
random_1 = random.choice(list_version)  # выбор одного из слова
random_2 = list(random_1)   # список этого слова
random_3 = list(len(random_1) * "-")    # список из прочерков слова
nothing = []   # будующее повторение букв
letters = list("qwertyuiopasdfghjklzxcvbnm")    # английские буквы
print("Угадай слово)", "\n", len(random_1) * "-")
pp = 0
while pp != 8:
    pp += 1
    result_1 = str(input("Введите одну из букв:"))  # ввод буквы в виде строки
    if result_1 in nothing:     # условие
        print("Такая буква уже есть!")
        continue
    pp -= 1
    nothing.append(result_1)
    if result_1 in random_2:
        if random_2.count(result_1) >= 2:   # если количество одинаковых букв 2 и больше в random_2, то:
            ind = random_2.index(result_1)  # вычисляем индекс введенной буквы
            random_3[ind] = result_1    # прочерк под индексом имеет result_1
            random_2[ind] = "-"     # буква под индексом имеет -
        ind = random_2.index(result_1)      # вычисляем индекс введенной буквы
        random_3[ind] = result_1    # прочерк под индексом имеет result_1
        pp -= 1     # возврат попытки
    elif len(result_1) >= 2:    # исключение
        print("Вы должны ввести одну букву!")
        pp -= 1
    elif result_1 not in letters:   # исключение
        print("Вводите буквы на английском языке!")
        pp -= 1
    elif result_1 not in random_2:
        print("В слове такой буквы нет, попробуйте снова!")
    print(''.join(random_3))  # объединение строк и добавления между ними символа
fin_str = ''.join(random_3)
if fin_str == random_1:
    print("Вы угадали слово!\nВы выжили!")
else:
    print("Вы проиграли!")
