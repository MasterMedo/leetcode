from math import inf


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def f(root: Optional[TreeNode]) -> int:
            nonlocal path_sum
            if root is None:
                return 0

            left = f(root.left)
            right = f(root.right)
            path_sum = max(path_sum, left + right + root.val)
            return max(0, max(left, right) + root.val)

        path_sum = -inf
        f(root)
        return path_sum
