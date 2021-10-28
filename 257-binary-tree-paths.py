class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [f"{root.val}"]

        return [
            f"{root.val}->{path}"
            for path in self.binaryTreePaths(root.left)
            + self.binaryTreePaths(root.right)
        ]
