#!/usr/bin/env python3
import copy
import collections
import datetime
import uuid


SHAPE = collections.namedtuple(                                                     
    'SHAPE', (
        'CIRCLE',
        'SQUARE',
        'TRIANGLE',
        'RHOMBUS',
    )
)(
    'circle',
    'square',
    'triangle',
    'rhombus',
)

def test_deepcopy(d):
    print('id(d): {}'.format(id(d)))
    print(d)

    deep = copy.deepcopy(d)
    print('id(deep): {}'.format(id(deep)))
    print(deep)

if __name__ == '__main__':
    test_deepcopy({
        'time': datetime.datetime.now(),
        'uuid': uuid.uuid4(),
        'shape': SHAPE.CIRCLE
    })
