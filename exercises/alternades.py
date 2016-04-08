import operator


def make_alternades(a_word):
    if len(a_word) == 1:
        return a_word, ''

    first = ''.join(operator.itemgetter(*range(0, len(a_word), 2))(a_word))
    second = ''.join(operator.itemgetter(*range(1, len(a_word), 2))(a_word))
    return first, second


words = set()

with open('../data/unixdict.txt') as f:
    for word in f:
        words.add(word.strip())

for word in words:
    word1, word2 = make_alternades(word)
    if word1 in words and word2 in words:
        print '"{}": makes "{}" and "{}"'.format(word, word1, word2)
