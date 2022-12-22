from random import randint


def create_polynomial(number):
    pol: str = f'{randint(1, 100)}x^{number}'
    for i in range(number - 1, 0, -1):
        flag = randint(0, 1)
        flag2 = randint(0, 1)
        if flag:
            if i == 1:
                if flag2:
                    pol = pol + ' + ' + f'{randint(1, 100)}x'
                else:
                    pol = pol + ' - ' + f'{randint(1, 100)}x'
            elif flag2:
                pol = pol + ' + ' + f'{randint(1, 100)}x^{i}'
            else:
                pol = pol + ' - ' + f'{randint(1, 100)}x^{i}'
    pol += ' = 0'
    return pol


if __name__ == "__main__":
    print(create_polynomial(int(input('input polynomial degree: '))))
    
