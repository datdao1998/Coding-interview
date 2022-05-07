def getMinimumCost(k, c):
    c.sort(reverse=True)
    l = len(c)
    t = 0
    for i in range(l):
        t = t + (int(i / k) + 1) * c[i]
    return t


k = 3
c = [2, 5, 6]
print(getMinimumCost(k,c))
