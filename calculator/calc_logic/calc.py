from .parser import parse_input


def start():
    user_input = input("Введите выражение: ")
    print(parse_input(user_input))
