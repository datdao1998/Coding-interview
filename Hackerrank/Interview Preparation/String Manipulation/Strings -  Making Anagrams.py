from collections import Counter


def makeAnagram(a, b):
    # Write your code here
    keep = 0
    candidate = list(set(a + b))
    counter_a = dict(Counter(a))
    counter_b = dict(Counter(b))
    for c in candidate:
        if c in counter_a.keys() and c in counter_b.keys():
            keep += min(counter_a[c], counter_b[c])
    return len(a) + len(b) - 2 * keep


a = 'cde'
b = 'abc'
print(makeAnagram(a, b))
