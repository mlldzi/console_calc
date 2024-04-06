from .parser import parse_input
from .postfix import evaluate_postfix
from .exceptions import check_for_command, check_for_exit
from calculator.some_functions.work_with_history import logging_history


def start():
    while True:
        user_input = input("Введите выражение: ")

        if check_for_exit(user_input):
            break
        if check_for_command(user_input):
            start()

        try:
            expression = parse_input(user_input)
            result = evaluate_postfix(expression)
            logging_history(user_input, result)
            print(result)

        except ValueError as er:
            print(er)
