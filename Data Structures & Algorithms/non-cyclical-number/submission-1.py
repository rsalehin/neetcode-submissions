class Solution:
    def isHappy(self, n: int) -> bool:

        def nextNum(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total += digit**2
            return total 
        seen = set()
        while n != 0 and n not in seen:
            seen.add(n)
            n = nextNum(n)
        return n == 1

        