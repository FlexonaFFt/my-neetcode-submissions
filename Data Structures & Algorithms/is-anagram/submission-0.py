from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first, second = Counter(s), Counter(t)
        return first == second