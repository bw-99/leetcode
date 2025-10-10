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

        queue = [(root, root.val)]
        while queue:
            curRoot, curSum = queue.pop(0)

            if (not (curRoot.left or curRoot.right)) and curSum == targetSum:
                is_exist = True
                break

            if curRoot.left:
                queue.append((curRoot.left, curSum+curRoot.left.val))
            if curRoot.right:
                queue.append((curRoot.right, curSum+curRoot.right.val))

        return is_exist