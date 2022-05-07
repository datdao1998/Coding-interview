def maxSubsetSum(arr):
    if len(arr) < 3:
        return max(max(arr), 0)
    dp = [arr[0], max(arr[1], arr[0])]
    for i in range(2, len(arr)):
        dp.append(max(dp[i - 2] + arr[i], dp[i - 1], arr[i]))
    return max(max(dp), 0)


# arr = [-2, 1, 3, -4, 5]
# arr = [3, 7, 4, 6, 5]
# arr = [2, 1, 5, 8, 4]
# arr = [3, 5, -7, 8, 10]
arr = [-2, -3, -1]
print(maxSubsetSum(arr))
