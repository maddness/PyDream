from abc import ABCMeta, abstractmethod
import json


class Expression(object):
    __metaclass__ = ABCMeta

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def save(self):
        pass


class Literal(Expression):
    def __init__(self, value):
        super(Literal, self).__init__(value)

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, Literal):
            return self.value == other.value
        else:
            return False

    def __str__(self):
        return self.save()

    def save(self):
        return json.dumps(self.__dict__)


class Function(Expression):
    def __init__(self, value, arguments):
        super(Function, self).__init__(value)
        self.arguments = arguments

    def __hash__(self):
        return 31 * hash(self.value) + sum([i.__hash__() for i in self.arguments])

    def __eq__(self, other):
        if isinstance(other, Function):
            return self.value == other.value and self.arguments == other.arguments
        else:
            return False

    def __str__(self):
        return self.save()

    def save(self):
        return json.dumps({'value': self.value, 'arguments': map(lambda x: str(x), self.arguments)})


def load_expression(string):
    raw_expression = json.loads(string)
    if 'value' in raw_expression:
        if 'arguments' in raw_expression:
            return Function(raw_expression['value'], raw_expression['arguments'])
        else:
            return Literal(raw_expression['value'])


lit1 = Literal('35')
lit2 = Literal(12)

# print load_expression(lit1.save())
# print load_expression(lit1.save()) == lit1


func1 = Function('g', [lit1, lit2])
print func1.save()

print load_expression(func1.save())
print load_expression(func1.save()) == func1
