class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]

        for value in nums[1:]:
            curr = max(value, curr + value)
            best = max(best, curr)

        return best