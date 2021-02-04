class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def extend(root: TreeNode):
            nonlocal node
            if root is None:
                return

            extend(root.left)
            root.left = None
            node.right = root
            node = root
            extend(root.right)

        head = node = TreeNode()
        extend(root)
        return head.right
