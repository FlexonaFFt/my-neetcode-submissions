class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums, longest = set(nums), 0

        for num in setnums:
            if num - 1 not in setnums:
                curr, length = num, 1
                while curr + 1 in setnums:
                    curr += 1 
                    length += 1
                
                longest = max(length, longest)
        
        return longest