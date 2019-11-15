import random


def phone_number_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 999)).zfill(3)
    last = str(random.randint(1, 9999)).zfill(4)

    while last[0] == last[1] == last[2] == last[3]:
        print(last)
        last = (str(random.randint(1, 9999)).zfill(4))
        print("was the same numbers")

    return '{}-{}-{}'.format(first, second, last)
