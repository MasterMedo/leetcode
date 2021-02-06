class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            best = root.val
            left = right = 0
            if root.left is not None:
                x, left = helper(root.left)
                if x > best:
                    best = x
            if root.right is not None:
                x, right = helper(root.right)
                if x > best:
                    best = x

            best_without = max(
                best,
                right + root.val + left,
                right + root.val,
                left + root.val
            )
            best_with = root.val + max(right, left, 0)
            return best_without, best_with

        return max(helper(root))
