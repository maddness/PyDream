# filename = raw_input('enter file name: ')
filename = '../data/file.txt'

with open(filename, 'r') as source, open('../data/result.txt', 'w') as target:
    for index, line in enumerate(source):
        target.write(str(index + 1) + ' ' + line)
