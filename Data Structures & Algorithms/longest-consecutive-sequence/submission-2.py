class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in store:  # Iterate over the set to avoid duplicates
            if num - 1 not in store:  # Start a new streak only if num is the beginning
                streak, curr = 1, num
                while curr + 1 in store:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res
