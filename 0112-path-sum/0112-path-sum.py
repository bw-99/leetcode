# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        is_exist = False

        if not root:
            return False

        def dfs(root, curSum):
            nonlocal targetSum, is_exist

            curSum += root.val

            if (curSum == targetSum) and not ((root.left) or (root.right)):
                is_exist = True
                return

            if root.left:
                dfs(root.left, curSum)
            
            if root.right:
                dfs(root.right, curSum)
        
        dfs(root, 0)

        return is_exist