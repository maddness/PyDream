def multi():
    return [lambda x: i * x for i in range(4)]

print [i(3) for i in multi()]
