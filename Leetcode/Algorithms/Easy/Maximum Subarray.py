class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        total = 0
        res = 0
        for i in nums:
            total += i
            if total < 0:
                total = 0
            res = max(res, total)
        return res
