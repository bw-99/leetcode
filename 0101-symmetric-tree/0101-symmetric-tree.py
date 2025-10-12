from collections import deque

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            a, b = q.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            # 교차로 푸시: (a.left ↔ b.right), (a.right ↔ b.left)
            q.append((a.left,  b.right))
            q.append((a.right, b.left))
        return True