def rotLeft(a, d):
    # Write your code here
    index = d % len(a)
    return a if index == 0 else a[index:] + a[:index]