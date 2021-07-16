import random


def co_generator():
    n = [random.randrange(10) for i in range(9)]
    v = [41, 37, 29, 23, 19, 17, 13, 7, 3]
    s = sum(x * y for x, y in zip(n, v))
    d = s % 11
    if d >= 2:
        d = 11 - d
    n.append(d)

    return print("%d%d%d.%d%d%d.%d%d%d-%d" % tuple(n))


