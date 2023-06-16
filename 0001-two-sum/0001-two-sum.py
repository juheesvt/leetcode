class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = dict()
        for idx, value in enumerate(nums):

            if target-value in nums[idx+1:] or target-value in nums[0:idx]:
                answer[idx] = value

        return answer.keys()