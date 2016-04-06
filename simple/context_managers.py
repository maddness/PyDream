from contextlib import contextmanager


class fileopen_class(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def fileopen_iter(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()


# class way
with fileopen_class('../data/file.txt') as f:
    for line in f:
        print line,

print '\n' + '===' * 10

# iterator way
with fileopen_iter('../data/file.txt') as d:
    for line in d:
        print line,
