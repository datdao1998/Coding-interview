def substrCount(n, s):
    count = n  # Initialize with n as each character is a special palindromic string.
    streak = [1] * n  # Initialize streak with all 1s.

    for i in range(1, n):
        # This condition checks for the aa, aaa, .... types and also updates the streak             array.
        if s[i] == s[i - 1]:
            count += streak[i - 1]
            streak[i] = streak[i - 1] + 1

        # This condition checks for aba, aabaa, .... types.
        temp = i - streak[i] - 1
        if temp >= 0:
            if s[i] == s[temp] and streak[i] <= streak[temp]:
                count += 1

    return count


n = 4
s = 'aaaa'
print(substrCount(n, s))
