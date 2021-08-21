# -*- coding: utf-8 -*-
"""Find the nth fibonacci number
"""


def fib(x, y, nth, count):
    count += 1
    tmp = x + y
    if count != nth:
        return fib(y, tmp, nth, count)
    else:
        return tmp


if __name__ == '__main__':
    assert fib(1, 1, 7, 2) == 13
    assert fin(1, 1, 9, 2) == 34
