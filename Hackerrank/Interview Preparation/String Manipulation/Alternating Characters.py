def alternatingCharacters(s):
    # Write your code here
    if len(s) == 1:
        return 0

    res = 0
    cnt = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            res += cnt
            cnt = 0
        else:
            cnt += 1
    if cnt > 0:
        res += cnt
    return res


s = 'AAABBB'
print(alternatingCharacters(s))
