class Solution:
    def scoreOfString(self, s: str) -> int:
        counter = 0 
        for i in range(1, len(s)):
            counter += abs(ord(s[i]) - ord(s[i - 1]))
        return counter