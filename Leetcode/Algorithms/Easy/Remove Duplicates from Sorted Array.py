from collections import OrderedDict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = OrderedDict.fromkeys(nums).keys()
        return len(nums)
