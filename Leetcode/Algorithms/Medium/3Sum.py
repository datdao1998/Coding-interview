"""
Constrains:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Input : [-1, 0, 1, 2, -1, -4]
Output: [[-1,-1,2],[-1,0,1]]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = - nums[i]
            s, e = i + 1, n - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    while s < e and nums[s] == nums[s - 1]:
                        s = s + 1
                elif nums[s] + nums[e] < target:
                    s = s + 1
                else:
                    e = e - 1
        return result


nums = [-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(nums))
