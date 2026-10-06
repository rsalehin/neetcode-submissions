class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        # Initialize DP arrays
        hold = [0] * n
        sell = [0] * n
        cooldown = [0] * n
        
        # Base cases
        hold[0] = -prices[0]
        sell[0] = 0
        cooldown[0] = 0
        
        # Fill the DP arrays
        for i in range(1, n):
            hold[i] = max(hold[i-1], cooldown[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
            cooldown[i] = max(cooldown[i-1], sell[i-1])
        
        # The result is the maximum of cooldown or sell on the last day
        return max(sell[-1], cooldown[-1])

# Example Usage
solution = Solution()
prices = [1, 3, 4, 0, 4]
print(solution.maxProfit(prices))  # Output: 6
