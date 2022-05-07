from collections import Counter


def migratoryBirds(arr):
    # Write your code here
    counter = dict(Counter(arr))
    maxOccurs = max(list(counter.values()))

    keys = sorted(list(counter.keys()))

    for key in keys:
        if counter[key] == maxOccurs:
            return key


arr = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(arr))
