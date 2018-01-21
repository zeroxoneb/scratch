#!/usr/bin/env python3

import enum

class Shape(enum.Enum):
    CIRCLE = 'circle'
    SQUARE = 'square'
    TRIANGLE = 'triangle'

    def __repr__(self):
        return str(self._value_)

print(Shape.CIRCLE.value)
print(Shape('circle'))
