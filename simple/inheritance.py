class Animal(object):
    def __init__(self):
        print 'constructing Animal'

    def say_hi():
        return 'generic hi!'


class Doge(Animal):
    def __init__(self):
        print 'constructing Doge'

    # def



poxy = Doge()
print poxy.say_hi()
print Doge.say_hi()