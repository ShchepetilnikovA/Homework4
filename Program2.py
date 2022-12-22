def simple_factor(number):
    i = 2
    lst = []
    while i ** 2 < number:
        while number % i == 0:
            lst.append(i)
            number //= i
        i += 1
    if number > 0:
        lst.append(number)
    print(lst)


simple_factor(512)
