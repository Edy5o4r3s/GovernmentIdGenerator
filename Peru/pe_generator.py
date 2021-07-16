import random


def pe_generator():
    n = [2, 0] + [random.randrange(10) for i in range(8)]
    v = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    s = sum(x * y for x, y in zip(n, v))
    b = s // 11
    d = 11 - (s - b * 11)
    n.append(d)

    return print("%d%d%d%d%d%d%d%d%d%d%d" % tuple(n))

