from collections import Counter


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    dictionary = dict(Counter(a))
    keys = list(dictionary.keys())
    keys.sort()
    res = 0
    for key in keys:
        val = dictionary[key]
        if (key + 1) in keys:
            val += dictionary[key + 1]
        res = max(res, val)
    return res
