from random import choice
from string import ascii_uppercase as upp, digits as nums

__names = set()
__limit = len(upp)**2 * len(nums)**3


def gen_name():
    if len(__names) >= __limit:
        raise Exception('the robot names database is full')
    while True:
        n = '{}{}{:03d}'.format(choice(upp), choice(upp), int(choice(nums)))
        if n not in __names:
            __names.add(n)
            return n


class Robot(object):
    def __init__(self):
        self.__name = gen_name()

    def reset(self):
        self.__name = None

    @property
    def name(self):
        if self.__name is None:
            self.__name = gen_name()
        return self.__name
