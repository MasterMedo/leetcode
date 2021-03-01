class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def traverse(node: TreeNode) -> bool:
            if node is not None:
                left = traverse(node.left)
                right = traverse(node.right)
                if not left:
                    node.left = None
                if not right:
                    node.right = None

                return node.val == 1 or left or right

        dummy = TreeNode(right=root)
        traverse(dummy)
        return dummy.right
