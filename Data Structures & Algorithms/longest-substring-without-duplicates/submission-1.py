from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, curr, best = 0, Counter(), 0 

        for right, value in enumerate(s):
            curr[value] = curr.get(value, 0) + 1

            while curr[s[right]] > 1:
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1

            best = max(best, right - left + 1)

        return best