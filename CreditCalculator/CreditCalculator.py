import math
loan_p = int(input("Введите сумму кредита:"))
choice = input("Что вы хотите посчитать?\n"
               "тип «m» - для количества ежемесячных платежей\n"
               "тип «p» - для суммы ежемесячного платежа:\n"
               "Мой выбор:")
if choice == "m":
    m_p = int(input("Введите сумму ежемесячного платежа:"))
    print("Это займет", str(math.ceil(loan_p / m_p)), "месяцев на погашение кредита")
elif choice == "p":
    number_m = int(input("Введите количество месяцев:"))
    p_m = math.ceil(loan_p / number_m)
    last_p = loan_p - (number_m - 1) * p_m
    if last_p == p_m:
        print("Ваш ежемесячный платеж = " + str(p_m))
    else:
        print("Ваш ежемесячный платеж = " + str(p_m) + " и последний платеж " + str(last_p))
