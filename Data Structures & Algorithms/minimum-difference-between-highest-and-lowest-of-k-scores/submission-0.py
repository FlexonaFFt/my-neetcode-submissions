class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, best = 0, float('inf')

        for right in range(len(nums)):
            
            while right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                best = min(best, nums[right] - nums[left])

        return best 