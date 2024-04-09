from .fix_string import fix_string_for_parse_input
from calculator.math_functions.math_funcs import Gcd, Lcm


class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.elements = fix_string_for_parse_input(expression).split()
        self.operator_stack = []
        self.postfix_notation = []
        self.operator_priority = {'+': 1, '-': 1,
                                  '*': 2, '/': 2,
                                  '^': 3, 'mod': 3, '%': 3, '!': 3,
                                  'sqrt': 4, 'sin': 4, 'cos': 4, 'tan': 4, 'tg': 4, 'log': 4, 'lg': 4, 'ln': 4,
                                  'gcd': 5, 'lcm': 5}

        self.special_functions = {'gcd': Gcd, 'нод': Gcd, 'lcm': Lcm, 'нок': Lcm}
        self.nums = []
        self.spec_func = None

    def parse_input(self):
        for element in self.elements:

            if element in self.special_functions or self.spec_func is not None:
                if self.spec_func is None:
                    self.spec_func = element
                if element == ',':
                    continue
                self.nums.append(element)
                if element == ")":
                    self.nums = map(int, self.nums[2:-1])
                    spec_func = self.special_functions[self.spec_func]
                    self.postfix_notation.append(spec_func(*self.nums))
                    self.spec_func = None
                    self.nums = []

            elif element.isdigit():
                self.postfix_notation.append(int(element))

            elif element in self.operator_priority:
                while self.operator_stack and self.operator_stack[-1] != '(' and self.operator_priority.get(
                        self.operator_stack[-1], 0) >= self.operator_priority[element]:
                    self.postfix_notation.append(self.operator_stack.pop())
                self.operator_stack.append(element)

            elif element == '(':
                self.operator_stack.append(element)
            elif element == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.postfix_notation.append(self.operator_stack.pop())
                if self.operator_stack and self.operator_stack[-1] == '(':
                    self.operator_stack.pop()
                else:
                    raise ValueError("Неправильное расположение скобок")
            else:
                raise ValueError("Некорректный символ")

        while self.operator_stack:
            if self.operator_stack[-1] == '(':
                raise ValueError("Неправильное расположение скобок в выражении")
            self.postfix_notation.append(self.operator_stack.pop())
        return self.postfix_notation
