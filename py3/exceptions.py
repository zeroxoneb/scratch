#!/usr/bin/env python3

import sys
import traceback

def _raiser(msg):
    raise Exception(msg)

try:
    _raiser("exception")
except Exception:
    e_cls, e, e_tb = sys.exc_info()
    for l in traceback.format_tb(exc_traceback):
        print(l,)
    # print(traceback.format_tb(exc_traceback))
