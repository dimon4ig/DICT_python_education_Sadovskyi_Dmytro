a = list(input("Введите ячейки:"))
region = str('---------')
s_1 = ['|', a[0], a[1], a[2], '|']
s_2 = ['|', a[3], a[4], a[5], '|']
s_3 = ['|', a[6], a[7], a[8], '|']
dig = [int(i) for i in range(1, 4)]  # i хранящая в себе числа 1, 2 и 3
s_l = [' ', s_1, s_2, s_3, ' ']
answer_1 = 0
answer_2 = 0


def wins():
    res = []
    if a.count("X") - a.count("O") >= 2:
        return "Невозможно"
    elif a.count("O") - a.count("X") >= 2:
        return "Невозможно"
    if s_1[1] == s_1[2] == s_1[3] != "_":
        res.append(s_1[1])
    if s_2[1] == s_2[2] == s_2[3] != "_":
        res.append(s_2[1])
    if s_3[1] == s_3[2] == s_3[3] != "_":
        res.append(s_3[6])
    if s_1[1] == s_2[1] == s_3[1] != "_":
        res.append(s_1[1])
    if s_1[2] == s_2[2] == s_3[2] != "_":
        res.append(s_1[2])
    if s_1[3] == s_2[3] == s_3[3] != "_":
        res.append(s_1[3])
    if s_1[1] == s_2[2] == s_3[3] != "_":
        res.append(s_1[1])
    if s_1[3] == s_2[2] == s_3[1] != "_":
        res.append(s_1[3])
    if res.count("X") >= 2:
        res.remove("X")
    elif res.count("O") >= 2:
        res.remove("O")
    if len(res) >= 2:
        return "Невозможно"
    elif len(res) == 1:
        return res[0] + " победил"
    elif "_" not in a:
        if len(res) == 0:
            return "Ничья"
    elif "_" in a:
        if len(res) == 0:
            return "Игра не закончена"


def square():
    print("-------------\n" +
          '  '.join(s_1), "\n" +
          '  '.join(s_2), "\n" +
          '  '.join(s_3), "\n" +
          "-------------")
    print(wins())


def step():
    cycle = 0
    global s_1, s_2, s_3, answer_1, answer_2
    while cycle != 1:
        print("Введите координаты:")
        try:    # ключевое слово для обработки исключений
            answer_1, answer_2 = input().split(' ')  # split разбивает строки на подстроки в зависимости от разделителя
            answer_1 = int(answer_1)
            answer_2 = int(answer_2)
        except ValueError:  # исключение ошибки
            print("Вы должны ввести числа!")
            continue
        if answer_1 and answer_2 not in dig:
            print("Координаты должны быть от 1 до 3!")
        elif answer_1 and answer_2 in dig:
            if s_l[answer_1][answer_2] != '_':  # для определения занятости клетки под её координатой
                print("Эта клетка занята! Выбери другую!")
            else:
                s_l[int(answer_1)][int(answer_2)] = "X"
                cycle = 1
    square()


square()
step()
