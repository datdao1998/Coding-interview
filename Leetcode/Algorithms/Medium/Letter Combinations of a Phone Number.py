class Solution(object):

    def combination(self, list1, list2):
        out = []
        for i in list1:
            for j in list2:
                out.append(i + j)
        return out

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        dictionary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = ['']
        for digit in digits:
            res = self.combination(res, dictionary[digit])
        return res


digits = ""
print(Solution().letterCombinations(digits))

# a = ['']
# b = ['c', 'd']
# print(Solution().combination(a, b))
