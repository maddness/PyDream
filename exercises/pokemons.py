class Item(object):
    def __init__(self, index):
        self.index = index
        self.free = True


def words_fit(first, second):
    return first[-1] == second[0]


def search():
    global best_line

    for item in indexes:
        line_is_empty = len(pokemon_line) == 0
        if line_is_empty or (item.free and words_fit(pokemon_line[-1], pokemons[item.index])):
            pokemon_line.append(pokemons[item.index])
            item.free = False
            search()
            pokemon_line.pop()
            item.free = True

    if len(pokemon_line) > len(best_line):
        best_line = pokemon_line[:]

    if len(pokemon_line) == 0:
        print best_line


if __name__ == '__main__':
    with open('../data/poke_small.txt') as f:
        pokemons = sum(map(lambda x: x.split(), f.readlines()), [])

    indexes = [Item(i) for i in range(len(pokemons))]

    best_line = []
    pokemon_line = []

    search()



"""
'machamp', 'petilil', 'landorus', 'scrafty', 'yamask', 'kricketune',
'emboar', 'registeel', 'loudred', 'darmanitan', 'nosepass', 'simisear',
'relicanth', 'heatmor', 'rufflet', 'trapinch', 'haxorus', 'seaking',
'girafarig', 'gabite', 'exeggcute', 'emolga', 'audino'
"""
