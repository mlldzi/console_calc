import math


def push_to_stack(element, stack):
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
