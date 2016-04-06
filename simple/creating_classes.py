def class_creator(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


RonClass = class_creator('ron')
print RonClass
print RonClass()

FooClass = class_creator('foo')
print FooClass
print FooClass()

# creation with type()
MyLittlePony = type('MyPony', (), {'name': 'Lola', 'age': 8})
print MyLittlePony
print MyLittlePony().name


# dynamic creation
def say_my_name(self):
    return 'Joel'

BattleBorn = type('BattleBorn', (), {'say_my_name': say_my_name})


print hasattr(BattleBorn, 'say_my_name')
print BattleBorn().say_my_name()


