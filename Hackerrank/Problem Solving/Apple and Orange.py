def condition(s, t, coordinate):
    return s <= coordinate and t >= coordinate


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app = [a + apple for apple in apples]
    ora = [b + orange for orange in oranges]
    print(len([i for i in app if condition(s, t, i)]))
    print(len([o for o in ora if condition(s, t, o)]))


s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)
