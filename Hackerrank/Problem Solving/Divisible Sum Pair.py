def divisibleSumPairs(n, k, ar):
    # Write your code here
    div = [0 for mod in range(k)]
    for ele in ar:
        div[ele % k] += 1

    res = div[0] * (div[0] - 1)
    for i in range(1, k):
        res += div[i] * (div[i] - 1) if k == 2 * i else div[i] * div[k - i]

    return res // 2


n = 5
k = 2
ar = [5, 9, 10, 7, 4]

print(divisibleSumPairs(n, k, ar))
