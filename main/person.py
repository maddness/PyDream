class Person:
    def __init__(self, age=1, name='zombie'):
        self.age = age
        self.name = name

    def __add__(self, other):
        print 'in add - self: ' + str(self) + ', other: ' + str(other)
        return Person(self.age + other.age)

    def __radd__(self, other):
        print 'in radd - self: ' + str(self) + ', other: ' + str(other)
        return Person(self.age + other, self.name)

    def __eq__(self, other):
        print '__eq__() | self: ' + str(self) + ', other: ' + str(other)
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        return hash((self.age, self.name))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '[{},{}]'.format(self.name, self.age)


a = Person(23, "mark")
b = Person(23, "mark")

dic = {a: 123}

print dic[b]
