class Solution:
    def function(self, num: int) -> int:
        num, summa = str(num), 0
        for char in num: 
            summa += int(char) ** 2

        return summa
    
    def isHappy(self, n: int) -> bool:
        seen = set() 

        while n != 1:

            if n in seen: 
                return False 
            seen.add(n)
            n = self.function(n)

        return True 