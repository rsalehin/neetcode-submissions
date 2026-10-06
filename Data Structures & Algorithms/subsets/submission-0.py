class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # List to store all subsets
        current_subset = []  # Temporary list to build individual subsets

        def backtrack(index):
            """
            Recursive function to generate all subsets.
            
            Args:
                index: The current index in the 'nums' array being considered.
            """
            # Base case: If we have considered all elements
            if index == len(nums):
                result.append(current_subset.copy())  # Add a copy of the current subset to the result
                return 
            
            # Include the current element (nums[index]) in the subset
            current_subset.append(nums[index])
            backtrack(index + 1)  # Recur for the next index

            # Exclude the current element (backtrack)
            current_subset.pop()  # Remove the last element to explore the next path
            backtrack(index + 1)  # Recur for the next index

        # Start backtracking from the first index
        backtrack(0)
        return result
