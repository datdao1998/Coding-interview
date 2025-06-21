class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = {i: True for i in range(len(nums) + 1)}
        for num in nums:
            arr.pop(num)
        return list(arr.keys())[0]
            