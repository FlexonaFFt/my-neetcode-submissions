class Solution:
    def mySqrt(self, x: int) -> int:
        down_num, up_num, out = 0, x, 0

        while down_num <= up_num:
            mid = down_num + (up_num - down_num) // 2
            if mid ** 2 > x:
                up_num = mid - 1
            elif mid ** 2 < x:
                down_num = mid + 1
                out = mid 
            else: return mid 
        return out