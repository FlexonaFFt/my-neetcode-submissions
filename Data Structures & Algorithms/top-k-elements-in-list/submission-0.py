class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, ans = collections.Counter(nums), []
        pairs = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [num for num, count in pairs[:k]]