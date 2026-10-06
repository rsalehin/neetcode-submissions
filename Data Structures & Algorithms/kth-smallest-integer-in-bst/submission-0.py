# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        result = []
        def in_order_dfs(current_node):
            if current_node.left:
                in_order_dfs(current_node.left)
            result.append(current_node.val)
            if current_node.right:
                in_order_dfs(current_node.right)
        in_order_dfs(root)
        return result[k-1]
            

        