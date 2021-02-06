from collections import deque
from math import inf


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = deque()
        prev = -inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
