class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def traverse(node: TreeNode) -> int:
            if node.left is None and node.right is None:
                return 1

            if node.left is None:
                return 1 + traverse(node.right)

            if node.right is None:
                return 1 + traverse(node.left)

            return 1 + min(traverse(node.left), traverse(node.right))

        return traverse(root) if root is not None else 0
