class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # If (target + total_sum) is odd or negative, it's not possible
        if target > total_sum or (target + total_sum) % 2 != 0:
            return 0
        
        subset_sum = (target + total_sum) // 2
        
        # Step 1: Create a DP table
        dp = [[0] * (subset_sum + 1) for _ in range(len(nums) + 1)]
        
        # Step 2: Base case
        for i in range(len(nums) + 1):
            dp[i][0] = 1  # There's one way to make a sum of 0 (by selecting no elements)
        
        # Step 3: Fill the DP table
        for i in range(1, len(nums) + 1):
            for s in range(subset_sum + 1):
                # Exclude current number
                dp[i][s] = dp[i - 1][s]
                
                # Include current number if possible
                if s >= nums[i - 1]:
                    dp[i][s] += dp[i - 1][s - nums[i - 1]]
        
        return dp[len(nums)][subset_sum]
