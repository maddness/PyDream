import random

for i in range(10):
    print random.random()

for i in range(10):
    # included the endpoint
    print random.randint(1, 10)

for i in range(10):
    # excluded the endpoint
    print random.randrange(1, 10)
