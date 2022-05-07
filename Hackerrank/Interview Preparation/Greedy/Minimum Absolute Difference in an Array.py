def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    distance = []
    for i in range(1, len(arr)):
        distance.append(abs(arr[i] - arr[i - 1]))
    return min(distance)


arr = [1, -3, 71, 68, 17]
print(minimumAbsoluteDifference(arr))
