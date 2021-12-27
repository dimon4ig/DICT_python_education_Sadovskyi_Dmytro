str_m1 = str_m2 = stl_m1 = stl_m2 = s = 0
e = []
b = c = d = []
answer = 100


def mat():
    global str_m1, str_m2, stl_m1, stl_m2, b, c
    str_m1, stl_m1 = input("Введите количество строк и столбцов 1-ой матрицы:").split(" ")
    b = [[int(k) for k in input().split(" ")] for t in range(int(str_m1))]
    str_m2, stl_m2 = input("Введите количество строк и столбцов 2-ой матрицы:").split(" ")
    c = [[int(k) for k in input().split(" ")] for t in range(int(str_m2))]


def summa():
    global d, e
    mat()
    if str_m1 == str_m2:
        if stl_m1 == stl_m2:
            for i in range(int(str_m1)):
                for j in range(int(stl_m1)):
                    e.append(b[i][j] + c[i][j])
                d.append(e)
                e = []
            res()
        else:
            print("Операция не может быть выполнена.")
    else:
        print("Операция не может быть выполнена.")


def res():
    global d
    print("Результат:")
    for i in range(int(str_m1)):
        print(" ".join(map(str, d[i])))
    d = []


def constant():
    global str_m1, stl_m1, b, e, d
    str_m1, stl_m1 = input("Введите количество строк и столбцов матрицы: ").split(" ")
    b = [[int(k) for k in input().split(" ")] for t in range(int(str_m1))]
    cons = int(input("Введите константу: "))
    for i in range(int(str_m1)):
        for j in range(int(stl_m1)):
            e.append(b[i][j] * cons)
        d.append(e)
        e = []
    res()


def mat_x():
    global str_m1, str_m2, stl_m1, stl_m2, b, c, s, e, d
    mat()
    if int(str_m1) == int(stl_m2):
        for k in range(int(str_m1)):
            for i in range(int(stl_m2)):
                for j in range(int(str_m2)):
                    s += b[k][j] * c[j][i]
                e.append(s)
                s = 0
            d.append(e)
            e = []
        res()
    else:
        print("Операция не может быть выполнена.")


while answer != 0:
    answer = int(input("1. Сложить матрицы\n"
                       "2.Умножить матрицу на константу\n"
                       "3. Умножить матрицы\n"
                       "0. Выход\n"
                       "Ваш выбор:"))
    if answer == 0:
        print("До скорых встреч!!!")
        break
    elif answer == 1:
        summa()
    elif answer == 2:
        constant()
    elif answer == 3:
        mat_x()
