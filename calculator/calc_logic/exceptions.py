from calculator.math_functions.math_funcs import functions, operators
import calculator.math_functions.math_funcs as funcs
from calculator.some_functions.decorators import decorator_sub


@decorator_sub
def print_info():
    print("Возможные команды:")
    for i in operators:
        print(i, '-', funcs.info[operators[i]])
    for i in functions:
        print(i, '-', funcs.info[i])


def check_for_command(user_input):
    if user_input == "help":
        print_info()
        return True

    if user_input == "":
        return True


def check_for_exit(user_input):
    phrases = ["goodbye", "exit", "quit", "выход", "стоп", "stop"]
    if user_input.lower() in phrases:
        return True
