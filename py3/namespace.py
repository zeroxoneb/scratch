#!/usr/bin/env python3

import types

d = {
    'key': 'value',
    'dict': {
        'key': 'value',
        'dict': {
            'key': 'value'
        }
    }
}

sn = types.SimpleNamespace(**d)
print(sn.dict.dict)
