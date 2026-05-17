from collections import defaultdict 

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum, counter = 0, defaultdict(int)
        counter[0], output = 1, 0 

        for value in nums:
            prefix_sum += value
            output += counter[prefix_sum - goal]
            counter[prefix_sum] += 1

        return output