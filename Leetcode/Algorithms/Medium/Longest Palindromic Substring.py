""""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""
        substring = ""
        for i in range(len(s)):
            odd = self.expandFromMiddle(s, i, i)
            even = self.expandFromMiddle(s, i, i + 1)
            maxString = odd if len(odd) > len(even) else even
            if len(maxString) > len(substring):
                substring = maxString
        return substring

    def expandFromMiddle(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
