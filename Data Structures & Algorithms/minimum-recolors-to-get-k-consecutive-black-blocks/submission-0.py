class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, best, white = 0, float('inf'), 0

        for right, value in enumerate(blocks):
            if value == 'W': white += 1

            while right - left + 1 > k: 
                if blocks[left] == "W":
                    white -= 1
                left += 1

            if right - left + 1 == k:
                best = min(best, white)

        return best 