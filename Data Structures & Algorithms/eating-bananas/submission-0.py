class Solution:
    
    def needed(self, piles: List[int], k: int): 
        return sum((p + k - 1) // k for p in piles)
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right 

        while left <= right:
            mid = (left + right) // 2
            if self.needed(piles, mid) <= h:
                res = mid 
                right = mid - 1
            else: left = mid + 1

        return res 
    