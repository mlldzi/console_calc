from datetime import datetime
from calculator.calc_logic.fix_string import fix_string_for_parse_input


def logging_history(expression, result):
    expression = fix_string_for_parse_input(expression)

    path = r"database\history.txt"
    with open(path, "a") as file:
        file.write(f"{datetime.now().replace(microsecond=0)}: {expression} = {result}\n")


def read_history():
    path = r"database\history.txt"
    with open(path, "r") as file:
        return file.read()
