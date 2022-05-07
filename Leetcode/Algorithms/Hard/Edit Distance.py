import numpy


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distances = numpy.zeros((len(word1) + 1, len(word2) + 1))

        for t1 in range(len(word1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(word2) + 1):
            distances[0][t2] = t2

        a = 0
        b = 0
        c = 0

        for t1 in range(1, len(word1) + 1):
            for t2 in range(1, len(word2) + 1):
                if (word1[t1 - 1] == word2[t2 - 1]):
                    distances[t1][t2] = distances[t1 - 1][t2 - 1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1 - 1][t2]
                    c = distances[t1 - 1][t2 - 1]

                    if (a <= b and a <= c):
                        distances[t1][t2] = a + 1
                    elif (b <= a and b <= c):
                        distances[t1][t2] = b + 1
                    else:
                        distances[t1][t2] = c + 1

        return int(distances[len(word1)][len(word2)])
