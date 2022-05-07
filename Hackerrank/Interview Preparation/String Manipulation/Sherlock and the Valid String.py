from collections import Counter


def isValid(s):
    # Write your code here
    string = Counter(Counter(s).values())
    if len(string.keys()) == 1:
        return "YES"

    elif len(string.values()) == 2:
        key1, key2 = string.keys()
        if string[key1] == 1 and (key1 - 1 == key2 or key1 - 1 == 0):
            return "YES"
        elif string[key2] == 1 and (key2 - 1 == key1 or key2 - 1 == 0):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


s = "aaaabbcc"
print(isValid(s))
