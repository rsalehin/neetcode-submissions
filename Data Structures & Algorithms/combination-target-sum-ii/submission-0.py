class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, current_path, total):
            if total == target:
                result.append(current_path.copy())
                return
            if i == len(candidates) or total > target:
                return
            current_path.append(candidates[i])
            dfs(i + 1, current_path, total + candidates[i])
            current_path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs( i + 1, current_path, total)

        dfs(0, [], 0)
        return result

        