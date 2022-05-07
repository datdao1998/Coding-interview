def optimalCandies(n, arr):
    candies = [1] * n
    for i in range(n - 1):
        if arr[i + 1] > arr[i]:
            candies[i + 1] = candies[i] + 1
    for i in range(n - 1, 0, -1):
        if arr[i - 1] > arr[i] and candies[i - 1] <= candies[i]:
            candies[i - 1] = candies[i] + 1
    return sum(candies)


n = 10
candies = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
print(optimalCandies(n, candies))
