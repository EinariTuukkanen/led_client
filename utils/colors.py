from random import randint


def random_rgb():
    return [randint(0, 255) for _ in range(3)]


def random_rgbs(n):
    return [random_rgb() for _ in range(n)]
