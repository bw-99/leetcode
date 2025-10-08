# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    solutions = []
    tmp_solutions = []

    def dfs(self, root: Optional[TreeNode], targetSum: int, curSum: int):
        self.tmp_solutions.append(root.val)

        if not(root.left or root.right):
            if curSum == targetSum:
                self.solutions.append([item for item in self.tmp_solutions])
        
        if root.left:    
            self.dfs(root.left, targetSum, curSum + root.left.val)
            self.tmp_solutions.pop(-1)
        
        if root.right:
            self.dfs(root.right, targetSum, curSum + root.right.val)
            self.tmp_solutions.pop(-1)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.solutions = []
        self.tmp_solutions = []

        if root:
            self.dfs(root, targetSum, root.val)
        return self.solutions
        