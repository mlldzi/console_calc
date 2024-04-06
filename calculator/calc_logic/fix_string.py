def fix_string_for_parse_input(expression):
    """
    Функция для добавления пробелов из выражения для корректной обработки
    """
    expression_with_spaces = ""
    for char in expression:
        if char.isdigit() or char.isalpha():
            expression_with_spaces += char
        else:
            expression_with_spaces += " " + char + " "
    return expression_with_spaces