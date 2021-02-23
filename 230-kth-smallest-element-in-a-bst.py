class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node: TreeNode) -> int:
            if node is not None:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        return next(e for i, e in enumerate(inorder(root), 1) if i == k)
