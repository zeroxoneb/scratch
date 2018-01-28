#!/usr/bin/env python3

import random

print "02:%02x:%02x:%02x:%02x:%02x" % (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
)
