#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

import string

P = 131
M = 1e9 + 7
PP = [P ** i for i in range(11)]
APPENDS = [""] + list(string.ascii_letters) + [str(d) for d in range(10)]


def calc_hash(pw):
    cur_h = 0
    for i in range(len(pw)):
        cur_h += ord(pw[-(i + 1)]) * PP[i]
    return cur_h % M


def authEvents(events):
    # Write your code here
    cur_h = None
    good_hashs = None
    ans = []
    for event, value in events:
        if event == "setPassword":
            good_hashs = set(calc_hash(value + x) for x in APPENDS)
        else:
            assert event == "authorize"
            ans.append(1 if int(value) in good_hashs else 0)
    return ans



