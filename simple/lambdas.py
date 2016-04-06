def create_multipliers():
    return [lambda x: i * x for i in range(5)]


mult = lambda x, y: x * y

print mult(2, 4)
# fully anonymous

print (lambda x, y: x + y)(5, 8)

# --------
for i in create_multipliers():
    print i(3)
