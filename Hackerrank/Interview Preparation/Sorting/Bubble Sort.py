def countSwaps(a):
    # Write your code here
    step = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                step += 1
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

    print("Array is sorted in {} swaps.".format(str(step)))
    print("First Element: {}".format(str(a[0])))
    print("Last Element: {}".format(str(a[-1])))


a = [3, 4, 1, 2]
countSwaps(a)
