def sockMerchant(n, ar):
    # Write your code here
    score = [0] * 101
    res = 0
    for i in range(n):
        score[ar[i]] += 1
    for i in range(101):
        res += score[i] // 2
    return res