# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (not p) and q:
            return False
        elif (not q) and p:
            return False
        elif (not q) and (not p):
            return True

        queue = [(p, q)]
        while queue:
            p_root, q_root = queue.pop(0)
            if p_root.val != q_root.val:
                return False

            if p_root.left is None and q_root.left is not None:
                return False
            elif p_root.left is not None and q_root.left is None:
                return False
            
            if p_root.right is None and q_root.right is not None:
                return False
            elif p_root.right is not None and q_root.right is None:
                return False

            if p_root.left:
                if p_root.left.val == q_root.left.val:
                    queue.append((p_root.left, q_root.left))
                else:
                    return False

            if p_root.right: 
                if p_root.right.val == q_root.right.val:
                    queue.append((p_root.right, q_root.right))
                else:
                    return False
        return True