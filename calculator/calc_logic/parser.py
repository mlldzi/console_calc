from .fix_string import fix_string_for_parse_input


def parse_input(expression):
    """
    Ожидается, что выражение состоит только из цифр и операторов,
    разделённых пробелами
    """
    elements = fix_string_for_parse_input(expression).split()

    operator_stack = []
    postfix_notation = []
    operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    for element in elements:
        if element.isdigit():
            postfix_notation.append(int(element))
        elif element in operator_priority:
            while operator_stack and operator_stack[-1] != '(' and operator_priority.get(operator_stack[-1], 0) >= \
                    operator_priority[element]:
                postfix_notation.append(operator_stack.pop())
            operator_stack.append(element)
        elif element == '(':
            operator_stack.append(element)
        elif element == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_notation.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
            else:
                raise ValueError("Неправильное расположение скобок")
        else:
            raise ValueError("Некорректный символ")

    # Добавление оставшихся операторов в постфиксную нотацию
    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Неправильное расположение скобок в выражении")
        postfix_notation.append(operator_stack.pop())

    return postfix_notation
