# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []

        def dfs(root, tmp_answer):
            tmp_answer.append(root.val)

            if not (root.left or root.right):
                answer.append(tmp_answer)
                return

            if root.left:
                dfs(root.left, tmp_answer[:])
            
            if root.right:
                dfs(root.right, tmp_answer[:])
        
        dfs(root, [])
        return ["->".join(str(x) for x in item) for item in answer]
        
