class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, left: bool = False) -> int:
        if root is None:
            return 0

        if left and root.left is None and root.right is None:
            return root.val

        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
