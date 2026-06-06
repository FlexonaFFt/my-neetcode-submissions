class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        out = [0] * n 
        rightMax = -1

        for i in range(n - 1, -1, -1):
            out[i] = rightMax
            rightMax = max(arr[i], rightMax)

        return out