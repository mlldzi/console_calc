import math
from calculator.math_functions.math_funcs import functions


def evaluate_postfix(expression):
    stack = []
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x ** y,
        'sqrt': lambda x: x ** 0.5,
        'log': lambda x: math.log(x, 2),
        'lg': lambda x: math.log(x, 10),
        'ln': lambda x: math.log(x, math.e),
        'sin': lambda x: math.sin(x),
        'cos': lambda x: math.cos(x),
        'tan': lambda x: math.tan(x),
        'tg': lambda x: math.tan(x),
        'mod': lambda x, y: x % y,
        '%': lambda x, y: x % y,
        '!': lambda x: math.factorial(x)
    }

    for element in map(str, expression):
        if element.isdigit():
            stack.append(int(element))
        else:
            if element in operations:
                if element in functions:
                    operand = stack.pop()
                    result = operations[element](operand)
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operations[element](operand1, operand2)
                stack.append(result)
    return stack[0]
