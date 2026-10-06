class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base Case
        if n == 0:
            return 1
        # When n is negative

        if n<0:
            return 1.0/pow(x, -1*n)
        
        # If n is odd

        if n%2 == 1:
            return x*self.myPow(x*x, (n-1)//2)
        
        # If n is even
        else:
            return self.myPow(x*x, n//2)
        