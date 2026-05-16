class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, n, m = 0, len(s1), len(s2)
        if n > m: return False 
        need, window = [0] * 26, [0] * 26 

        for char in s1: need[ord(char) - ord('a')] += 1
        for i in range(n): window[ord(s2[i]) - ord('a')] += 1
        if window == need: return True 
        for right in range(n, m):
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if window == need: return True 

        return False 