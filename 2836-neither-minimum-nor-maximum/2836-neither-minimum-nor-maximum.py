class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_val, max_val = min(nums), max(nums)
        for n in nums:
            if n != min_val and n != max_val:
                return n
        return -1

