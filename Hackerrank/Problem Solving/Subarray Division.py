#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(0, len(s) + 1 - m):
        if sum(s[i:i + m]) == d:
            count += 1
    return count
