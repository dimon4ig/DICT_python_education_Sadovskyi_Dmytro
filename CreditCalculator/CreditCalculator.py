# python CreditCalculator\CreditCalculator.py --type=diff --principal=1000000 --periods=10 --interest=10
# python CreditCalculator\CreditCalculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
# python CreditCalculator\CreditCalculator.py --type=diff --principal=500000 --periods=8 --interest=7.8
# python CreditCalculator\CreditCalculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# python CreditCalculator\CreditCalculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
from math import ceil, log, floor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()
typ = args.type
principal = args.principal
period = args.periods
interest = args.interest / 1200
payment = args.payment


def diff__payment():
    i = 0
    sum_d_p = 0
    global typ, principal, period, interest, payment
    for k in range(1, period + 1):
        i += 1
        diff_payment = ceil(float(principal / period) + interest * (principal - principal * (k - 1) / period))
        print("Месяц " + str(i) + ": оплата " + str(int(diff_payment)))
        sum_d_p += diff_payment
    overpayment = sum_d_p - principal
    print("Переплата = " + str(overpayment))


def period_():
    global typ, principal, period, interest, payment
    period = ceil(log(payment / (payment - (interest * principal)), (1 + interest)))
    if period // 12 == 0:
        print("Это займет", str(period), "месяцев на погашение кредита!")
    elif period % 12 == 0:
        print("Это займет", str(period // 12), "лет на погашение кредита!")
    elif period % 12 != 0:
        print("Это займет", str(period // 12), "лет и", str(period % 12), "месяцев на погашение кредита!")
    overpayment = payment * period - principal
    print("Переплата = " + str(overpayment))


def payment_():
    global typ, principal, period, interest, payment
    i_period = (1 + interest) ** period
    payment = ceil(principal * (interest * i_period / (i_period - 1)))
    print("Ваш ежемесячный платеж = " + str(payment) + "!")
    overpayment = payment * period - principal
    print("Переплата = " + str(overpayment))


def principal_():
    global payment, interest, period, principal, typ
    i_period = (1 + interest) ** period
    principal = floor(payment / (interest * i_period / (i_period - 1)))
    print("Основная сумма кредита = " + str(principal) + "!")
    overpayment = payment * period - principal
    print("Переплата = " + str(overpayment))


try:
    if typ == "annuity":
        if period is None:
            if principal > 0 and payment > 0 and interest > 0:
                period_()
            else:
                print("Incorrect parameters")
        elif payment is None:
            if principal > 0 and period > 0 and interest > 0:
                payment_()
            else:
                print("Incorrect parameters")
        elif principal is None:
            if payment > 0 and period > 0 and interest > 0:
                principal_()
            else:
                print("Incorrect parameters")
    elif typ == "diff":
        if principal > 0 and period > 0 and interest > 0:
            diff__payment()
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
except TypeError:
    print("Incorrect parameters")
