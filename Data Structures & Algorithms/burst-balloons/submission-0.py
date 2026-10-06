class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums +  [1]
        n = len(nums)
        dp = [[0]*n for i in range(n)]

        for subarray_length in range(1, n-1):
            for start_index in range(n - subarray_length):
                end_index = start_index + subarray_length - 1
                for k in range(start_index, end_index + 1):
                    gain = nums[start_index -1]* nums[k] * nums[end_index + 1]
                    dp[start_index][end_index] = max(dp[start_index][end_index], gain + dp[start_index][k-1]+dp[k+1][end_index])
        return dp[1][n-2]
        