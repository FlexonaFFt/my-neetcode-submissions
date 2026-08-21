class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1

        while left < right: 
            mid = (left + right) // 2
            counter = 0 

            for num in nums:
                if num <= mid: counter += 1

            if counter > mid: right = mid 
            else: left = mid + 1
        return left 