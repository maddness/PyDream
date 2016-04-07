class SetInfo(object):
    def __init__(self, element):
        self.count = 1
        self.group = {element}

    def add_element(self, element):
        self.count += 1
        self.group.add(element)


def sort_word(chars):
    return ''.join(sorted(chars))


dic = {}

with open('../data/unixdict.txt') as f:
    for line in f:
        word = line.rstrip()
        key = sort_word(word)
        if key in dic:
            dic[key].add_element(word)
        else:
            dic[key] = SetInfo(word)

result = sorted(dic.values(), key=lambda x: x.count, reverse=True)

print '\n'.join(map(lambda x: str(x.group), result[:10]))
