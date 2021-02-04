class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root

        return self.searchBST(root.left if root.val > val else root.right, val)
