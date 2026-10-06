class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute force solution

        res = [0] * len(nums)
        n = len(nums)

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res


        