from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, best, max_curr, curr = 0, 0, 0, Counter()

        for right, char in enumerate(s):
            curr[char] = curr.get(char, 0) + 1
            max_curr = max(max_curr, curr[char])

            while (right - left + 1) - max_curr > k:
                curr[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return best 