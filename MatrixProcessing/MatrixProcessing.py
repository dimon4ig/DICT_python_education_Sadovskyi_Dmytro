from math import ceil

str_m1 = str_m2 = stl_m1 = stl_m2 = s = con = 0
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


def constant(bk):
    global e, d, con
    for i in range(str_m1):
        for j in range(stl_m1):
            e.append(round(bk[i][j] * con, 2))
        d.append(e)
        e = []
    return d


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


def matrix():
    global str_m1, stl_m1, b
    str_m1, stl_m1 = input("Введите количество строк и столбцов матрицы:").split(" ")
    print("Введите матрицу:")
    b = [[int(k) for k in input().split(" ")] for _ in range(int(str_m1))]


def res_s():
    global b
    print("Результат:")
    for i in range(int(str_m1)):
        print(" ".join(map(str, (b[i]))))
    b = []


def t_mat():
    global str_m1, stl_m1, b
    str_m1, stl_m1 = input("Введите количество строк и столбцов матрицы: ").split(" ")
    str_m1 = int(str_m1)
    stl_m1 = int(stl_m1)
    print("Введите матрицу:")
    b = [[int(k) for k in input().split(" ")] for _ in range(str_m1)]


def t_mat_side():
    global str_m1, stl_m1, b
    matrix()
    l = int(str_m1) - 1
    for i in range(l + 1):
        for j in range(l + 1):
            if i > l - j:
                b[i][j], b[l - j][l - i] = b[l - j][l - i], b[i][j]
    res_s()


def t_mat_main():
    global str_m1, stl_m1, b
    matrix()
    l = int(str_m1)
    for i in range(l):
        for j in range(l):
            if i > j:
                b[i][j], b[j][i] = b[j][i], b[i][j]
    res_s()


def t_mat_ver():
    global str_m1, stl_m1, b
    matrix()
    l = int(str_m1) - 1
    f = ceil(l / 2)
    for i in range(l + 1):
        for j in range(f):
            b[i][j], b[i][l - j] = b[i][l - j], b[i][j]
    res_s()


def t_mat_hor():
    global str_m1, stl_m1, b
    matrix()
    lo = int(str_m1) - 1
    f = ceil(lo / 2)
    for i in range(f):
        for j in range(lo + 1):
            b[i][j], b[lo - i][j] = b[lo - i][j], b[i][j]
    res_s()


def t_mat_info():
    print("1.Главная диагональ\n"
          "2. Боковая диагональ\n"
          "3. Вертикальная линия\n"
          "4. Горизонтальная линия")
    choice = int(input("Ваш выбор: "))
    if choice == 1:
        t_mat_main()
    elif choice == 2:
        t_mat_side()
    elif choice == 3:
        t_mat_ver()
    elif choice == 4:
        t_mat_hor()
    else:
        print("Операция не может быть выполнена.")


def minor(h, i, u):
    return [k[:u] + k[u + 1:] for k in (h[:i] + h[i + 1:])]


def determ(l):
    if len(l) == 2:
        return l[0][0] * l[1][1] - l[0][1] * l[1][0]
    det = 0
    for i in range(len(l)):
        det += ((-1) ** i) * l[0][i] * determ(minor(l, 0, i))
    return det


def inwerse_mat_main(bk):
    global str_m1, stl_m1
    for i in range(str_m1):
        for j in range(str_m1):
            if i > j:
                bk[i][j], bk[j][i] = bk[j][i], bk[i][j]
    return bk


def inwerse_m(k):
    global con, d
    for i in range(str_m1):
        for j in range(stl_m1):
            if i + j % 2 == 0:
                b_1[i][j] = determ(minor(k, i, j))
            else:
                b_1[i][j] = -(determ(minor(k, i, j)))
    try:
        con = 1 / determ(k)
        cad = constant(inwerse_mat_main(b_1))
        for z in range(str_m1):
            print(' '.join(map(str, cad[z])))
    except ZeroDivisionError:
        print("Эта матрица не имеет инверсии.")


while answer != 0:
    answer = int(input("1. Сложить матрицы\n"
                       "2. Умножить матрицу на константу\n"
                       "3. Умножить матрицы\n"
                       "4. Матрица транспонирования\n"
                       "5. Вычислить определитель\n"
                       "6. Обратная матрица\n"
                       "0. Выход\n"
                       "Ваш выбор:"))
    if answer == 0:
        print("До скорых встреч!!!")
        break
    elif answer == 1:
        summa()
    elif answer == 2:
        str_m1, stl_m1 = input("Введите количество строк и столбцов матрицы: ").split(" ")
        b = [[float(k) for k in input().split(" ")] for _ in range(int(str_m1))]
        con = float(input("Введите константу: "))
        for i in range(int(str_m1)):
            for j in range(int(stl_m1)):
                e.append(b[i][j] * con)
            d.append(e)
            e = []
        res()
    elif answer == 3:
        mat_x()
    elif answer == 4:
        t_mat_info()
    elif answer == 5:
        t_mat()
        print("Результат: " + str(determ(b)))
    elif answer == 6:
        t_mat()
        b_1 = [["_" for k in range(str_m1)] for v in range(stl_m1)]
        print("Результат:")
        inwerse_m(b)
        print()
