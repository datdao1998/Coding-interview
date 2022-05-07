def maximumToys(prices, k):
    # Write your code here
    prices = sorted(prices)
    if len(prices) == 1:
        return 1 if prices[0] <= k else 0
    for i in range(1, len(prices)):
        prices[i] += prices[i - 1]
    return next(x for x in range(len(prices)) if prices[x] > k)


prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50

print(maximumToys(prices, k))
