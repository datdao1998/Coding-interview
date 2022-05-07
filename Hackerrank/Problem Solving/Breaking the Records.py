#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    record_min, record_max = scores[0], scores[0]
    val_min, val_max = 0, 0
    for score in scores:
        if score < record_min:
            val_min += 1
            record_min = score
        if score > record_max:
            val_max += 1
            record_max = score

    return [val_max, val_min]
