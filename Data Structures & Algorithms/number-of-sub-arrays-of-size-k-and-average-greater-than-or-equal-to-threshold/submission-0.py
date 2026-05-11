class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n, need = len(arr), k * threshold
        left, curr, counter = 0, 0, 0

        for right in range(n):
            curr += arr[right]
            if right - left + 1 > k:
                curr -= arr[left]
                left += 1

            if right - left + 1 == k and curr >= need:
                counter += 1

        return counter 