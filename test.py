import random

a = [1, 2, 3, 4, 5, 6, 7, 8]


def randmos(v):
    x = random.choice(v)
    v.remove(x)


randmos(a)

print(a)
