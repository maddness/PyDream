import random


def check_brackets(a_line):
    total = 0
    for i in a_line:
        if i == '[':
            total += 1
        elif i == ']':
            total -= 1
        else:
            raise TypeError('not a bracket!')

        if total < 0:
            return False

    return True if total == 0 else False


def generate_brackets(length=10):
    result = ''
    for i in range(length):
        result += '[' if random.randint(0, 1) == 0 else ']'
    return result


for count in range(10):
    line = generate_brackets()
    print line, ' ', check_brackets(line)
