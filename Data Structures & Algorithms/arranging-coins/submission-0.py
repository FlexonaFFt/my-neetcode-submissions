class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right: 
            mid = (left + right) // 2
            need = mid * (mid + 1) // 2

            if need == n: return mid 
            elif need < n: left = mid + 1
            else: right = mid - 1

        return right