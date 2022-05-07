def maxPairs(skillLevel, minDiff):
    # Write your code here
    skillLevel.sort()
    n = len(skillLevel)
    t = 0
    a = 0
    b = n // 2
    while a < n // 2 and b < n:
        if (skillLevel[b] - skillLevel[a] >= minDiff):
            t += 1
            a += 1
        b += 1
    return t


skillLevel = [1, 2, 3, 4, 5, 6]
minDiff = 4

print(maxPairs(skillLevel, minDiff))
