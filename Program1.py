import math


def acc_pi(acc):
    pi = math.pi
    our_pi = 0
    coef = 0
    n = 1
    while abs((our_pi - pi)) > acc:
        coef += 1 / ((2 * n) + 1) * ((-1 / 3) ** n)
        our_pi = 2 * (3 ** 0.5) * (1 + coef)
        n += 1

    print(our_pi)


acc_pi(0.00000001)
