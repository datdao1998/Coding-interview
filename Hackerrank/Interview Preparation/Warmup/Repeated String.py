def repeatedString(s, n):
    # Write your code here
    frequency = s.count('a')
    x1, y1 = n % len(s), n // len(s)
    return y1 * frequency if x1 == 0 else y1 * frequency + s[:x1].count('a')

s = 'aba'
n = 10
print(repeatedString(s,n))
