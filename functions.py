from decimal import Decimal, getcontext


number_Of_Process = 1


def pi(index):
    getcontext().prec = 10000
    result = Decimal(0)
    for k in range(0, 1000):
        if k % number_Of_Process == index:
            result += Decimal(-3)**(-k)/(2*k + 1)
            results = Decimal(result * Decimal.sqrt(Decimal(12)))
    return results


def bbp2(index):
    getcontext().prec = 10000
    result = Decimal(0)
    results = Decimal(0)
    for i in range(0, 10):
        if i % number_Of_Process == index:
            a = ((Decimal(-1) ** i) / (2 ** (10*i)))
            b = Decimal((2 ** 5) / (4 * i + 1))
            c = Decimal(Decimal(1) / (4 * i + 3))
            d = Decimal((2 ** 8) / (10 * i + 1))
            e = Decimal((2 ** 6) / (10 * i + 3))
            f = Decimal((2 ** 2) / (10 * i + 5))
            j = Decimal((2 ** 2) / (10 * i + 7))
            h = Decimal(Decimal(1) / (10 * i + 9))
            result += Decimal(a * (- b - c + d - e - f - j + h))
            results = result * Decimal(1 / 2 ** 6)
    return Decimal(results)
