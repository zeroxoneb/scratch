#!/usr/bin/env python3

import uuid

def char8(uuid):
    allowed = 'abcdefghijkmnopqrstuvwxyz1234567890' * 6
    b = ""
    a = uuid.hex
    while a:
        b += allowed[int(a[:2], 16) & 0xaf]
        a = a[4:]

    return b

print(char8(uuid.uuid4()))
