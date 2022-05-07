""""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
    return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        dictionary = {}
        for c in nums3:
            for d in nums4:
                dictionary[c + d] = dictionary.get(c + d, 0) + 1
        count = 0
        for a in nums1:
            for b in nums2:
                count += dictionary.get(-(a + b), 0)

        return count


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(Solution().fourSumCount(nums1, nums2, nums3, nums4))
