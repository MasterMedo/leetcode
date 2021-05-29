class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is not None:
            if root.val < low:
                return self.trimBST(root.right, low, high)

            elif root.val > high:
                return self.trimBST(root.left, low, high)

            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
