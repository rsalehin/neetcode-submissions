class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return [list(t) for t in res]
        