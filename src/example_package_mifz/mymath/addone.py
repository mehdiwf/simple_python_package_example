from .sub_one import sub
from ..printmod import say_hello


def add_one(x):
    return x + 1


def add_one_and_say_hello(x):
    say_hello()
    return add_one(x)


def add_one_v2(x):
    return sub(x) + 2
