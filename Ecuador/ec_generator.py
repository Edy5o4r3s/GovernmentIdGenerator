import random


def ec_generator():
    last_digit = random.randrange(4)
    if last_digit == 0:
        last_digit = 1
    first_digits = [random.randrange(10) for i in range(3)]
    verification1 = str(first_digits[0:2])
    verification1 = verification1[1] + verification1[4]
    verify = True
    while verify:
        if int(verification1) > 24 or first_digits[2:3] == 7 or first_digits[2:3] == 8:
            first_digits = [random.randrange(10) for i in range(3)]
            verification1 = str(first_digits[0:2])
            verification1 = verification1[1] + verification1[4]
        else:
            verify = False

    n = first_digits + [random.randrange(10) for i in range(7)] + [0, 0] + [last_digit]
    return print("%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n))

