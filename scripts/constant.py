from main import factorial
import decimal

def pi(precision):
    decimal.getcontext().prec = precision + 1
    pi = decimal.Decimal(0)
    for k in range(precision):
        pi += (decimal.Decimal(1) / (16 ** k)) * ((decimal.Decimal(4) / (8 * k + 1)) - (decimal.Decimal(2) / (8 * k + 4)) - (decimal.Decimal(1) / (8 * k + 5)) - (decimal.Decimal(1) / (8 * k + 6)))
    return pi

def tau(*imp):
    if not imp:
        imp = 4
    else:
        imp = imp[0]
    return round(pi(imp), imp)

def e(*imp):
    if not imp:
        imp = 50
    else:
        imp = imp[0]
    return_e = 0
    for n in range(imp):
        return_e = return_e + 1 / main.factorial(n)
    return round(return_e, imp)
