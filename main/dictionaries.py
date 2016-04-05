dic = {1: 'alex', 2: 'bob', 3: 'ron'}

# no exceptions
print dic.get(2)

# default value if no such key
print dic.get(8, 'no_name')

# KeyError raised if no key
try:
    print dic[9]
except KeyError:
    print 'better use get()'

# get and remove entity
val = dic.pop(1)
print dic

# keys and values
print dic.keys()
print dic.values()
print list(dic.iteritems())

# clear dictionary
dic.clear()
print dic

