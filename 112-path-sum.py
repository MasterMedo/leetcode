class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == targetSum:
            return True

        return any(
            [
                self.hasPathSum(root.left, targetSum - root.val),
                self.hasPathSum(root.right, targetSum - root.val),
            ]
        )
