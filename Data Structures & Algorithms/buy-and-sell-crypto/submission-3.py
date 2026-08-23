class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best, minimal = 0, prices[0]

        for value in prices: 
            best = max(best, value - minimal)
            minimal = min(minimal, value)

        return best 