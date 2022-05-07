"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        lst = ['' for i in range(numRows)]

        step = 1
        index = 0
        for i in s:
            if index == numRows:
                step = -1
                index -= 2
            if index == -1:
                step = 1
                index += 2
            lst[index] = lst[index] + i
            index += step
        return ''.join(lst)


s = 'ABCD'
numRows = 2

print(Solution().convert(s, numRows))
