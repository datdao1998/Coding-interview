import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        closestDiff = math.inf
        sign = 1
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(target - s) < closestDiff:
                    sign = -1 if target - s < 0 else 1
                closestDiff = min(abs(target - s), closestDiff)
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return target - (closestDiff * sign)
