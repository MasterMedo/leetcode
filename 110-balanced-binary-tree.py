class Solution:
    def helper(self, root: Optional[TreeNode]) -> Optional[int]:
        if root is None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        if left is None or right is None or abs(left - right) > 1:
            return None

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) is not None
