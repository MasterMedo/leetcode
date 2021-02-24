class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node: TreeNode) -> TreeNode:
            if node is not None:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
                return node

        return invert(root)
