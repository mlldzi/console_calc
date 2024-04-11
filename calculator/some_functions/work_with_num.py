import math


def push_to_stack(element, stack):
    """
    Функция для добавления в массив(стек), пришлось так сделать,
    потому что пайтон не может обработать такого рода числа int("2.3")
    Поэтому, если ошибка на int("2.3"), то число однозначно флоат
    """
    try:
        stack.append(int(element))
    except:
        try:
            stack.append(float(element))
        except:
            pass


def check_for_pi(element, stack):
    if element in ['pi', 'p']:
        stack.append(math.pi)
    else:
        stack.append(-math.pi)


def check_for_e(element, stack):
    if element == 'e':
        stack.append(math.e)
    else:
        stack.append(-math.e)


def evaluate_special_function(functions, spec_func, nums_for_spec_functions, postfix_notation):
    """
    Функция для обработки НОД и НОК
    """
    nums = []
    for elem in nums_for_spec_functions[2:-1]:
        push_to_stack(elem, nums)

    spec_func_to_eval = functions[spec_func]
    postfix_notation.append(spec_func_to_eval(*nums))

    spec_func = None
    nums_for_spec_functions = []

    return spec_func, nums_for_spec_functions


def evaluate_exp(num_for_exp, postfix_notation):
    """
    Функция для обработки экспоненты
    """
    num_for_exp = int(num_for_exp[2])
    postfix_notation.append(math.exp(num_for_exp))
    num_for_exp = []
    return num_for_exp
