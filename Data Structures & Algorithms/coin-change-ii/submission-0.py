class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Step 1: Get the number of coins and sort them (optional for clarity)
        n = len(coins)
        coins.sort()
        
        # Step 2: Initialize the DP table with dimensions (n+1) x (amount+1)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Step 3: Base case - There is 1 way to make amount 0 (by choosing no coins)
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Step 4: Iterate over coins in reverse to consider all subsets
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                # Step 5: Case 1 - Skip the current coin
                dp[i][a] = dp[i + 1][a]
                
                # Step 6: Case 2 - Include the current coin if the remaining amount is non-negative
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]
        
        # Step 7: Return the result stored in dp[0][amount]
        return dp[0][amount]
