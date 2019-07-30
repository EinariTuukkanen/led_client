from random import randint


def random_rgb():
    return [randint(0, 255) for _ in range(3)]


def random_rgbs(n):
    return [random_rgb() for _ in range(n)]


def rgb_to_hex(r, g, b):
    return "#{0:02x}{1:02x}{2:02x}".format(_clamp(r), _clamp(g), _clamp(b))


def _clamp(x):
    return max(0, min(x, 255))
