import math
from calculator.some_functions.parent_classes import OneArg


class Sin(OneArg):
    """
    Синус
    """

    def calculate(self):
        return math.sin(self.a)


class Cos(OneArg):
    """
    Косинус
    """

    def calculate(self):
        return math.cos(self.a)


class Tan(OneArg):
    """
    Тангенс
    """

    def calculate(self):
        return math.tan(self.a)


class Tg(Tan):
    pass
