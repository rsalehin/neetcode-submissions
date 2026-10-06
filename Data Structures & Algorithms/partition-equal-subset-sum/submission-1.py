class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 != 0:
            return False
        target = total_sum // 2
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for sums in range(1, target + 1):
                if nums[i-1]<=sums:
                    dp[i][sums] = dp[i-1][sums] or dp[i-1][sums-nums[i-1]]
                else:
                    dp[i][sums] = dp[i-1][sums]
        return dp[n][target]         