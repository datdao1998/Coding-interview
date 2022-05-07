def longestSubarray(arr):
    if len(arr) < 2:
        return len(arr)

    best = 1
    bestLower = 1
    bestHigher = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            bestLower += 1
            bestHigher += 1
        elif arr[i] - 1 == arr[i - 1]:
            bestLower = 1 + bestHigher
            bestHigher = 1
        elif arr[i] + 1 == arr[i - 1]:
            bestHigher = 1 + bestLower
            bestLower = 1
        else:
            bestLower = 1
            bestHigher = 1
        best = max(best, bestHigher, bestLower)
    return best


arr = [0, 1, 2, 1, 2, 3]
print(longestSubarray(arr))
