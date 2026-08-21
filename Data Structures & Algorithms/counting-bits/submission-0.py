class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for curr in range(n + 1):
            bite = str(bin(curr)[2:])
            output.append(bite.count('1'))
        return output