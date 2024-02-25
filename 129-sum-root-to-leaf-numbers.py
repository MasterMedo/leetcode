class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def partialSums(root: Optional[TreeNode], val: int = 0) -> list[int]:
            if root is None:
                return []
            root_val = val * 10 + root.val
            if root.left is None and root.right is None:
                return [root_val]
            sums = []
            if root.left is not None:
                sums.extend(partialSums(root.left, root_val))
            if root.right is not None:
                sums.extend(partialSums(root.right, root_val))
            return sums

        return sum(partialSums(root))
