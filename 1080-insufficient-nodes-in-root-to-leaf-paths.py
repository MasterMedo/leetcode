class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def valid(node: TreeNode, s: int) -> bool:
            if node is None:
                return False

            if node.left is None and node.right is None:
                return s + node.val >= limit

            if not (left := valid(node.left, s + node.val)):
                node.left = None
            if not (right := valid(node.right, s + node.val)):
                node.right = None
            return any([left, right])

        return root if valid(root, 0) else None
