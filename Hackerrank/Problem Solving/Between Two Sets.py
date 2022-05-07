#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(a, b):
    while a * b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def lcm(a, b):
    return a * b // gcd(a, b)


def getTotalX(a, b):
    ans = 0
    # Write your code here
    lcm_a, gcd_b = a[0], b[0]
    for e in a:
        lcm_a = lcm(lcm_a, e)
    for e in b:
        gcd_b = gcd(gcd_b, e)

    if gcd_b % lcm_a > 0:
        return 0

    factor = gcd_b // lcm_a
    for i in range(1, factor + 1):
        if factor % i == 0:
            ans += 1
    return ans


a = [2, 6]
b = [24, 36]

print(getTotalX(a, b))
