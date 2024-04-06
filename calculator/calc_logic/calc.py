from .parser import parse_input
from .postfix import evaluate_postfix

def start():
    user_input = input("Введите выражение: ")
    expression = parse_input(user_input)
    result = evaluate_postfix(expression)
    print(result)
