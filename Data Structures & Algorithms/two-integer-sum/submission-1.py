class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for index, num in enumerate(nums):
            num_dict[num] = index

        for current_index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict and num_dict[complement] != current_index:
                return [current_index, num_dict[complement]]
        

        