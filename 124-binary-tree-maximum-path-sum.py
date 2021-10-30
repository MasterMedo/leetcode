from math import inf


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global path_sum

        def f(root: Optional[TreeNode]) -> int:
            global path_sum
            if root is None:
                return 0

            if root.left is None and root.right is None:
                path_sum = max(path_sum, root.val)
                return max(0, root.val)

            left = f(root.left)
            right = f(root.right)
            path_sum = max(path_sum, left + right + root.val)
            return max(0, max(left, right) + root.val)

        path_sum = -inf
        f(root)
        return path_sum
