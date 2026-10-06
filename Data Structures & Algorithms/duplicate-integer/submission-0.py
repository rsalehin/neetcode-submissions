class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = dict()
        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = 1
        return False
         