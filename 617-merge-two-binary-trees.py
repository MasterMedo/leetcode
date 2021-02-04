class Solution:
    def mergeTrees(self, a: TreeNode, b: TreeNode) -> TreeNode:
        if a is None:
            return b

        if b is None:
            return a

        a.val += b.val
        a.left = self.mergeTrees(a.left, b.left)
        a.right = self.mergeTrees(a.right, b.right)

        return a
