from functools import wraps


def decorator_sub(func):
    @wraps(func)
    def wrapper():
        print('*' * 52)
        func()
        print('*' * 52)

    return wrapper
