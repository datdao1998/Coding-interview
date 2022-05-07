""""
Example : 1 3 3

We will store element like that
3 0 0 -3 0
Meaning

First element is 3 greater than 0.
Second  ->       0 greater than index 1 element.
Third   ->       0 greater than index 2 element
Fourth  ->      -3 greater than index 3 element.
fifth   ->       0 greater than index 4 element.
"""


def arrayManipulation(n, queries):
    # Write your code here
    score = [0] * (n + 1)
    for query in queries:
        start, end, value = query[0] - 1, query[1] - 1, query[2]
        score[start] += value
        score[end + 1] -= value

    maxValue = score[0]
    first = 0
    for i in range(len(score) - 1):
        first += score[i]
        if first > maxValue:
            maxValue = first

    return maxValue


n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
print(arrayManipulation(n, queries))
