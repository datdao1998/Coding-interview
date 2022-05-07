import math
import os
import random
import re
import sys


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    totalPrice = sum(bill)
    values = []
    for price in bill:
        values.append(totalPrice - price)
    actual = values[k] // 2
    if b > actual:
        print(b - actual)
    else:
        print('Bon Appetit')
