class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnSize = len(columnTitle)
        res = 0
        for i in range(columnSize - 1):
            res += self.countPrePosition(i + 1)
        
        for i in range(len(columnTitle)):
            currentCharacter = columnTitle[i]
            res += (ord(currentCharacter) - ord('A')) * self.countPrePosition(columnSize - i - 1)
        
        return res + 1

    
    def countPrePosition(self, n):
        s = 1
        for i in range(n):
            s = s * 26
        return s


if __name__ == "__main__":
    solution = Solution()
    columnTitles = [
        "A",
        "AB",
        "ZY"
    ]

    for columnTitle in columnTitles:
        print(solution.titleToNumber(columnTitle))