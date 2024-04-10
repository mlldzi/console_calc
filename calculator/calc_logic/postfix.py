import math
from calculator.math_functions.math_funcs import *


def evaluate_postfix(expression):
    stack = []
    operations = {
        '+': Add,
        '-': Subtract,
        '*': Multiply,
        '/': Divide,
        '^': Power,
        'sqrt': Sqrt,
        'log': Log,
        'lg': Log,
        'ln': Ln,
        'sin': Sin,
        'cos': Cos,
        'tan': Tan,
        'tg': Tg,
        'mod': Mod,
        '%': Mod,
        '!': Factorial,
        'gcd': Gcd,
        'ldm': Lcm
    }

    for element in map(str, expression):
        if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
            stack.append(int(element))
        else:
            if element in operations:
                if element in functions:
                    operand = stack.pop()
                    result = operations[element](operand).result
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operations[element](operand1, operand2).result
                stack.append(result)
    if len(stack) != 1:
        raise ValueError('Неверное выражение')
    return stack[0]
