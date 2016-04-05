def foo(a, b, c, d):
    return ','.join(map(str, [a, b, c, d]))


def return_args(*args):
    return args


a = (1, 3, 5, 6)
print foo(*a)

print return_args('a', 5, True)
