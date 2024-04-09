from datetime import datetime
from calculator.calc_logic.fix_string import fix_string_for_parse_input
from calculator.some_functions.brackets import brackets_fix


def logging_history(expression, result):
    expression = fix_string_for_parse_input(expression)
    expression = brackets_fix(expression)

    path = r"database\history.txt"
    with open(path, "a") as file:
        file.write(f"{datetime.now().replace(microsecond=0)}: {expression} = {result}\n")


def read_history(length=9):
    path = r"database\history.txt"
    with open(path, "r") as file:
        lines = file.readlines()
        if length > len(lines):
            length = len(lines)
        lines = lines[-length:]
        lines[length - 1] = lines[length - 1].strip()
        return "".join(lines)
