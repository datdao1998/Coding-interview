from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = dict(Counter(nums))
        return True if any(counter[x] > 1 for x in counter) else False
