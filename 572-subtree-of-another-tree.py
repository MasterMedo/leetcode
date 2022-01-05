class Solution:
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        def merkle(node):
            if node is None:
                return 0

            node.merkle = hash(
                " ".join(
                    map(str, (merkle(node.left), node.val, merkle(node.right)))
                )
            )
            return node.merkle

        def traverse(node):
            if node is None:
                return False

            if node.merkle == subRoot.merkle:
                return True

            return traverse(node.left) or traverse(node.right)

        merkle(root)
        merkle(subRoot)
        return traverse(root)
