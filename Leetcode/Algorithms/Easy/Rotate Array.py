from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            k = k % len(nums)
            if k > 0:
                concate1 = nums[-k:]
                concate2 = nums[:-k]
                for i in range(len(nums)):
                    if i < k:
                        nums[i] = concate1[i]
                    else:
                        nums[i] = concate2[i - k]
