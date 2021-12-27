str_m1 = str_m2 = stl_m1 = stl_m2 = 0
e = []
b = c = d = []


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
            print("ERROR")
    else:
        print("ERROR")


def res():
    for i in range(int(str_m1)):
        print(" ".join(map(str, d[i])))


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


constant()
