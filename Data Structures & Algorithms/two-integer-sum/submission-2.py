class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in mapping:
                return [mapping[complement], index] 
            mapping[num] = index
        return []
        