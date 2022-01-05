class Solution:
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        def find_candidates(node):
            if node is None:
                return False

            if node.val == subRoot.val:
                if is_equal(node, subRoot):
                    return True

            return find_candidates(node.left) or find_candidates(node.right)

        def is_equal(root, node):
            if root is None and node is None:
                return True

            if root is None or node is None:
                return False

            return (
                root.val == node.val
                and is_equal(root.left, node.left)
                and is_equal(root.right, node.right)
            )

        return find_candidates(root)
