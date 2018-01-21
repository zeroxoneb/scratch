from typing import TypeVar, Generic

T = TypeVar('T')

class Field(Generic[T]):
    def __init__(self, value: T = None) -> None:
        print(f'__init__(self: {self}, value: {value})')
        self.default = value

    def __get__(self, instance, owner) -> T:
        print(f'__get__(self: {self}, instance: {instance}, owner: {owner})')
        if self.name not in instance.__dict__:
            self.__set__(instance, self.default)

        return instance.__dict__[self.name]

    def __set__(self, instance, value: T) -> None:
        print(f'__set__(self: {self}, instance: {instance}, value: {value})')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name: str) -> None:
        print(f'__set_name__(self: {self}, owner: {owner}, name: {name})')
        self.name = name

Str = Field[str]
Int = Field[int]

class Model:
    _str: Str = Str('default')
    _int: Int = Int('fail')

m = Model()
print(f'm._str = {m._str}')
m._str = 'str'
m._int = 1
print(f'm._str = {m._str}')
print(f'm._int = {m._int}')

# Set int field to a string that can't be converted
m._int = {}
print(f'm._int = {m._int}')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items = []  # type: List[T]

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

default = 1
s = Stack[str]()
s.push(default)
s.push('string')

print(s.items)


class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

Box(1)
Box[int](1)
s = 'some string'
Box[int](s)
