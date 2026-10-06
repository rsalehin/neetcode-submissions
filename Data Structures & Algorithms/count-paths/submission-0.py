class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Adding extra row and column to avoid out of bound error. 
        dp = [[0] * (n+1) for _ in range(m+1)]
        #Define the base case
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
        