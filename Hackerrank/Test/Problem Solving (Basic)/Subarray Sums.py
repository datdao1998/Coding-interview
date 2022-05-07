#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here

    zeros = []
    cnt_zero = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            cnt_zero += 1
            zeros.append(cnt_zero)
        else:
            zeros.append(cnt_zero)

    stackSum = []
    tmpSum = 0
    for i in range(len(numbers)):
        tmpSum += numbers[i]
        stackSum.append(int(tmpSum))

    result = []

    for query in queries:
        totalQueryValue = 0
        totalZeros = 0
        l, r, value = query[0], query[1], query[2]

        if l == 1:
            totalQueryValue += int(stackSum[r - 1])
            totalZeros += (zeros[r - 1]) * value
        else:
            totalQueryValue += int(stackSum[r - 1] - stackSum[l - 2])
            totalZeros += (zeros[r - 1] - zeros[l - 2]) * value
        result.append(int(totalZeros + totalQueryValue))

    # print("output = " + result)
    return result


numbers = [-5, 0]
queries = [[2, 2, 20], [1, 2, 10]]
print(findSum(numbers, queries))
