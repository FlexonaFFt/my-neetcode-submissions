class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_counter = 1, 0 
        for num in nums:
            if num: prod *= num 
            else: zero_counter += 1
        if zero_counter > 1: return[0] * len(nums)

        res = [0] * len(nums)
        for idx, item in enumerate(nums):
            if zero_counter: res[idx] = 0 if item else prod
            else: res[idx] = prod // item
        return res