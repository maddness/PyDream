# 26
def max_in_list(a_list):
    return reduce(lambda x, y: max(x, y), a_list)


print max_in_list([2, 7, 3, 8, 5, 45, 67, 34, 5])

# 27
words = ['alf', 'gloom', 'snoop', 'rockstar']

print [len(word) for word in words]
print map(lambda x: len(x), words)

# 28
print reduce(lambda x, y: max(x, y), map(lambda x: len(x), words))


# 29
def filter_long_words(a_list, limit):
    return filter(lambda x: len(x) > limit, a_list)


print filter_long_words(words, 5)


# 30
def translate(sentence):
    vocabulary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    return map(lambda x: vocabulary.get(x, '---'), sentence)


print translate(['Santa', 'year', 'christmas'])


# 31
def my_map(fn, iterable):
    return [fn(i) for i in iterable]


def my_filter(fn, iterable):
    return [i for i in iterable if fn(i)]


def my_reduce(fn, iterable, initial=0):
    total = initial
    for i in iterable:
        total = fn(total, i)
    return total


print my_map(lambda x: x * 2, [1, 2, 3, 4, 5, 6, 7])
print my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print my_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
