def hourglassSum(arr):
    # Write your code here
    maxValue = (-9) * 36

    for i in range(1, 5):
        for j in range(1, 5):
            value = arr[i][j] + sum(arr[i - 1][j - 1:j + 2]) + sum(arr[i + 1][j - 1:j + 2])
            maxValue = max(maxValue, value)

    return maxValue


arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))
