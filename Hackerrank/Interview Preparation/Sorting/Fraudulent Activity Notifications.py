from bisect import bisect_left, insort_left


def activityNotifications(expenditure, d):
    # Write your code here
    notice = 0

    lastd = sorted(expenditure[:d])

    def med():
        return lastd[d // 2] if d % 2 == 1 else ((lastd[d // 2] + lastd[d // 2 - 1]) / 2)

    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * med():
            notice += 1
        del lastd[bisect_left(lastd, expenditure[i - d])]
        insort_left(lastd, expenditure[i])
    return notice


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5

print(activityNotifications(expenditure, d))
