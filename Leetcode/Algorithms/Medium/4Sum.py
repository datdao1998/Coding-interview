class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        s = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        s.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1

        return s
