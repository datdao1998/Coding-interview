from collections import Counter


def twoStrings(s1, s2):
    # Write your code here
    cnt1 = Counter([char for char in s1])
    cnt2 = Counter([char for char in s2])
    return "NO" if cnt1 - cnt2 == cnt1 else "YES"


s1 = 'hello'
s2 = 'world'
print(twoStrings(s1, s2))
