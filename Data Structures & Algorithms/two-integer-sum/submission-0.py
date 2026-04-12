from collections import Counter 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = Counter()

        for right, val in enumerate(nums):
            index[val] = right 

        for right, val in enumerate(nums):
            diff = target - val
            if diff in index and index[diff] != right:
                return [right, index[diff]]
        return []